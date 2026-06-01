---
name: ppf-contact-solver-workflows
description: Use when running, scripting, deploying, testing, or explaining ZOZO/st-tech ppf-contact-solver workflows for physics-based contact simulation involving shells, solids, rods, GPU/CUDA Docker, JupyterLab, Blender add-on, Python API, MCP control, or Windows native builds.
---

# PPF Contact Solver Workflows

Source analyzed: https://github.com/st-tech/ppf-contact-solver

Use this skill for contact simulation workflows, deployment, scripting, Blender integration, Docker/GPU setup, MCP control, and test/build triage.

## Repository Shape

- Python frontend API is under `frontend/`.
- Jupyter examples are under `examples/*.ipynb`.
- Blender scripts are under `examples/blender/`.
- Rust/Python bindings and solver crates are under `crates/`.
- Blender add-on docs are under `docs/blender_addon/`.
- Documentation generators are in `docs/generate_*_reference.py`.
- Windows native build scripts are under `build-win-native/`.
- Assets and gallery media are under `asset/`.

The project is Apache-2.0 and focused on offline, physics-based contact simulation, not real-time simulation.

## Hardware And Runtime Requirements

Default practical requirement:

- NVIDIA GPU with CUDA 12.8 or newer support.
- x86 architecture; arm64 is not supported by the analyzed README.
- Docker with NVIDIA Container Toolkit on Linux/Windows, or Windows native executable.
- Blender 5+ only when using the Blender add-on.

Do not recommend running local warmup paths casually; the README warns that `warmup.py` is likely to fail locally and be difficult to clean up.

## Quick Docker Run

Linux/macOS shell syntax for a GPU-enabled host:

```bash
MY_WEB_PORT=8080
MY_BLENDER_PORT=9090
IMAGE_NAME=ghcr.io/st-tech/ppf-contact-solver-compiled:latest
docker run --rm -it \
  --name ppf-contact-solver \
  --gpus all \
  -p ${MY_WEB_PORT}:${MY_WEB_PORT} \
  -p ${MY_BLENDER_PORT}:${MY_BLENDER_PORT} \
  -e WEB_PORT=${MY_WEB_PORT} \
  $IMAGE_NAME
```

JupyterLab should become available at `http://localhost:8080`.

For background use, replace `--rm` with `-d`, then stop/remove explicitly when done.

## Frontend Choices

There are two main user-facing workflows:

- Blender add-on: build scenes visually or script them in Blender, then run simulations through the solver.
- JupyterLab/Python: script scenes, assets, parameters, sessions, previews, builds, runs, and logs in notebooks.

Both communicate with the same solver engine.

## Python Scene Workflow

The common notebook pattern is:

1. Create or load assets.
2. Create a scene.
3. Add shells, solids, rods, pins, transforms, and jitter where needed.
4. Build and report the scene.
5. Preview the initial state.
6. Create a session from the scene.
7. Set simulation/material parameters.
8. Build and run the session.
9. Inspect logs and exported results.

When writing examples, prefer adapting an existing notebook such as `examples/drape.ipynb`, `examples/woven.ipynb`, or Blender scripts under `examples/blender/`.

## Blender And MCP

The repo exposes Blender add-on tools and an MCP server so an agent can drive simulation workflows through natural language.

When scripting Blender:

- Import the add-on API through Blender's extension namespace.
- Use the documented `solver` API surface.
- Keep procedural scene creation deterministic when debugging.
- Use preview/export steps to verify geometry before starting expensive runs.

When using MCP, separate scene creation, parameter adjustment, simulation run, and result fetch into explicit steps so failures are easy to localize.

## Testing And CI

The project has multiple test surfaces:

- frontend Python tests in `frontend/tests/`;
- example notebook execution tests;
- Blender add-on CI;
- Windows native build tests;
- Docker build workflow.

For local CPU/non-GPU contexts, focus on lint/static checks and docs generation. Do not claim full solver validation without a suitable CUDA GPU/runtime.

Useful documentation generators:

```bash
python docs/generate_blender_api_reference.py
python docs/generate_mcp_reference.py
```

## Windows Native Build

The `build-win-native/` workflow is designed to be self-contained and does not require admin-installed build tools. Important scripts:

- `warmup.bat`: downloads/prepares portable tools.
- `build.bat`: compiles CUDA library and Rust binary.
- `bundle.bat`: creates distribution.
- `fast-check-all.bat`: runs example notebook tests.
- `clean-build.bat`, `clean-env.bat`, `clear-all.bat`: cleanup levels.

First warmup can be large and slow because it downloads many GB of tools.

## Simulation Debugging

For simulation failures:

1. Verify runtime first: GPU, driver, CUDA support, Docker GPU access.
2. Check scene geometry: intersections, scale, pin constraints, material parameters.
3. Reduce to a smaller example.
4. Inspect logs and channel names.
5. Compare against a known working example.
6. Only then adjust solver parameters.

Avoid presenting large-scale examples as quick smoke tests; the README notes some can take days.

