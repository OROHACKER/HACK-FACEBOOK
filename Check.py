<p align="center"><img src="https://github.com/thehackingsage/hacktonian/blob/master/logo.png?raw=true" /></p>
<p align="center"><a href="https://tracking.gitads.io/?repo=hacktronian"><img src="https://images.gitads.io/hacktronian" alt="GitAds"/></a></p>
<p align="center">***Pentesing Tools That All Hacker Needs.***</p>

## OROHACKER Menu :

- Information Gathering
- Password Attacks
- Wireless Testing
- Exploitation Tools
- Sniffing & Spoofing
- Web Hacking
- Private Web Hacking
- Post Exploitation
- Install The HACKTRONIAN

### Information Gathering:

- Nmap
- Setoolkit
- Port Scanning
- Host To IP
- wordpress user
- CMS scanner
- XSStrike
- Dork - Google Dorks Passive Vulnerability Auditor
- Scan A server's Users
- Crips

### Password Attacks:

- Cupp
- Ncrack

### Wireless Testing:

- reaver
- pixiewps
- Fluxion

### Exploitation Tools:

- ATSCAN
- sqlmap
- Shellnoob
- commix
- FTP Auto Bypass
- jboss-autopwn

### Sniffing & Spoofing:

- Setoolkit
- SSLtrip
- pyPISHER
- SMTP Mailer

### Web Hacking:

- Drupal Hacking
- Inurlbr
- Wordpress & Joomla Scanner
- Gravity Form Scanner
- File Upload Checker
- Wordpress Exploit Scanner
- Wordpress Plugins Scanner
- Shell and Directory Finder
- Joomla! 1.5 - 3.4.5 remote code execution
- Vbulletin 5.X remote code execution
- BruteX - Automatically brute force all services running on a target
- Arachni - Web Application Security Scanner Framework

### Private Web Hacking:

- Get all websites
- Get joomla websites
- Get wordpress websites
- Control Panel Finder
- Zip Files Finder
- Upload File Finder
- Get server users
- SQli Scanner
- Ports Scan (range of ports)
- ports Scan (common ports)
- Get server Info
- Bypass Cloudflare

### Post Exploitation:

- Shell Checker
- POET
- Weeman

## Installation in Linux :

This Tool Must Run As ROOT !!!

```git clone https://github.com/thehackingsage/hacktronian.git```

```cd hacktronian```

```chmod +x install.sh```

```./install.sh```

That's it.. you can execute tool by typing **hacktronian**

## Installation in Android :

Open [Termux](https://play.google.com/store/apps/details?id=com.termux)

```pkg install git```

```pkg install python```

```git clone https://github.com/thehackingsage/hacktronian.git```

```cd hacktronian```

```chmod +x hacktronian.py```

```python2 hacktronian.py```

## Video Tutorial : 

YouTube : https://www.youtube.com/watch?v=1LJlyQAQby4

## License :

[MIT Licence](https://github.com/thehackingsage/hacktronian/blob/master/LICENSE)

That's It... If You Like This Repo. Please Share This With Your Friends..

& Don't Forget To Follow Me At [Twitter](https://www.twitter.com/thehackingsage), [Instagram](https://www.instagram.com/thehackingsage), [Github](https://www.github.com/thehackingsage) & SUBSCRIBE My [YouTube](https://www.youtube.com/channel/UCYK1n9A4TUq1CvGc6F3DzoA) Channel..!!!

***Thankyou.***
***Keep Visiting..***
***Enjoy.!!! :)***

import requests
import json

USER_TOKEN = "" #Fill your fb user token (open https://facebook.com/me, ctrl +u and copy access token
SHIELD_ENABLE = "true" #Change to false if turn off shield



def get_userid(token):
	url = "https://graph.facebook.com/me?access_token=%s" % token
	res = requests.get(url)
	info = json.loads(res.text)
	return info["id"]

def turn_shield(token, enable = True):
	uid = get_userid(token)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(uid))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % token}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)

turn_shield(USER_TOKEN, SHIELD_ENABLE)
