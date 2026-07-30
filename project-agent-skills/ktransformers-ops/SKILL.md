---
name: ktransformers-ops
description: Plan, install, benchmark, and troubleshoot kvcache-ai/KTransformers CPU-GPU heterogeneous LLM inference and fine-tuning workflows, including kt-kernel, MoE models, quantization, expert placement, SGLang integration, and LLaMA-Factory SFT. Use when the user names KTransformers or needs large-model inference or training with constrained GPU memory and substantial CPU resources.
---

# KTransformers Operations

Treat KTransformers as a hardware-sensitive external framework. Do not begin installation until the target model, operating system, CPU instruction set, GPU backend, VRAM, RAM, disk, driver, and CUDA/ROCm/oneAPI versions are known.

## Choose A Path

- `kt-kernel` inference: CPU-GPU heterogeneous serving and optimized MoE kernels.
- SFT: KTransformers integration with LLaMA-Factory and Accelerate/FSDP2.
- Existing legacy paths: inspect the exact upstream version before following older tutorials.

## Workflow

1. Record hardware with `uname`, CPU flags, GPU inventory, driver/toolkit versions, RAM, NUMA topology, and free disk.
2. Match the model and quantization format to a current upstream tutorial. Do not assume support from the model family name alone.
3. Create an isolated environment and pin the inspected KTransformers commit or release.
4. Build only the selected path and capture compiler output.
5. Run the smallest documented smoke test before downloading or loading a production-scale model.
6. Benchmark prompt length, concurrency, time to first token, output throughput, peak VRAM/RAM, and accuracy-sensitive settings.
7. For SFT, validate one batch and checkpoint save/resume before a long run.

Never present upstream benchmark numbers as expected local performance. Avoid automatic kernel/driver replacement, global Python installs, or multi-hundred-gigabyte downloads without explicit scope. Read `references/source.md` for the inspected source and license.
