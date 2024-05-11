# Web Checker Script

## Description
This script checks the availability of ports 80 and 443 for the URLs provided in an input file and saves the results to a CSV file.
Provides a python alternative to using the Nmap command for port scanning (nmap -iL urls.txt -p 80,443 -oA scan_results)

## Usage 
python webchecker.py urls_file output_file

## Example URLs File
The input file should contain one URL per line, such as:

https://example1.com
https://example2.com

## Results
The script will generate a CSV file with the results of checking the availability of ports 80 and 443 for each provided URL.

The format of the CSV file is as follows:

URL,IP,Port,Active
https://example1.com,192.168.1.1,80,Yes
https://example1.com,192.168.1.1,443,Yes
https://example2.com,192.168.1.2,80,No
https://example2.com,192.168.1.2,443,Yes
