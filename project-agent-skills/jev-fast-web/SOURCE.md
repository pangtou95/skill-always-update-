# Source Record

- Upstream: https://github.com/browser-use/jev-ultrafast
- Reviewed commit: `452c1ad2dd628008f1d5608f28158d76e49e6cc0`
- Review date: `2026-09-18`
- Upstream license: MIT, https://github.com/browser-use/jev-ultrafast/blob/main/LICENSE
- Runtime dependency: `browser-harness==0.1.13` and `httpx[http2]>=0.28,<1`, Python 3.12+ at the reviewed commit.
- Import mode: original Codex Skill and adapter; upstream package installed separately, not copied into this library.

Upstream's 25% median time reduction was measured on three matched pairs of one Google Flights task, not on Codex Computer Use or a broad site benchmark. This Skill's local fixture probe measures only DOM observation latency. Full AI task testing needs TypeSafe and text-model API keys, a Chrome/CDP session, matching task definitions, and independent outcome checks; none of those are implied by the offline tests.
