### TLTR;
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level02
level02@192.168.1.64's password: f2av5il02puano7naaf6adaaf
level02@SnowCrash:~$ su flag02
Password: ft_waNDReL0L
Don't forget to launch getflag !
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
```
***
Login as `level02`.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ssh 192.168.1.64 -p 4242 -l level02
level02@192.168.1.64's password: f2av5il02puano7naaf6adaaf
```
A `.pcap` file is located in home directory.
Pcap files are data files containing the packet data of a network.
```shell
level02@SnowCrash:~$ ls -l
total 12
----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap
```
Copy `level02.pcap` file from VM on local to further processing.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  scp -P 4242 level02@192.168.1.64:~/level02.pcap  .
level02@192.168.1.64's password: f2av5il02puano7naaf6adaaf
level02.pcap                 100% 8302    10.4MB/s   00:00
```
Copied file `level02.pcap` is not readable. So change file modes by setting on read bits.
```shell
┌──$ [~/42/2021/snow-crash]
└─>  ls -l level02.pcap
----r--r--  1 aslan  staff  8302 Jan 28 08:11 level02.pcap 
┌──$ [~/42/2021/snow-crash]
└─>  chmod +r level02.pcap
```
Open `level02.pcap` with Wireshark and follow TCP Stream from packet `#43`.

At the first glance, it seems that the password is `ft_wandr...NDRel.L0L`. But it does not allow to log into `flag02`.

Swith view mode to show data as Hex Dump.
```
Packet	  Hexadecimal					     ASCII
000000D6  00 0d 0a 50 61 73 73 77  6f 72 64 3a 20            ...Passw ord: 
000000B9  66                                                 f
000000BA  74                                                 t
000000BB  5f                                                 _
000000BC  77                                                 w
000000BD  61                                                 a
000000BE  6e                                                 n
000000BF  64                                                 d
000000C0  72                                                 r
000000C1  7f                                                 .
000000C2  7f                                                 .
000000C3  7f                                                 .
000000C4  4e                                                 N
000000C5  44                                                 D
000000C6  52                                                 R
000000C7  65                                                 e
000000C8  6c                                                 l
000000C9  7f                                                 .
000000CA  4c                                                 L
000000CB  30                                                 0
000000CC  4c                                                 L
000000CD  0d                                                 .
```

By corresponding ASCII characters to its hexadecimal representation, it reveals that besides the printable characters there is control characters.
> _"The stream content is displayed in the same sequence as it appeared on the network. Non-printable characters are replaced by dots."_ [¹](https://www.wireshark.org/docs/wsug_html_chunked/ChAdvFollowStreamSection.html)

Code `7f` corresponds to the non-printable "delete" `DEL` control character.
So removing all character followed by dot gives:

```ft_wandr...NDRel.L0L  --->   ft_waNDReL0L```

Login as `flag02` and get the flag.
```shell
level02@SnowCrash:~$ su flag02
Password: ft_waNDReL0L
Don't forget to launch getflag !
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
```
