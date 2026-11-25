# Mission 3 — Understand the operating system

## 1. Task / objective

Explore macOS, running processes, storage, paths, and file permissions. Explain some responsibilities of an operating system.

## 2. Work completed

I used System Settings to check information about my Mac and Terminal to inspect storage, system activity, running processes, paths, and file permissions.

### System information

| Information explored | What it tells you | My privacy-safe observation |
|---|---|---|
| Operating system / system details | Identifies the operating system and information about the computer. | I checked System Settings > General > About and confirmed that my computer uses macOS. |
| Current account identity | Identifies the account being used on the computer. | I checked my account on the Mac. I have not included the account name in this README. |
| Available and used storage | Shows storage volumes and how much space is used and available. | I ran `df -h`. It displayed storage sizes and available space in a readable format. I have not copied any private volume or device details here. |
| System activity snapshot | Shows a brief view of system activity and resource use. | I ran `top -l 1`. It displayed a snapshot of system activity. |
| Running processes | Shows programs and other tasks currently running on the computer. | I ran `ps aux`. It displayed a list of processes, including a PID column. I have not included usernames or other identifying output. |

### Processes

A process is a program or task that is currently running. In the output from `ps aux`, the PID column contains a number that identifies each process. Examples of processes I may see include a web browser, Finder, and background macOS tasks.

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

- System Settings > General > About — checked information about my Mac.
- System Settings > General > Storage — viewed storage information.
- `df -h` — displayed used and available storage.
- `top -l 1` — showed a snapshot of system activity.
- `ps aux` — listed running processes and their PIDs.
- `pwd` — showed the folder I was working in.
- `ls` — listed files and folders.
- `cd` — moved between folders.
- `ls -l` — displayed file permissions and other file details.
- Activity Monitor — viewed running apps and processes.
- VS Code — wrote this README.

## 4. My understanding

The operating system manages programs, memory, devices, files, and permissions. A process is a running program or task, and its PID helps identify it in the process list. The `df -h` command reports storage use, while `top -l 1` shows a brief system activity snapshot. Absolute paths start from the filesystem root, while relative paths depend on the current folder.

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