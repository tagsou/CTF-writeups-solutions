import requests
import gzip

url = "https://inst-6ead480c13c5fb46-proxies.chal.crewc.tf/"


r = requests.post(url+"/aaaa",data=gzip.compress(b"GIVE ME FLAG!"),headers={"Content-Encoding":"gzip"})

print(r.text)