# Bandit Writeup (Level 10 → 20)

---

## Level 10 → 11
Hint: The file content is encoded, not plain text. Try decoding it using common encodings.

Command used: base64 -d data.txt  
Password found: dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr  

What I learned:  
Base64 is a common encoding scheme. The `base64 -d` command decodes encoded data back to readable form.

---

## Level 11 → 12
Hint: Characters are shifted uniformly. Think of simple substitution ciphers.

Command used: tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt  
Password found: 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4  

What I learned:  
ROT13 is a Caesar cipher shifting letters by 13 positions. The `tr` command can map characters to decode it.

---

## Level 12 → 13
Hint: The file is not directly readable. It has been transformed multiple times.

Command used:
xxd -r data.txt > data  
file data  
(Repeated decompression using gunzip, bunzip2, tar -xf)

Password found: FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn  

What I learned:  
This level required a **looped process**:
hexdump → reverse → identify → decompress → repeat  
The `file` command is essential to identify the next format at each step.

---

## Level 13 → 14
Hint: You are given access via a private key instead of a password.

Command used: ssh -i sshkey.private bandit14@localhost -p 2220  
Password found: MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS  

What I learned:  
SSH supports key-based authentication. Permissions must be restricted (`chmod 600`) for the key to work.

---

## Level 14 → 15
Hint: A service is running on a port. You must communicate with it.

Command used: cat /etc/bandit_pass/bandit14 | nc localhost 30000  
Password found: 8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo  

What I learned:  
Netcat (`nc`) allows direct communication with network services. Input can be piped directly into it.

---

## Level 15 → 16
Hint: The service requires secure communication (SSL/TLS).

Command used: cat /etc/bandit_pass/bandit15 | openssl s_client -quiet -connect localhost:30001  
Password found: kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx  

What I learned:  
Some services require encrypted connections. `openssl s_client` enables SSL/TLS communication.

---

## Level 16 → 17
Hint: Multiple ports exist. Only one gives a meaningful response.

Command used:
nmap -p 31000-32000 -sV localhost  
openssl s_client -quiet -connect localhost:31790  

Password found: (RSA Private Key)

What I learned:  
- Port scanning helps discover active services  
- Not all services behave the same (echo vs real service)  
- SSL services require proper tools to interact  

---

## Level 17 → 18
Hint: Compare two files and find the difference.

Command used: diff passwords.old passwords.new  
Password found: x2gLTTjFwMOhQ8oWNbmN362QKxfRqGlO  

What I learned:  
The `diff` command highlights differences between files. The changed line reveals the password.

---

## Level 18 → 19
Hint: Login shell is restricted. Execute a command directly during SSH.

Command used: ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"  
Password found: cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8  

What I learned:  
SSH can execute commands directly without opening an interactive shell, bypassing restrictions.

---

## Level 19 → 20
Hint: A special binary runs with elevated privileges.

Command used: ./bandit20-do cat /etc/bandit_pass/bandit20  
Password found: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO  

What I learned:  
Setuid binaries execute with the owner's permissions. They can be used to access restricted files.

---
