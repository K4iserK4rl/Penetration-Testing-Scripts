import requests
import sys

subList = open("subdomains.txt").read().splitlines()

for sub in subList:
    subDomains = f"http://{sub}.{sys.argv[1]}"

    try:
        requests.get(subDomains)
    except requests.ConnectionError:
        pass
    #else:
    print("Valid Domain: ", subDomains) 
        
exit(0)
