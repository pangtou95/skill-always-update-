---
name: twenty-crm-development
description: Use when building, extending, self-hosting, debugging, or contributing to Twenty open-source CRM, including Twenty apps, objects/fields/views, Nx/Yarn monorepo work, NestJS server, React frontend, Docker/Helm deployment, SDK generation, and e2e tests based on twentyhq/twenty.
---

# Twenty CRM Development

Source analyzed: https://github.com/twentyhq/twenty

Use this skill for Twenty CRM app development, monorepo navigation, self-hosting, SDK usage, and contribution work.

## Repository Shape

Twenty is a Yarn 4 + Nx monorepo. Main packages include:

- `packages/twenty-front`: React frontend.
- `packages/twenty-server`: NestJS backend.
- `packages/twenty-ui`: shared UI components.
- `packages/twenty-shared` and `packages/twenty-utils`: shared logic.
- `packages/twenty-sdk`: app/extension SDK.
- `packages/twenty-client-sdk`: generated GraphQL/client SDK.
- `packages/twenty-cli` and `packages/create-twenty-app`: app scaffolding and publishing.
- `packages/twenty-docker`: Docker Compose, Helm chart, container files.
- `packages/twenty-docs`: documentation.
- `packages/twenty-e2e-testing`: Playwright tests and page objects.

The root package requires Node `^24.5.0`, Yarn `>=4.0.2`, and is AGPL-3.0 licensed.

## Product Model

Twenty is an open-source CRM where technical teams can define and version CRM primitives as code:

- objects;
- fields;
- views/layouts;
- workflows;
- agents and logic functions;
- workspace-specific metadata.

When implementing features, first identify whether the task is core product, app SDK, CLI, documentation, deployment, or e2e coverage.

## Common Commands

Use Yarn, not npm.

```bash
yarn install
yarn start
yarn nx graph
yarn nx run twenty-front:start
yarn nx run twenty-server:start
yarn nx run twenty-server:worker
```

Root start script runs frontend, server, and worker once port `3000` is ready:

```bash
yarn start
```

Docs generation:

```bash
yarn docs:generate
yarn docs:generate-navigation-template
yarn docs:generate-paths
```

Prefer package-specific Nx targets after inspecting `project.json` in the target package.

## App SDK Pattern

For custom CRM apps, the README pattern is:

```bash
npx create-twenty-app my-app
```

Define objects as code:

```ts
import { defineObject, FieldType } from 'twenty-sdk/define';

export default defineObject({
  nameSingular: 'deal',
  namePlural: 'deals',
  labelSingular: 'Deal',
  labelPlural: 'Deals',
  fields: [
    { name: 'name', label: 'Name', type: FieldType.TEXT },
    { name: 'amount', label: 'Amount', type: FieldType.CURRENCY },
  ],
});
```

Publish:

```bash
npx twenty app:publish --private
```

When creating or reviewing app objects, check naming consistency: singular/plural names, labels, field types, relationship fields, and migration/version behavior.

## Development Workflow

1. Locate the package boundary before editing.
2. Inspect the local package `project.json`, `package.json`, and nearby tests.
3. Follow existing patterns for metadata, workspace isolation, permissions, and localization.
4. For backend work, respect NestJS module/service boundaries and queue behavior.
5. For frontend work, reuse `twenty-ui` and established state patterns before adding dependencies.
6. For SDK generation, regenerate and test generated artifacts instead of hand-editing generated files.

## Testing Workflow

Use the closest target:

- unit/integration tests through package Nx targets;
- Playwright e2e from `packages/twenty-e2e-testing`;
- SDK tests in `packages/twenty-client-sdk`;
- Helm chart tests under `packages/twenty-docker/helm/twenty/tests`.

When changing user workflows, add or update e2e tests and page objects under `packages/twenty-e2e-testing/lib/pom/`.

## Deployment Notes

Self-hosting is supported through Docker Compose and Helm:

- Docker assets: `packages/twenty-docker/docker-compose.yml`
- Dev Compose: `packages/twenty-docker/docker-compose.dev.yml`
- Helm chart: `packages/twenty-docker/helm/twenty/`

For deployment issues, verify PostgreSQL, Redis, server, worker, storage env vars, token secrets, ingress/server URL, and migrations.

## Large Monorepo Discipline

Do not run broad expensive tasks first. Prefer:

```bash
yarn nx show projects
yarn nx affected -t test
yarn nx affected -t lint
```

If macOS case-insensitive checkout reports file collisions in website illustration paths, avoid touching those collided files unless the task specifically concerns the website assets.

