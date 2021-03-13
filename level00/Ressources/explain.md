### TLTR;
```shell
┌──$ [~/42/2020/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level00
level00@192.168.1.64's password: level00
level00@SnowCrash:~$ alias rot11="tr A-Za-z L-ZA-Kl-za-k"
level00@SnowCrash:~$ cat /usr/sbin/john | rot11
nottoohardhere
level00@SnowCrash:~$ su flag00
Password: nottoohardhere
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```

***

Login as `level00`.
```shell
┌──$ [~/42/2020/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level00
level00@192.168.1.64's password: level00
```

There is no file or binary to exploit in home directory.
```shell
level00@SnowCrash:~$ ls -l
total 0
```

But in the introduction video wandre gives a clu:
> "FIND this first file who can run only as flag00..."

So, search for files owned by `flag00` and redirect stderr to the black hole.
```shell
level00@SnowCrash:~$ find / -user flag00 -exec ls -l {} \; 2>/dev/null
----r--r-- 1 flag00 flag00 15 Mar  5  2016 /usr/sbin/john
----r--r-- 1 flag00 flag00 15 Mar  5  2016 /rofs/usr/sbin/john
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
```
Looks like that string is encrypted.
Rotate text by replacing current `char` to `char + 11` (ROT11).
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
LMNOPQRSTUVWXYZABCDEFGHIJK
```
```shell
level00@SnowCrash:~$ alias rot11="tr A-Za-z L-ZA-Kl-za-k"
level00@SnowCrash:~$ cat /usr/sbin/john | rot11
nottoohardhere
```
Login as `flag00` and get the flag.
```shell
level00@SnowCrash:~$ su flag00
Password: nottoohardhere
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```
