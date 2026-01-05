# A guide to the Linux command line

## Introduction

In this guide i will be going over how the Linux command line works.
I will be discussing what parts it is made of and how they all work together.
I will also be covering command commands that every person should know.
And i will cover the basics of shell scripting.

## Parts of the command line

The linux command line is not one singular thing, it consists of many parts.
Each having a specific important purpose. Each of these parts is modular and can be swapped out to fit your needs.

**The Terminal:**

The terminal (often called terminal emulator), is a front end interface that allows you to interact with the shell of the system.
At its core its just a window in which you input text which gets passed down to the shell and then displays the output of the shell.
The terminal emulator does not understand commands, it just passes input to the shell and renders output.
Common terminal emulators include: ``Konsole``, ``Kitty``, ``Gnome Terminal``, and ``Ghostty``.

**The Shell:**

The shell is a program that interprets commands and then runs the right programs. 
It is like the bridge between the user and the kernel. its the most basic form of interacting with your system.
The most commonly used shell programs are: ``Bash``, ``Zsh``, ``Powershell``.

**The Binaries:**

The shell itself doesnt execute anything, it just interprets a command and then executes the correct binary programs with the correct arguments.
Each command is just calling one or more of those binary programs.
So the commands like: ``cd``, ``ls``, ``cat``.
Are basically just names of executable binaries.
All major Linux distro's come with a standard set of these commands (binaries).
Most of these binaries are part one of the following projects: ``gnu-coreutils``, ``util-linux``, ``procps-ng``, ``iproute2``, ``iputils``. and then there are a number of binaries that are their own projects.
But you can be sure that all major Linux distros come with the binaries of those 5 projects, so if you learn those you are set.

## Commonly used commands

**📂 Files & Directories**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>ls</td><td>gnu</td><td>List files and directories</td><td>ls /home</td></tr>
    <tr><td>cd</td><td>bash</td><td>Change the current directory</td><td>cd /home</td></tr>
    <tr><td>pwd</td><td>gnu</td><td>Print current working directory</td><td>pwd</td></tr>
    <tr><td>cp</td><td>gnu</td><td>Copy files or directories</td><td>cp file.txt copy.txt</td></tr>
    <tr><td>mv</td><td>gnu</td><td>Move or rename files/directories</td><td>mv file.txt moved.txt</td></tr>
    <tr><td>rm</td><td>gnu</td><td>Remove files or directories</td><td>rm file.txt</td></tr>
    <tr><td>mkdir</td><td>gnu</td><td>Create directories</td><td>mkdir folder</td></tr>
    <tr><td>rmdir</td><td>gnu</td><td>Remove empty directories</td><td>rmdir folder</td></tr>
    <tr><td>touch</td><td>gnu</td><td>Create empty file or update timestamp</td><td>touch file.txt</td></tr>
    <tr><td>cat</td><td>gnu</td><td>Display or concatenate file contents</td><td>cat file.txt</td></tr>
    <tr><td>echo</td><td>bash</td><td>Print text to stdout</td><td>echo "hello world"</td></tr>
    <tr><td>basename</td><td>gnu</td><td>Strip directory path from filename</td><td>basename /path/file.txt</td></tr>
    <tr><td>dirname</td><td>gnu</td><td>Strip filename to show directory path</td><td>dirname /path/file.txt</td></tr>
  </tbody>
</table>

**🔒 Privileges & Ownership**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>chmod</td><td>gnu</td><td>Change file permissions</td><td>chmod +x script.sh</td></tr>
    <tr><td>chown</td><td>gnu</td><td>Change file owner and group</td><td>chown user:group file.txt</td></tr>
    <tr><td>sudo</td><td>other</td><td>Execute command as root user</td><td>sudo rm file.txt</td></tr>
    <tr><td>su</td><td>util-linux</td><td>Switch to root user</td><td>su</td></tr>
  </tbody>
</table>

**🔍 Search & Filters**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>find</td><td>gnu</td><td>Search for files in directories</td><td>find /home -name "*.txt"</td></tr>
    <tr><td>grep</td><td>gnu</td><td>Search text in files using patterns</td><td>grep "error" log.txt</td></tr>
    <tr><td>sed</td><td>gnu</td><td>Filters text using given rules</td><td>sed 's/old/new/' file.txt</td></tr>
    <tr><td>xargs</td><td>gnu</td><td>Use output as arguments</td><td>cat dirs.txt | xargs rmdir</td></tr>
  </tbody>
</table>

**⚙️ Processes**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>ps</td><td>procps-ng</td><td>Show currently running processes</td><td>ps aux</td></tr>
    <tr><td>kill</td><td>gnu</td><td>Terminate a process by PID</td><td>kill 1234</td></tr>
    <tr><td>pkill</td><td>gnu</td><td>Terminate a process by name</td><td>pkill firefox</td></tr>
  </tbody>
</table>

**📦 Archiving & Compression**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>tar</td><td>gnu</td><td>Archive or extract files</td><td>tar -cvf archive.tar file.txt</td></tr>
    <tr><td>gzip</td><td>gnu</td><td>Compress files</td><td>gzip archive.tar</td></tr>
    <tr><td>gunzip</td><td>gnu</td><td>Decompress gzip files</td><td>gunzip archive.tar.gz</td></tr>
  </tbody>
</table>

**🌐 Networking**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>ping</td><td>iputils</td><td>Test network connectivity</td><td>ping google.com</td></tr>
    <tr><td>ip</td><td>iproute2</td><td>Show or configure network interfaces</td><td>ip addr</td></tr>
    <tr><td>curl</td><td>other</td><td>Downloads files from the web</td><td>curl -O http://example.com/file</td></tr>
    <tr><td>wget</td><td>other</td><td>Downloads files from the web</td><td>wget http://example.com/file</td></tr>
  </tbody>
</table>

**💾 Storage & Disks**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>mount</td><td>util-linux</td><td>Mount disks or drive</td><td>mount /dev/sda1 /mnt/usb</td></tr>
    <tr><td>umount</td><td>util-linux</td><td>Unmount disks or drive</td><td>umount /mnt/usb</td></tr>
    <tr><td>fdisk</td><td>util-linux</td><td>Manages disks or drives</td><td>fdisk -l</td></tr>
  </tbody>
</table>

**🖥️ System & Other**
<table>
  <thead>
    <tr><th>Command</th><th>Project</th><th>Description</th><th>Example</th></tr>
  </thead>
  <tbody>
    <tr><td>shutdown</td><td>util-linux</td><td>Shut down the system</td><td>shutdown</td></tr>
    <tr><td>reboot</td><td>util-linux</td><td>Reboot the system</td><td>reboot</td></tr>
    <tr><td>clear</td><td>gnu</td><td>Clears the terminal output</td><td>clear</td></tr>
    <tr><td>env</td><td>gnu</td><td>Configure environment variables</td><td>env</td></tr>
    <tr><td>export</td><td>gnu</td><td>Configure temp environment variables</td><td>export VAR=value</td></tr>
    <tr><td>which</td><td>other</td><td>Locate a command in PATH</td><td>which cat</td></tr>
    <tr><td>whereis</td><td>util-linux</td><td>Locate binaries</td><td>whereis cat</td></tr>
    <tr><td>type</td><td>bash</td><td>Show command type information</td><td>type cat</td></tr>
    <tr><td>uname</td><td>gnu</td><td>Show system and kernel information</td><td>uname -a</td></tr>
    <tr><td>uptime</td><td>procps-ng</td><td>Show system uptime and load</td><td>uptime</td></tr>
    <tr><td>who</td><td>util-linux</td><td>Show who is logged in</td><td>who</td></tr>
    <tr><td>whoami</td><td>gnu</td><td>Show current user</td><td>whoami</td></tr>
    <tr><td>id</td><td>gnu</td><td>Show user and group IDs</td><td>id</td></tr>
    <tr><td>groups</td><td>gnu</td><td>List groups for a user</td><td>groups</td></tr>
  </tbody>
</table>

## Shebangs

You will often encounter shell scripts starting with ``#!/bin/bash``, the ``#!`` is called a shebang. It is used to specify which interpreter will be used to run the script. 
So if your script uses bash specific scripting syntax, then you put a bash shebang on the first line of your script. 
If you want your script to be posix compatible so it can run on other unix like systems that don't have bash, then you use the sh shebang. 
The sh shell is compatible with alot more unix like operating systems than just linux, making your scripts more portable at the cost of bash specific scripting features.

**Bash Compatible**
<table>
  <tr>
    <th>Shebang</th>
    <th>Comment</th>
    <th>Debian</th>
    <th>Arch</th>
    <th>Fedora</th>
    <th>MacOS</th>
    <th>FreeBSD</th>
  </tr>
  <tr>
    <td>#!/bin/bash</td>
    <td>the classic bash location on linux</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>❌</td>
    <td>❌</td>
  </tr>
  <tr>
    <td>#!/usr/bin/bash</td>
    <td>the modern bash location on linux</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>❌</td>
    <td>❌</td>
  </tr>
  <tr>
    <td>#!/bin/env bash</td>
    <td>the env binary is almost never in bin/</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
  </tr>
  <tr>
    <td>#!/usr/bin/env bash</td>
    <td>finds bash via the path</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
</table>

**Posix Compatible**
<table>
  <tr>
    <th>Shebang</th>
    <th>Comment</th>
    <th>Debian</th>
    <th>Arch</th>
    <th>Fedora</th>
    <th>MacOS</th>
    <th>FreeBSD</th>
  </tr>
    <tr>
    <td>#!/bin/sh</td>
    <td>the default sh location on most systems</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
  <tr>
    <td>#!/usr/bin/sh</td>
    <td>the sh binary is almost never in usr/bin/</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
  </tr>
  <tr>
    <td>#!/bin/env sh</td>
    <td>the env binary is almost never in bin/</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
    <td>❌</td>
  </tr>
  <tr>
    <td>#!/usr/bin/env sh</td>
    <td>finds sh via the path</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
    <td>✅</td>
  </tr>
</table>

**Conclusion**

Just use ``#!/bin/bash`` or ``#!/usr/bin/bash`` for linux bash scripts.

Just use ``#!/usr/bin/env bash`` for cross platform bash scripts.

Just use ``#!/bin/sh`` or ``#!/usr/bin/env sh`` for cross platform posix scripts.

## File globbing

In many tools including many shells you can filter your file or directory selection with something called **Globbing**,
and its a way of quickly filtering your file or directory selection selection. If you want to select a specific set of files or directories
from the command line you can use this following specific syntax that is specifically designed for that purpose.

**Basics**
<table>
  <tr>
    <td><code>.</code></td>
    <td>Current directory</td>
  </tr>
  <tr>
    <td><code>..</code></td>
    <td>Parent directory</td>
  </tr>
  <tr>
    <td><code>~</code></td>
    <td>Home directory</td>
  </tr>
  <tr>
    <td><code>*</code></td>
    <td>Matches any file or directory</td>
  </tr>
  <tr>
    <td><code>**</code></td>
    <td>Matches any file or directory recursively</td>
  </tr>
  <tr>
    <td><code>/</code></td>
    <td>Directory separator</td>
  </tr>
</table>

**Examples**
```bash
ls * # list files and dirs in the current directory
ls ** # list files and dirs recursively starting from this dir
ls *.txt # list text files in this dir
ls **/*.txt # list text files recursively starting from this dir

ls . # list files and dirs inside the current directory
ls .. # list files and dirs inside the parent directory
ls ~ # list files and dirs inside the home directory
ls / # list files and dirs inside the root directory

ls text* # list files and dirs starting with "text" in the name
ls *text # list files and dirs ending with "text" in the name
ls *text* # list files and dirs containing "text" anywhere in the name
ls file.c* # list files with extensions starting with "c" (c, cpp, cs)

ls file?.txt # list txt files named "file" + any character (file1.txt, file2.txt)
ls file??.txt # list txt files named "file" + any 2 characters (file12.txt, file13.txt)

ls file{1,2,3}.txt # list files: file1.txt, file2.txt, and file3.txt
ls {foo,bar,hello}.txt # list files: foo.txt, bar.txt, and hello.txt

ls file[123].txt # list files: file1.txt, file2.txt, and file3.txt
ls file[a-f].txt # list files with a single char in the range a-c (fileb.txt, filec.txt)
ls file[!0-9].txt # list files where the character after "file" is NOT a digit (0-9)
```

## Piping

comming soon...

## Chaining

comming soon...

## Loops

comming soon...