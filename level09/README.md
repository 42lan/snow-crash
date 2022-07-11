Login as `level09`.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level09
level09@192.168.1.64's password: 25749xKZ8L7DkSCwJkT9dyv6f
```
An `SUID` executable and token file are located in home directory.
```shell
level09@SnowCrash:~$ ls -l
total 12
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token
level09@SnowCrash:~$ ./level09
You need to provied only one arg.
level09@SnowCrash:~$ ./level09 token
tpmhr
level09@SnowCrash:~$ cat token
f4kmm6p|=�p�n��DB�Du{��
```
Seems that token file has non `ASCII` characters.
```shell
level09@SnowCrash:~$ xxd token
0000000: 6634 6b6d 6d36 707c 3d82 7f70 826e 8382  f4kmm6p|=..p.n..
0000010: 4442 8344 757b 7f8c 890a                 DB.Du{....
```
Regarding the output it seems that index position is added to each character which gives following output.
```shell
level09@SnowCrash:~$ ./level09 "0123456789"
02468:<>@B
level09@SnowCrash:~$ ./level09 "abcdefghij"
acegikmoqs
```
Use `ltrace` to intercept dynamic library calls and system calls executed by the program.
```gdb
level09@SnowCrash:~$ ltrace ./level09 "abcdefghij"
__libc_start_main(0x80487ce, 2, 0xbffff7d4, 0x8048aa0, 0x8048b10 <unfinished ...>
ptrace(0, 0, 1, 0, 0xb7e2fe38) = -1
puts("You should not reverse this"You should not reverse this) = 28
+++ exited (status 1) +++
```
_"You should not reverse this"_ - gives idea that output can be reversed.

Write a Python script which will subtract index position from each character.
```python
level09@SnowCrash:~$ vi /tmp/reverse.py
#!/usr/bin/python
import sys
i = -1
content = open("/home/user/level09/token").readlines()[0]
for c in content:
   i += 1
     try:
        sys.stdout.write(chr(ord(c) - i))
     except:
        pass
print "\n",
```
Change file modes by setting on execute bits.
```shell
level09@SnowCrash:~$ chmod +x /tmp/reverse.py
level09@SnowCrash:~$ /tmp/reverse.py
f3iji1ju5yuevaus41q1afiuq
```
Login as `flag09` and get the flag.
```shell
level09@SnowCrash:~$ su flag09
Password: f3iji1ju5yuevaus41q1afiuq
Don't forget to launch getflag !
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```
