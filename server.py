import argparse
import subprocess

# Server IPMI details
IPMIHOST = "192.168.1.223"
IPMIUSER = "root"
IPMIPASS = "<password>"

def execute_ipmi_command(command):
    full_command = f"ipmitool -I lanplus -H {IPMIHOST} -U {IPMIUSER} -P {IPMIPASS} {command}"
    subprocess.run(full_command, shell=True)

def power_on():
    print("Powering on the server...")
    execute_ipmi_command("chassis power on")

def set_fan_speed(speed):
    print(f"Setting fan speed to {speed}%...")
    # You'll need to convert the percentage to your server's specific command.
    # This is a placeholder for how you might implement it.
    fan_speed_value = int((speed * 255) / 100)  # Example conversion
    execute_ipmi_command(f"raw 0x30 0x30 0x02 0xff {hex(fan_speed_value)}")

def toggle_dynamic_fan_control():
    print("Toggling dynamic fan control...")
    # Placeholder - Implement the actual IPMI command to toggle dynamic control
    execute_ipmi_command("raw 0x30 0x30 0x01 0x01")  # This command may need to be adjusted

# Argument Parsing
parser = argparse.ArgumentParser(description='Server Management Script')
parser.add_argument('-p', '--power', choices=['on', 'off'], help='Power on or off the server')
parser.add_argument('-f', '--fan', type=int, choices=range(0,101), metavar="[0-100]", help='Set fan speed percentage')
parser.add_argument('-d', '--dynamic', action='store_true', help='Toggle dynamic fan control')

args = parser.parse_args()

# Execute based on arguments
if args.power == 'on':
    power_on()
elif args.power == 'off':
    # Here, you can add a function to power off if desired
    pass
if args.fan is not None:
    set_fan_speed(args.fan)
if args.dynamic:
    toggle_dynamic_fan_control()
