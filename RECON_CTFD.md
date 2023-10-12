>Jump Box
->Network scan: 192.168.28.96/27
-->Network scan:192.168.150.224/27

Target Section:

Network scans:
Network: 192.168.28.96/27
Network:192.168.150.224/27
OSs: unknown
Creds: student ::
Known Ports: unknown
Known URL: consulting.site.donovia
Known URL: conference.site.donovia
Action: Reconnaissance to collect intelligence and identify possible avenues of approach in the network.


student@lin-ops:~/Desktop/Security$ ssh -MS /tmp/gray student@10.50.36.239
student@lin-ops:~/Desktop/Security$ ssh -S /tmp/gray gray -O forward -D9050
student@jump:~$ for i in {1..254} ;do (ping -c 1 192.168.28.$i | grep "bytes from" &) ;done
192.168.28.1,.2,.3,.97,.98,.99,.100,.105,.111,.120,.129,.130,.131
student@lin-ops:~/Desktop/Security$ proxychains nmap -v -sT -Pn -T4 -sV 192.168.28.129,130,131,111,105

192.168.150.X  
.225, .226, .227  
.226 and .227 have dns 53 open  

192.168.28.X  
.97, .98, .99, .100, .105, .111, .120  
.98 has 53  
.100 has 80, 2222 as ssh  
.105 has 21,23,2222 as ssh  
.111 has 80, 2222 as105 ssh and 8080 as http  
.120 has 4242 as ssh  

File Transfer Protocol (FTP) appears to be available within Donovian Cyberspace, perform further reconnaissance and interrogate this service to identify the flag.
student@lin-ops:~$ proxychains wget -r FTP://192.168.28.105

Intelligence shows that the Donovian Government is preparing for a conference, you have been tasked to collect all information relating to the speakers.
Identify the key individual to find the flag
student@lin-ops:~$ ssh -S /tmp/gray gray -O forward -L 1441:192.168.28.111:8080
firefox
0.0.0.0:1461
F12
look through web site 
ctrl+f strong on articles page and look for Armstrong 
also on contact page ctrl+f for strong and piece together the flag
