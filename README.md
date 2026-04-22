# Zabbix → MAX Alertscripts

Simple Python scripts to send Zabbix alerts to MAX (https://max.ru) via HTTP API.

Useful in environments where Telegram or other messaging platforms are restricted or unavailable.

---

##  Quick Start

1. Place scripts into /usr/lib/zabbix/alertscripts
2. Set MAX_BOT_TOKEN
3. Get chat_id using get_user_id.py
4. Configure Media type in Zabbix

---

##  Requirements

- Python 3.6+
- requests

Install dependencies:

bash pip install -r requirements.txt 

---

##  Installation

Copy scripts to:

bash /usr/lib/zabbix/alertscripts 

Make them executable:

bash chmod +x /usr/lib/zabbix/alertscripts/*.py 

---

##  Token Configuration

Set your bot token via environment variable MAX_BOT_TOKEN.

Example for systemd:

ini [Service] Environment="MAX_BOT_TOKEN=YOUR_TOKEN" 

Apply changes:

bash sudo systemctl daemon-reexec sudo systemctl daemon-reload sudo systemctl restart zabbix-server 

Verify:

bash sudo systemctl show zabbix-server --property=Environment 

---

##  Get chat_id

Run:

bash export MAX_BOT_TOKEN=YOUR_TOKEN ./get_user_id.py 

The script will return JSON with updates. Find your chat_id there.

---

##  Zabbix Configuration

1. Go to:
      Administration → Media types   

2. Create new Media type:
   - Type: Script
   - Script name: zabbix_max_http.py

3. Parameters:
      {ALERT.SENDTO}    {ALERT.SUBJECT}    {ALERT.MESSAGE}   

---

##  User Setup

1. Go to:
      Administration → Users   

2. Add Media:
   - Type: MAX (created above)
   - Send to: chat_id

---

##  Manual Test

bash export MAX_BOT_TOKEN=YOUR_TOKEN  ./zabbix_max_http.py 123456789 "Test subject" "Test message" 

---

##  Common Errors

- MAX_BOT_TOKEN is not set  
  → token is not configured

- chat_id must be integer  
  → invalid format

- MAX API error ...  
  → API returned an error

---

##  Notes

- Uses MAX HTTP API
- No Telegram dependency
- Designed for restricted environments
