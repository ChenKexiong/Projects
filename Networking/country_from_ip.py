#input: ip
#output: country of the ip
import json
import requests
# An open API
country_path = 'http://api.ipinfodb.com/v3/ip-country/?key=5d3d0cdbc95df34b9db4a7b4fb754e738bce4ac914ca8909ace8d3ece39cee3b&ip%s'
def load_ips():
    with open("ips.json",'r') as f:
        ips = json.load(f)
    return ips
def lookup_ips(ips):
    results = {}
    for ip in ips:
        r = requests.get(country_path % ips[ip])
        if r.status_code == 200:
            sp = r.text.split(";")
            results[ip] = sp[-1]
    return results
if __name__ == '__main__':
    #test = {"dsg":234,"dsjg":34}
    #with open("test.json",'w') as f:
     #   json.dump(test,f)
    ips = load_ips()
    rs = lookup_ips(ips)
    print rs
