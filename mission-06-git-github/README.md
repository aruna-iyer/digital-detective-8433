# Mission 6 — Git and GitHub

## 1. Task / objective

Learn the basic Git workflow, create and publish a branch, open a Pull Request, and explain how branches and Pull Requests support collaboration.

## 2. Work completed

I checked the Git status, staged a change to the root README, committed it, and reviewed the recent commit history. I created a branch named `update-about`, added a “My Learning” section to the root README, and pushed the branch to GitHub.

I opened a Pull Request from `update-about` into `main`.

**Pull Request status:** Merged.

### Git workflow

| Git operation | What it does |
|---|---|
| Check repository status | Shows which files have changes and whether they are staged. |
| Stage selected changes | Selects changes to include in the next commit. |
| Create a commit | Saves a snapshot of the staged changes in Git history. |
| View commit history | Shows earlier commits and their messages. |

Staging selects changes for a commit. Committing saves those selected changes in the repository’s history.

### Branches and Pull Requests

A branch is a separate line of work in the repository. It lets someone make changes without changing the main branch immediately.

A Pull Request asks for a branch’s changes to be reviewed and considered for merging into another branch. It gives collaborators a place to review and discuss the changes before they are merged.

### Git command glossary

| Operation | Explanation |
|---|---|
| Initialize a repository | Starts Git tracking for a project folder. |
| Check status | Shows changed, staged, and untracked files. |
| Stage changes | Selects changes to include in the next commit. |
| Commit changes | Saves staged changes as a snapshot in Git history. |
| View history | Shows previous commits. |
| Create or list branches | Creates a separate line of work or shows existing branches. |
| Switch branches | Changes the branch currently being worked on. |
| Publish changes | Pushes local commits or a branch to GitHub. |
| Retrieve remote changes | Pulls changes from GitHub into the local repository. |

## 3. Commands / tools used

- `git status` — checked the repository’s current changes.
- `git add README.md` — staged the root README change.
- `git commit` — saved a change in Git history.
- `git log --oneline` — viewed recent commits.
- `git switch -c update-about` — created and switched to the new branch.
- `git push -u origin update-about` — published the branch to GitHub.
- `git switch main` — switched back to the main branch.
- `git pull origin main` — retrieved the latest changes from the main branch.
- GitHub — used to create and review the Pull Request.
- VS Code — edited the root README and this mission README.

## 4. My understanding

Git tracks changes to files. Staging chooses which changes go into the next commit, and committing saves them in the project history. A branch lets me work on changes separately, while a Pull Request lets people review those changes before they are merged.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `README.md`
- `mission-06-git-github/README.md`
- Pull Request: https://github.com/aruna-iyer/digital-detective-8433/pull/1

## 8. Commit details

- Commit message: `Complete Git and GitHub collaboration mission`
- Pushed to GitHub.