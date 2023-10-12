# Recon

## Web Scraping
see web scraper on fg if want to use to grab for example mulitple authors or quotes
## host discovery
ping sweep
Linux: `for i in {1..254} ;do (ping -c 1 192.168.1.$i | grep "bytes from" &) ;done`
do this first before nmap if scanning a whole network to limit the number of ips have to nmap
## port enumeration
to scan to se what ports are open on machine or multiple machines
`nmap -sS -Pn 8.8.8.8 -p 135-139,22,80,443,21,8080`
## port interrogation
`nc -Cv 127.0.0.1 80`
`nmap -sV 127.0.0.1 -p 22`
`nikto -h 127.0.0.1 -p 80`
## nmap scripts 
scripts can be found in `/usr/share/nmap/scripts` , use `grep` to search for specific name
`nmap --script http-enum <IP Address>`
`nmap -p 445 --script smb-os-discovery <IP Address / Subnet>`


# Web Exploitation DAY 1




# Web Exploitation DAY 2

# Reverse Engineering

## Registers
look to see different registers and their bits 
understand the directions in c code to be able to find answers
as well as python programming
will walk through steps of behavioral, dynamic analysis and disassembly
GHIDRA resource on windows

# Exploit Development Testing

## Buffer Overflow
look at fg, notes, and use scripts to do these things

# Post Exploitation

## stealing ssh identity keys
after stealing the key 
`chmod 600 /home/user/stolenkey`
`ssh -i /home/user/stolenkey jane@10.20.30.40`
## control sockets
pretty good with these
remember to make a master socket when want to actually travel through a new box 
## scp 
look at commands here for examples or notes whooohooo
[put a few examples we have used in class here]
## enumertion
look on this page in fg for numerous commands for both linux and windows for enumeration such as : user, process, service, network, etc.

# Windows Exploitation

# Linux Exploitation
