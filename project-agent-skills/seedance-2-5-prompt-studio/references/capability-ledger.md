# Capability Ledger

## Evidence levels

1. **Official model claim**: published by ByteDance Seed. It describes intended capability, not availability on every account or provider.
2. **Surface observation**: visible in a named product/account/region on a stated date.
3. **Provider documentation**: request fields or model IDs are documented, but a route may still be inactive.
4. **Live verification**: a real request completed and returned a usable result with observed billing and limits.
5. **Community example**: useful creative evidence, but not sufficient to prove model, settings, edits, or reproducibility.

## Inspected state

Last research pass: 2026-08-05, Asia/Tokyo.

| Claim | Evidence | Operational treatment |
| --- | --- | --- |
| Seedance 2.5 launched on 2026-07-31 | ByteDance Seed launch article | Official release |
| Up to 30 seconds in one pass and multi-round extension | ByteDance Seed | Verify duration options on selected surface |
| Up to 30 images, 10 videos, and 10 audio references | ByteDance Seed | Treat as an upper model claim, not a guaranteed per-provider request limit |
| Long-form, multimodal reference, timestamp editing, green-screen/camera/reference edits | ByteDance Seed | Use as prompt architecture; verify exact UI/API controls |
| Rolling out in Jimeng and Doubao Pro | ByteDance Seed | Account and region dependent |
| BytePlus ModelArk API coming soon | ByteDance Seed | Verify before implementation |
| EvoLink docs published; generation route pending | EvoLink status page inspected 2026-08-05 | `docs-only`; do not submit and claim generation |
| EvoLink page states first-party API opens 2026-08-07 | EvoLink status page | Future-dated claim; recheck on or after that date |
| 4K showcase/product experience | Product/gallery claims | Do not map to an EvoLink API tier unless current docs expose it |

## Sources

- ByteDance Seed launch: https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5
- ByteDance Seed model page: https://seed.bytedance.com/seedance2_5
- EvoLink gallery: https://evolink.ai/seedance-2-5-prompts
- EvoLink status page: https://evolink.ai/seedance-2-5

At execution time, prefer the selected provider's current primary documentation over this dated ledger.
