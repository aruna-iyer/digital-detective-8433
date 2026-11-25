# Mission 3 — Understand the operating system

## 1. Task / objective

Explore macOS, running processes, storage, paths, and file permissions. Explain some responsibilities of an operating system.

## 2. Work completed

I used macOS System Settings and Activity Monitor to explore my computer. In Terminal, I practised moving between folders, listing files, and checking the current folder. I also checked the permissions of a practice file.

### System information

| Information explored | What it tells you | My privacy-safe observation |
|---|---|---|
| Operating system / system details | Identifies the operating system and information about the computer. | I checked System Settings > General > About. It showed that my computer uses macOS. |
| Current account identity | Identifies the account being used on the computer. | I checked the account in System Settings. I have not included the account name in this README. |
| Available and used storage | Shows how much storage is used and how much is available. | I checked System Settings > General > Storage. It displayed the storage used and available on my Mac. |
| System activity snapshot | Shows apps and processes that are currently running. | I opened Activity Monitor and observed running apps and background processes. |

### Processes

A process is a program or task that is currently running on the computer. Activity Monitor displays information about running processes, including their process identifiers (PIDs). A PID is a number used to distinguish one running process from another.

Examples of processes I may see include a web browser and Finder. The list can also include background processes that help macOS work.

### Paths and permissions

An absolute path starts from the filesystem’s root location. A relative path is written from the folder Terminal is currently using.

- Absolute path example: `/Users/[redacted]/digital-detective-8433/mission-02-terminal/terminal-practice/notes.txt`
- Relative path example: `mission-02-terminal/terminal-practice/notes.txt`

I used `ls -l` to view the practice file’s permissions. In the permission letters, `r` means read, `w` means write, and `x` means execute. For a regular text file, the owner can read or edit it when the corresponding `r` or `w` letters appear. The `x` permission allows a file to be run as a program.

### Operating-system responsibilities

| OS responsibility | My explanation | Example |
|---|---|---|
| Process management | The operating system starts programs and shares processor time between running tasks. | macOS lets Chrome and Finder run at the same time. |
| Memory management | The operating system manages computer memory for programs that are running. | macOS gives memory to Chrome while it is open. |
| Device management | The operating system helps programs communicate with connected hardware. | macOS lets a program send a document to a printer. |
| File management | The operating system organizes files and folders and helps programs open and save them. | Finder lets me locate the downloaded Python textbook. |
| User interface / shell | The operating system provides ways to use the computer, such as the desktop, Finder, and Terminal. | I use Finder to browse files and Terminal to enter commands. |
| Security and permissions | The operating system controls account access and what users or programs can do with files. | File permissions determine whether a user can read, edit, or run a file. |

## 3. Commands / tools used

- `pwd` — showed the folder I was working in.
- `ls` — listed the files and folders in that location.
- `cd` — moved me into another folder.
- `ls -l` — displayed file permissions and other file details.
- System Settings > General > About — showed information about my Mac.
- System Settings > General > Storage — showed storage use and available space.
- Activity Monitor — showed apps and other processes that were running.
- VS Code — used to write this README.

## 4. My understanding

The operating system manages programs, memory, devices, files, and permissions. A process is a running program, and its PID helps identify it. Absolute paths start from the filesystem root, while relative paths depend on the current folder. File permissions show whether a user can read, write, or execute a file.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-03-operating-system/README.md`
- `mission-02-terminal/terminal-practice/notes.txt`

## 8. Commit details

- Commit message: `Document operating system and file management`
- Pushed to GitHub.