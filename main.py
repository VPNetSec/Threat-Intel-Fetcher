import os
import csv
import time
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('ABUSEIPDB_API_KEY')
url = 'https://api.abuseipdb.com/api/v2/check'
headers = {'Accept': 'application/json', 'Key': API_KEY}

def check_ip(ip):
    params = {'ipAddress': ip, 'maxAgeInDays': '90'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['data']
    return None

# Read IPs from the text file
with open('targets.txt', 'r') as file:
    ips = [line.strip() for line in file if line.strip()]

csv_filename = "threat_report.csv"

# Open CSV for writing
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["IP Address", "Abuse Score", "ISP", "Domain", "Total Reports"])
    
    print("\n--- Bulk Threat Intelligence Scanning ---")
    for ip in ips:
        print(f"[*] Analyzing {ip}...")
        data = check_ip(ip)
        
        if data:
            writer.writerow([
                data.get('ipAddress'), 
                data.get('abuseConfidenceScore'), 
                data.get('isp'), 
                data.get('domain'), 
                data.get('totalReports')
            ])
        else:
            print(f"[-] Failed to retrieve data for {ip}")
            
        time.sleep(1) # Pause for 1 second between requests to respect API rate limits
        
print(f"\n[+] Scan complete. Bulk data exported to {csv_filename}")