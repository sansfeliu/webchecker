# Web Checker Script

## Description
This Python script checks the availability of ports 80 and 443 for the URLs provided in an input file and saves the results to a CSV file.
Provides a basic alternative to using the Nmap command for port scanning (nmap -iL urls.txt -p 80,443 -oA scan_results)

## Usage 
python webchecker.py urls_file output_file
