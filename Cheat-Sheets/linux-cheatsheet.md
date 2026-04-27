# Linux Cheat Sheet

---

## Command: pwd
What it does: Shows current working directory  
Syntax: pwd  
Example: pwd  
Useful flags: None  

---

## Command: ls
What it does: Lists files and directories  
Syntax: ls [options] [path]  
Example: ls -la  
Useful flags: -l (long format), -a (hidden files), -h (human readable)  

---

## Command: cd
What it does: Changes directory  
Syntax: cd [path]  
Example: cd /home/user  
Useful flags: .. (go back), ~ (home directory)  

---

## Command: mkdir
What it does: Creates a directory  
Syntax: mkdir [dirname]  
Example: mkdir test  
Useful flags: -p (create nested directories)  

---

## Command: rmdir
What it does: Removes empty directory  
Syntax: rmdir [dirname]  
Example: rmdir test  

---

## Command: rm
What it does: Deletes files/directories  
Syntax: rm [options] [file]  
Example: rm file.txt  
Useful flags: -r (recursive), -f (force)  

---

## Command: cp
What it does: Copies files/directories  
Syntax: cp [source] [destination]  
Example: cp file.txt backup.txt  
Useful flags: -r (recursive copy)  

---

## Command: mv
What it does: Moves or renames files  
Syntax: mv [source] [destination]  
Example: mv file.txt new.txt  

---

## Command: cat
What it does: Displays file content  
Syntax: cat [file]  
Example: cat notes.txt  

---

## Command: less
What it does: Views file page by page  
Syntax: less [file]  
Example: less largefile.txt  

---

## Command: head
What it does: Shows first lines of file  
Syntax: head [file]  
Example: head file.txt  
Useful flags: -n (number of lines)  

---

## Command: tail
What it does: Shows last lines of file  
Syntax: tail [file]  
Example: tail file.txt  
Useful flags: -n, -f (live updates)  

---

## Command: touch
What it does: Creates empty file  
Syntax: touch [filename]  
Example: touch test.txt  

---

## Command: file
What it does: Identifies file type  
Syntax: file [filename]  
Example: file test.txt  

---

## Command: find
What it does: Searches for files  
Syntax: find [path] [condition]  
Example: find . -name file.txt  
Useful flags: -type f, -size, -user  

---

## Command: grep
What it does: Searches text patterns  
Syntax: grep [pattern] [file]  
Example: grep "hello" file.txt  
Useful flags: -i (ignore case), -r (recursive)  

---

## Command: sort
What it does: Sorts lines  
Syntax: sort [file]  
Example: sort data.txt  

---

## Command: uniq
What it does: Removes duplicate lines  
Syntax: uniq [file]  
Example: sort data.txt | uniq  
Useful flags: -u (unique only)  

---

## Command: wc
What it does: Counts lines, words, characters  
Syntax: wc [file]  
Example: wc file.txt  
Useful flags: -l, -w, -c  

---

## Command: chmod
What it does: Changes file permissions  
Syntax: chmod [permissions] [file]  
Example: chmod 755 script.sh  

---

## Command: chown
What it does: Changes file ownership  
Syntax: chown [user]:[group] [file]  
Example: chown user:group file.txt  

---

## Command: ps
What it does: Shows running processes  
Syntax: ps  
Example: ps aux  

---

## Command: top
What it does: Real-time process monitor  
Syntax: top  

---

## Command: kill
What it does: Terminates a process  
Syntax: kill [PID]  
Example: kill 1234  

---

## Command: df
What it does: Shows disk space usage  
Syntax: df  
Example: df -h  

---

## Command: du
What it does: Shows directory size  
Syntax: du [path]  
Example: du -sh .  

---

## Command: echo
What it does: Prints text/output  
Syntax: echo [text]  
Example: echo "Hello"  

---

## Command: man
What it does: Shows manual for commands  
Syntax: man [command]  
Example: man ls  

---

## Command: history
What it does: Shows command history  
Syntax: history  

---

## Command: clear
What it does: Clears terminal screen  
Syntax: clear  

---
