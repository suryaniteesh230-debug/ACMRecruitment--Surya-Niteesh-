**KEYS AND COMMANDS**
ssh bandit0@bandit.labs.overthewire.org -p 2220
level 0-bandit0

level(0-1)-ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
ssh bandit0@bandit.labs.overthewire.org -p 2220
ls
cat readme


level(1-2)-263JGJPfgU6LtdEvgfWU1XP5yac29mFx
ssh bandit1@bandit.labs.overthewire.org -p 2220
ls
cat ./-


level(2-3)-MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
ssh bandit2@bandit.labs.overthewire.org -p 2220
ls
cat "spaces in this filename"


level(3-4)-2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
ssh bandit3@bandit.labs.overthewire.org -p 2220
ls -a inhere
cat inhere/.hidden


level(4-5)-4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
ssh bandit4@bandit.labs.overthewire.org -p 2220
ls inhere
file inhere/*
cat inhere/-file07


level(5-6)-HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
ssh bandit5@bandit.labs.overthewire.org -p 2220
find inhere/ -type f -size 1033c ! -executable
cat inhere/maybehere07/.file2


level(6-7)-morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
ssh bandit6@bandit.labs.overthewire.org -p 2220
find / -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password


level(7-8)-dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
ssh bandit7@bandit.labs.overthewire.org -p 2220
grep millionth data.txt


level(8-9)-4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
ssh bandit8@bandit.labs.overthewire.org -p 2220
sort data.txt | uniq -u


level(9-10)-FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
ssh bandit9@bandit.labs.overthewire.org -p 2220
strings data.txt | grep =


level(10-11)-dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
ssh bandit10@bandit.labs.overthewire.org -p 2220
cat data.txt
base64 -d data.txt


