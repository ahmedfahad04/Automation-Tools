import json
import subprocess

# Run the command and capture the output
output = subprocess.check_output(["netstat -n | awk '{print($5)}' | grep ':[0-9]\+' | grep -v '127.0.0.1\|0.0.0.0'"], shell=True)

# Decode the output to a string (if needed)
output_str = output.decode("utf-8")

# open file to save the output
fp = open('network_traffic.csv', 'w+')
fp.writelines('IP,Service,Area,Country\n')

# Print or use the output as needed
for ip in output_str.split('\n'):
    new_ip = ip.split(':')[0]
    cmd = f'curl ipinfo.io/{new_ip}'
    response = subprocess.check_output([cmd], shell=True)
    response_str = response.decode('utf-8')
    data = json.loads(response_str)
    
    try:
        print('IP: ', data['ip'], 'Area: ', data['timezone'], 'Country: ', data['country'])
        fp.writelines(f"{data['ip']},{data['org'].replace(',', '_')},{data['timezone'].replace(',', '_')},{data['country'].replace(',', '_')}\n")

    except:
        pass