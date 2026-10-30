# Threat-Intel-Fetcher

A Python-based security automation tool designed to streamline Security Operations Center (SOC) workflows by automating threat intelligence gathering and reporting.

## Overview
Manual IP reputation checking is time-consuming during incident response. This utility integrates with the AbuseIPDB API to ingest suspicious IP addresses in bulk, parse complex JSON threat data, and automatically generate clean, actionable reports for security analysts. 

## Features
* **Bulk Processing:** Reads target IP addresses from a local text file for mass analysis.
* **Data Parsing:** Extracts critical threat metrics including Abuse Confidence Score, ISP, and Total Reports.
* **Automated Reporting:** Outputs normalized findings into a cleanly formatted `threat_report.csv`.
* **Rate Limiting:** Built-in execution delays to respect API rate limit thresholds.
* **Operational Security:** Utilizes environment variables (`.env`) to prevent credential leakage.

## Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/VPNetSec/Threat-Intel-Fetcher.git](https://github.com/VPNetSec/Threat-Intel-Fetcher.git)


2. Install the required dependencies:
```bash
pip install requests python-dotenv

```

3. Create a `.env` file in the root directory and add your API key:
```text
ABUSEIPDB_API_KEY=your_actual_api_key_here

```


4. Add target IP addresses to `targets.txt` (one per line).

## Usage

Execute the primary script from your terminal:

```bash
python main.py

```

*The script will output progress to the console and generate a `threat_report.csv` file in the same directory.*
