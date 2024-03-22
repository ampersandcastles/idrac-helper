import subprocess

# Server IPMI details
IPMIHOST = "192.168.1.223"
IPMIUSER = "root"
IPMIPASS = "<password>"

def execute_ipmi_command(command):
    full_command = f"ipmitool -I lanplus -H {IPMIHOST} -U {IPMIUSER} -P {IPMIPASS} {command}"
    print(f"Executing command: {full_command}")  # Print the full command to debug
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
