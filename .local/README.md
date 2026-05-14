# .local/

This directory is **gitignored**. Use it for personal, machine-specific, or project-private content that you want to keep alongside the skill but never publish.

Common uses:

- Your own `preset-<project>.md` files with project-specific data paths, station names, parameter values, and limitations. The fast-path detection in `SKILL.md` and `references/startup-interview.md` scans `references/preset-*.md`, so if you want a private preset to be auto-detected, symlink it from `references/`:

  ```sh
  ln -s ../.local/preset-myproject.md references/preset-myproject.md
  ```

  The symlink target is gitignored; the symlink itself can also be gitignored or left untracked depending on your workflow.

- Local Claude Code overrides or session notes.
- Anything else you do not want in the public repository.

Anything inside `.local/` is excluded by `.gitignore`.
