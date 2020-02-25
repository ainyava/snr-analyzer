import csv
import os
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# INFO
AUTH = ('admin', '1234')
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.csv')

# Get data from router
r = requests.get('http://192.168.1.1/statsifcwan.html', auth=AUTH)
if r.status_code != 200:
    sys.exit('erorr')

# Select LineRate, SNR, Attenuation from data
s = BeautifulSoup(r.content, 'html.parser')
trs = s.find_all('table', {'class': 'formlisting'})[2].find_all('tr')
rate = trs[5].find_all('td')
snr = trs[7].find_all('td')
atn = trs[8].find_all('td')

# Format data
t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
row = [rate[1].string.strip(), rate[2].string.strip(), snr[1].string.strip(), snr[2].string.strip(),
       atn[1].string.strip(), atn[2].string.strip(), t]

# Read data file
with open(DATA_FILE, 'r') as csv_file:
    old_data = list(csv.reader(csv_file))

try:
    diff = abs(float(old_data[-1][2]) - float(row[2]))
except ValueError:
    diff = 0
    if snr[1] == 'N/A':
        diff = 2
        row = [0, 0, 0, 0, 0, 0, t]

if diff > 1:
    old_data.append(row)

with open(DATA_FILE, 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(old_data)
