"""
Pass a list of IP addresses that need to be resolved. Outputs a lists of the
domains associated with the IP. Any address that does not resolve will be listed
at the end of the output file.

Replace the file paths to match your desired input/output.
"""

import socket

with open(r"C:\Users\useraccount\Desktop\suspiciousIP.txt", "r") as input:
    ptr_lookup = []
    ip_address = input.readlines()
    converted_list = [] #Remove unwanted characters from original list
    error_log = [] #Log the IP addresses that did not return a domain 
    
    for item in ip_address:
        converted_list.append(item.strip())
    
    for i in converted_list:
        try:
            ptr_lookup.append(socket.gethostbyaddr(i)) 
        except socket.herror:
            error_log.append(f"Error, the IP address {i} did not resolve to a domain")
   
    with open(r"C:\Users\useraccount\Desktop\resolvedIP.txt", "w+") as output:
        for item in ptr_lookup:
            line = " ".join(str(x) for x in item)
            output.write(line + "\n")
        
        for i in range(len(error_log)):
            output.write(error_log[i] + "\n")
