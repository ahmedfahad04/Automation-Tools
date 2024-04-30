import subprocess 

output = subprocess.check_output(["journalctl | grep -i 'authentication failure' | awk '{print($2-$6)}'"], shell=True)
output_str = output.decode('utf-8')
print(output_str)