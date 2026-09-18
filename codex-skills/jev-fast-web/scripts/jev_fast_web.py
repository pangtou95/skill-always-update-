#!/usr/bin/env python3
"""Guarded terminal entrypoint for an optional Jev Ultrafast runtime."""

import argparse
import importlib.util
import json
import os
import statistics
import sys
import time
from urllib.parse import quote, urlparse


def emit(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True))


def hostname(value):
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("Use a full http(s) URL without embedded credentials")
    return parsed.hostname.lower()


def readiness():
    return {
        "runtime_importable": importlib.util.find_spec("jev_ultrafast") is not None,
        "typesafe_key_present": bool(os.environ.get("TYPESAFE_API_KEY")),
        "text_model_key_present": bool(os.environ.get("TEXT_MODEL_API_KEY")),
        "cdp_override_configured": bool(os.environ.get("BU_CDP_URL") or os.environ.get("BU_CDP_WS")),
    }


def probe(iterations):
    if not 1 <= iterations <= 100:
        raise ValueError("iterations must be between 1 and 100")
    if not readiness()["runtime_importable"]:
        raise RuntimeError("Jev runtime is missing from this Python environment")
    from jev_ultrafast.browser import Browser

    html = (
        "<!doctype html><title>Local probe</title><h1>Controls</h1>"
        "<label>Search<input aria-label='Search'></label>"
        "<button type='button'>Apply</button><select aria-label='Mode'>"
        "<option>All</option><option>Recent</option></select>"
    )
    browser = Browser("data:text/html," + quote(html))
    try:
        browser.observe(screenshot=False)
        samples = []
        for _ in range(iterations):
            start = time.perf_counter()
            state = browser.observe(screenshot=False)
            samples.append((time.perf_counter() - start) * 1000)
        emit({
            "result": "pass",
            "controls_observed": len(state["actions"]),
            "iterations": iterations,
            "median_observe_ms": round(statistics.median(samples), 2),
            "scope": "local DOM observation only; no model calls or Computer Use comparison",
        })
    finally:
        browser.close()


def run(args):
    initial_host = hostname(args.url)
    allowed = {value.lower() for value in args.allow_host}
    if not allowed or initial_host not in allowed:
        raise ValueError("The starting URL host must be explicitly allowlisted")
    if not 1 <= args.max_actions <= 60:
        raise ValueError("max-actions must be between 1 and 60")
    if not args.live:
        raise ValueError("Live model calls require --live")
    state = readiness()
    if not state["runtime_importable"] or not state["typesafe_key_present"] or not state["text_model_key_present"]:
        raise RuntimeError("Jev runtime, TYPESAFE_API_KEY and TEXT_MODEL_API_KEY are required")

    from jev_ultrafast import Agent

    status = "budget_exhausted"
    final = None
    with Agent(args.url, args.goal) as agent:
        for _ in range(args.max_actions * 2):
            final = agent.command("tick")
            current_url = final["page"]["url"]
            if hostname(current_url) not in allowed:
                status = "left_allowlisted_host"
                break
            if final["status"] in {"done", "blocked"}:
                status = final["status"]
                break
            if len(final["history"]) >= args.max_actions:
                break
        if final is None:
            raise RuntimeError("No browser observation was returned")

        verified = status == "done" and bool(args.expect_url_prefix or args.expect_text)
        if args.expect_url_prefix:
            verified = verified and final["page"]["url"].startswith(args.expect_url_prefix)
        if args.expect_text:
            verified = verified and args.expect_text in final["page"].get("text", "")
        emit({
            "status": status,
            "verified_by_expectation": verified,
            "actions": len(final["history"]),
            "elapsed_ms": final["elapsed_ms"],
            "final_url": final["page"]["url"],
        })
    return 0 if verified else 3


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check", help="Report runtime and key presence without exposing values")
    probe_parser = sub.add_parser("probe", help="Time local DOM snapshots without model calls")
    probe_parser.add_argument("--iterations", type=int, default=30)
    run_parser = sub.add_parser("run", help="Run one explicitly enabled, bounded web task")
    run_parser.add_argument("--url", required=True)
    run_parser.add_argument("--allow-host", action="append", required=True)
    run_parser.add_argument("--goal", required=True)
    run_parser.add_argument("--expect-url-prefix")
    run_parser.add_argument("--expect-text")
    run_parser.add_argument("--max-actions", type=int, default=12)
    run_parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "check":
            emit(readiness())
            return 0
        if args.command == "probe":
            probe(args.iterations)
            return 0
        return run(args)
    except (RuntimeError, ValueError) as error:
        emit({"status": "error", "message": str(error)})
        return 2


if __name__ == "__main__":
    sys.exit(main())
