# Git Workflow

## Repository
https://github.com/miladarmani/devops-final-project

## Branching
- `main` — stable branch
- Feature/docs work done on separate branches, e.g. `docs/add-lessons-learned`

## Pull requests
At least one PR was opened and merged (adding lessons-learned notes) to
demonstrate the branch → PR → review → merge flow, rather than committing
directly to `main`.

## Secrets
`.gitignore` excludes TLS keys/certs and other sensitive files so they
are never committed.
