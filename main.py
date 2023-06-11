import requests
import argparse

open_domains = []

parser = argparse.ArgumentParser()
parser.add_argument('--url',type=str,required=True)
args = parser.parse_args()


file = open('list.txt')
file = file.read()
lines = file.splitlines()


for subdomain in lines:
	url = f"https://{subdomain}.{args.url}"
	try:
		requests.get(url)
	except requests.ConnectionError:
		pass
	else:
		print("[+] open domain: ",url)
		write_domen = open(f"data/{args.url}.txt",'a')
		write_domen.write(f"{url} \n")
		write_domen.close()
		open_domains.append(url)