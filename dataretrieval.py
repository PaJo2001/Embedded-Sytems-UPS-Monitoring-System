import requests

#payload = {'Host': 'in.provider.com:8080', 'X-M2M-Origin': '/in-cse/cnt-946185962', 'X-M2M-RI': 'incse-55667', 'Accept': 'application/json'}
r = requests.get('http://139.59.42.21:8080/~/in-cse/in-name/Team43_UPS_performance_monitoring/pr_5_esp32_1/em/em_1_vll_avg/la)

print(r.url)
print(r.text)