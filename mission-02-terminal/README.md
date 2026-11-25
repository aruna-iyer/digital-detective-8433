# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective

Practise basic Terminal commands, create and manage files safely inside the assignment repository, understand flags and pipes, and learn what package managers do.

## 2. Work completed

I used Terminal from my assignment repository. Inside the Mission 2 folder, I created a practice folder and a text file. I added two lines, displayed the file, made a backup copy, and renamed the backup.

The file displayed:

First line
Second line

### Command reference

| Operation | Command used | What it does / what I observed |
|---|---|---|
| Show current folder | `pwd` | Displayed the path of my current folder. |
| List files and folders | `ls` | Listed the visible files and folders in the current folder. |
| Detailed listing including hidden files | `ls -la` | Showed a detailed list, including hidden files and file information. |
| Move to a folder | `cd mission-02-terminal` | Changed my current folder to the Mission 2 folder. |
| Create a folder | `mkdir -p terminal-practice` | Created the practice folder inside Mission 2. |
| Create an empty file | `touch notes.txt` | Created an empty text file inside the practice folder. |
| Write the first line | `printf "First line\n" > notes.txt` | Wrote the first line to the file. |
| Add the second line | `printf "Second line\n" >> notes.txt` | Added the second line without removing the first. |
| Display file contents | `cat notes.txt` | Displayed both lines in the Terminal. |
| Copy the file | `cp notes.txt backup.txt` | Made a separate copy of the file. |
| Rename the backup | `mv backup.txt notes-backup.txt` | Renamed the backup file. |
| Detailed listing with readable sizes | `ls -lah` | Displayed detailed file information, hidden files, and readable file sizes. |
| Send listing to show first lines | `ls -lah | head` | Displayed the first few lines of the detailed listing. |

### Answers about file operations

- `>` replaces a file’s contents. `>>` adds text to the end and keeps the existing contents.
- Copying creates another file with the same contents. Moving changes a file’s location or name.
- `pwd` tells me which folder Terminal is currently using.
- A directory listing helps me see the files and folders in the current location.

### Flags and pipes

The normal listing showed the visible files and folders. The detailed listing showed extra details about them. The `-a` flag included hidden files, `-l` displayed the details in a list, and `-h` showed file sizes in a readable format.

The pipe symbol `|` sends the output of one command to another command. In `ls -lah | head`, `ls -lah` created the detailed listing and `head` displayed only its first few lines.

### Package managers

A package manager helps install, update, and remove software. Homebrew is a package manager commonly used on macOS. I checked whether Homebrew was available and did not install or uninstall any software.

## 3. Commands / tools used

- `pwd` — showed my current folder.
- `ls` — listed files and folders.
- `ls -la` — displayed a detailed listing, including hidden files.
- `cd` — changed my current folder.
- `mkdir -p` — created the practice folder.
- `touch` — created an empty text file.
- `printf` — wrote the first line and appended the second line.
- `cat` — displayed the file contents.
- `cp` — copied the text file.
- `mv` — renamed the backup copy.
- `ls -lah` — showed detailed listings, hidden files, and readable file sizes.
- `head` — displayed the first few lines of the listing.
- `brew --version` and `brew list` — checked Homebrew, if it was installed.
- VS Code — used to write this README.

## 4. My understanding

I learned that Terminal commands work in the folder shown by `pwd`. I used `mkdir` and `touch` to make a folder and file, then used `printf`, `cat`, `cp`, and `mv` to edit, view, copy, and rename files. Flags change the information a command displays, and a pipe sends one command’s output to another command.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-02-terminal/README.md`
- `mission-02-terminal/terminal-practice/notes.txt`
- `mission-02-terminal/terminal-practice/notes-backup.txt`

## 8. Commit details

- Commit message: `Complete Terminal and file management mission`
- Pushed to GitHub: Yes, after confirming the files and commit are visible.