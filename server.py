import argparse
import subprocess

# Server IPMI details
IPMIHOST = "192.168.1.223"
IPMIUSER = "root"
IPMIPASS = "<oops>"

def execute_ipmi_command(command):
    full_command = f"ipmitool -I lanplus -H {IPMIHOST} -U {IPMIUSER} -P \"{IPMIPASS}\" {command}"
    print(f"Executing command: {full_command}")  # Print the full command to debug
    result = subprocess.run(full_command, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

def power_on():
    print("Powering on the server...")
    execute_ipmi_command("chassis power on")

def power_off():
    print("Powering off the server...")
    execute_ipmi_command("chassis power off")

def set_fan_speed(speed):
    print(f"Setting fan speed to {speed}%...")
    # You'll need to convert the percentage to your server's specific command.
    fan_speed_value = int((speed * 255) / 100)  # Example conversion
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
parser.add_argument('-f', '--fan', type=int, choices=range(0,101), metavar="[0-100]", help='Set fan speed percentage')
parser.add_argument('-d', '--dynamic', choices=['on', 'off'], help='Toggle dynamic fan control')

args = parser.parse_args()

# Execute based on arguments
if args.power == 'on':
    power_on()
elif args.power == 'off':
    power_off()
else:
    print("No action specified. Exiting...")
if args.fan is not None:
    set_fan_speed(args.fan)
if args.dynamic == 'on':
    enable_dynamic_fan_control()
elif args.dynamic == 'off':
    disable_dynamic_fan_control()

if not (args.power or args.fan or args.dynamic):
    parser.print_help()
else:
    if args.power == 'on':
        power_on()
    elif args.power == 'off':
        # Here, you can add a function to power off if desired
        pass
    if args.fan is not None:
        set_fan_speed(args.fan)
