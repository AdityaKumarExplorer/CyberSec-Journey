Level 0:
command: ssh -p 2220 bandit0@bandit.labs.overthewire.org
password: bandit0
What I learned: How to connect to a remote server using SSH

----
# Bandit Writeup (Level 0 → 10)

## Level 0 → 1
Command used: ssh bandit0@bandit.labs.overthewire.org -p 2220  
Password found: ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
What I learned: How to connect to a remote server using SSH  

---

## Level 1 → 2
Command used: cat ./-  
Password found: 263JGJPfgU6LtdEvgfWU1XP5yac29Fx  
What I learned: Handling special filenames like '-' using ./  

---

## Level 2 → 3
Command used: cat "spaces in this filename"  
Password found: MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx  
What I learned: Handling spaces in filenames using quotes  

---

## Level 3 → 4
Command used: ls -a, cat inhere/"...Hiding-From-You"  
Password found: 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
What I learned: Hidden files start with '.' and require -a to view  

---

## Level 4 → 5
Command used: cat ./inhere/-file07  
Password found: 4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw  
What I learned: Identifying file types using 'file' command  

---

## Level 5 → 6
Command used: find . -type f -size 1033c ! -executable  
Password found: HWasnPhtq9AVe0dmk45nxy20cvUa6EG
What I learned: Using find with filters (size, type, permissions)  

---

## Level 6 → 7
Command used: find / -user bandit7 -group bandit6 -size 33c 2>/dev/null  
Password found: morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj  
What I learned: Searching entire system and suppressing errors  

---

## Level 7 → 8
Command used: grep "millionth" data.txt  
Password found: dfwvzFQi4mu0wfNbFOE9RoWskMLg7eEc
What I learned: Searching inside files using grep  

---

## Level 8 → 9
Command used: sort data.txt | uniq -u  
Password found: 4CKMh1JI9bUIZZPXDqGanal4xvAg0JM 
What I learned: Finding unique lines using sort + uniq  

---

## Level 9 → 10
Command used: strings data.txt | grep "="  
Password found: FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey  
What I learned: Extracting readable text from binary files  

---

## Level 10 → 11
Command used: base64 -d data.txt  
Password found: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
What I learned: Decoding base64 encoded data  
