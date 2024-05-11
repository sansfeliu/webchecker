#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script: webchecker.py
# Author: Albert Sans i Feliu
# Description: This Python script checks the availability of ports 80 and 443 for the URLs provided in an input file and saves the results to a CSV file. Provides a basic alternative to using the Nmap command for port scanning (nmap -iL urls.txt -p 80,443 -oA scan_results)
# Usage: python webchecker.py urls_file output_file


import csv
import socket
import sys
import os

def resolve_hostname(url):
    try:
        ip = socket.gethostbyname(url)
        return ip
    except socket.gaierror:
        return None

def check_port(ip, url):
    results = []
    if ip:
        for port in [80, 443]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)  # Adjust the timeout as needed
            result = "Yes" if sock.connect_ex((ip, port)) == 0 else "No"
            results.append((url, ip, port, result))
            sock.close()
    else:
        print(f"Error: Could not resolve hostname to IP for URL: {url}")
    return results

def main(input_file, output_file):
    with open(input_file, 'r') as urls_file:
        # Add the .csv extension to the output file
        output_file += '.csv'
        
        with open(output_file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['URL', 'IP', 'Port', 'Active'])

            for url in urls_file:
                url = url.strip()  # Remove leading/trailing whitespace
                if url:
                    ip = resolve_hostname(url)
                    results = check_port(ip, url)
                    csv_writer.writerows(results)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python webchecker.py urls_file output_file")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)

