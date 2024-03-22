import argparse
import subprocess

# Server IPMI details
IPMIHOST = "192.168.1.223"
IPMIUSER = "root"
IPMIPASS = "<password>"

def execute_ipmi_command(command):
    full_command = f"ipmitool -I lanplus -H {IPMIHOST} -U {IPMIUSER} -P \"{IPMIPASS}\" {command}"
    result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode().strip())
    if result.stderr:
        print(result.stderr.decode().strip())

def power_on():
    print("Powering on the server...")
    execute_ipmi_command("chassis power on")

def power_off():
    print("Powering off the server...")
    execute_ipmi_command("chassis power off")

def set_fan_speed(speed):
    print(f"Setting fan speed to {speed}%...")
    fan_speed_value = int((speed * 255) / 100)
    execute_ipmi_command(f"raw 0x30 0x30 0x02 0xff {hex(fan_speed_value)}")

def enable_dynamic_fan_control():
    print("Enabling dynamic fan control...")
    execute_ipmi_command("raw 0x30 0x30 0x01 0x01")

def disable_dynamic_fan_control():
    print("Disabling dynamic fan control...")
    execute_ipmi_command("raw 0x30 0x30 0x01 0x00")

# Argument Parsing
parser = argparse.ArgumentParser(description='Server Management Script')
parser.add_argument('-p', '--power', choices=['on', 'off'], help='Power on or off the server')
parser.add_argument('-f', '--fan', type=int, choices=range(0, 101), metavar="[0-100]", help='Set fan speed percentage')
parser.add_argument('-d', '--dynamic', choices=['on', 'off'], help='Toggle dynamic fan control')

args = parser.parse_args()

# Check for no action
if not any([args.power, args.fan, args.dynamic]):
    parser.print_help()
    exit()

# Execute based on arguments
if args.power == 'on':
    power_on()
elif args.power == 'off':
    power_off()

if args.fan is not None:
    set_fan_speed(args.fan)

if args.dynamic == 'on':
    enable_dynamic_fan_control()
elif args.dynamic == 'off':
    disable_dynamic_fan_control()