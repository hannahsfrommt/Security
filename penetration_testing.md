HAST-006-M  
97dGQEcQWgSxAzo  
base64 and rot13 encoding throughout this module  
linux - 10.50.31.3  
windows - 10.50.44.112  

grey host - 10.50.36.239
un: student pw: 97..
where we are tunnelling through
setting up master socket
```student@lin-ops:~/Desktop/Security$ ssh -MS /tmp/gray student@10.50.36.239```
  
  

# pen testing
phase1 - mission definition
phase2 - recon
phase3 - footprinting
phase4 - exploitation and initial access
phase5 - post-exploitation
phase6 - document mission


## write a formal report
use op notes and maps and save passwords
- executive summary
- technical summary
## create a report for reasons...
- continuity of operations
- accounting of actions taken
- ability to repeat exact actions
- troubleshooting and lessons learned

# Scanning and Reconnaissance
Open Source Intelligence (OSINT)
## collection and use
### web data colletion
cached content, analytics, proxy web application, command lineinterrogation
*methods: urpsuite, oswap zap, theharvester*
### social media collection
twitter, facebook, instagram, people searches , registry and wish lists 
*methods: family trees, birth/death records, content analysis, graphic searches, open api's*
### sensitive data collection
business data, profiles, non-profits/charities, business filings, historical and public listings
*methods: google maps, job postings, company public websites/portals*
### publicly accessible data
physical addresses, phone numbers, email addresses, user name, search engine data, web and trafic cameras, wireless access point data
*methods: reverse lookup, newsletters, real estate data, standardized email formatting , google dorks*
### domain and ip address data collection
dns registration, ip address assignments, geolocation data, whois
*methods: whois , traceroute, web registrars*
  
can use it to: technical analysis/exploitations, phishing campaigns, attacking web portals, test common credentials, enumerate public facing targets  

## Hyper-Text Markup Language (HTML)
Standardized markup language for browser interpretation of webpages
- Client-side interpretation (web browser)
- Utilizes elements (identified by tags)
- Typically redirects to another page for server-side interaction
- Cascading Stylesheets (CSS) for page themeing


## Network Recon
1. host discovery
  -  Ping Sweep
      - Sends one icmp echo request packet to each host on the ```192.168.1.0/24```
      - Linux: ```for i in {1..254} ;do (ping -c 1 192.168.1.$i | grep "bytes from" &) ;done```
      - Windows: ```for /L %i in (1,1,255) do @ping -n 1 -w 200 192.168.1.%i > nul && echo 192.168.1.%i is up.```
2. Port enumeration
- Use nmap to scan a range and specific ports on a discovered machine:
- ```nmap -sS -Pn 8.8.8.8 -p 135-139,22,80,443,21,8080```
- Use nc to scan a range and specific ports on a discovered machine:
- ```nc -z -v -w 1 8.8.8.8 440-443```
3. Port interrogation
  - Use nc to interrogate a web server:
      - ```nc -Cv 127.0.0.1 80```
      - Type: GET / HTTP/1.0 to get a HTTP Response header from the server.
  - Use nmap to perform service detection on port 22 of your opstation:
      - ```nmap -sV 127.0.0.1 -p 22```
  - Using nikto to perform a vulnerability scan on your opstation:
      - ```nikto -h 127.0.0.1 -p 80```
      - Also shows other information like what HTTP methods are allowed and various CVE vulnerabilities.

   
## NMAP Scripting Engine
- benefits of scanning w scripts
- script management and utilization
- usage and examples
## script management
/usr/share/nmap/scripts
## usage and examples
```
nmap --script <filename>|<category>|<directory>
nmap --script-help "ftp-* and discovery"
nmap --script-args <args>
nmap --script-args-file <filename>
nmap --script-help <filename>|<category>|<directory>
nmap --script-trace
```



demo 

```
student@lin-ops:~/Desktop/Security$ ssh -MS /tmp/gray student@10.50.36.239
student@lin-ops:~/Desktop/Security$ ssh -S /tmp/gray gray -O forward -D9050
student@jump:~$ for i in {1..254} ;do (ping -c 1 192.168.28.$i | grep "bytes from" &) ;done
192.168.28.1,.2,.3,.97,.98,.99,.100,.105,.111,.120,.129,.130,.131
student@lin-ops:~/Desktop/Security$ proxychains nmap -v -sT -Pn -T4 -sV 192.168.28.129,130,131,111,105
student@lin-ops:~/Desktop/Security$ ssh -S /tmp/gray gray -O forward -L 1440:192.168.28.111:80
student@lin-ops:~/Desktop/Security$ firefox
student@lin-ops:~/Desktop/Security$ ssh -S /tmp/gray gray -O forward -L 1550:192.168.28.111:22

student@lin-ops:~/Desktop/Security$ ssh -MS /tmp/billybobhost billybob@0.0.0.0 -p 1550
student@lin-ops:~/Desktop/Security$ ssh -S /tmp/billybobhost -O forward -D9050
```
* to cancel tunnel replace the "forward" with "cancel" *












