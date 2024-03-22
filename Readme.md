# idrac helper

Really this is a personal python script for myself. If you find it useful, great! If not, that's fine too. If you have a suggestion, I'm all ears. I can't promise I'll implement it, I'm pretty bad at coding. I'll try though, sounds like fun! Maybe...

Anyway, this script is designed to do a few things with my 720xd. It powers it on/off, changes the fan speed, and toggles the dynamic fan speed. 

## Options
```-h, --help            show this help message and exit
  -p {on,off}, --power {on,off}
                        Power on or off the server
  -f [0-100], --fan [0-100]
                        Set fan speed percentage
  -t, --temp            Adjust fan speed based on temperature
  -d {on,off}, --dynamic {on,off}
                        Toggle dynamic fan control
```

## Requirements
- Python
- [ipmitool](https://github.com/ipmitool/ipmitool)
    - `sudo apt install ipmitool` for Ubuntu/Debian
    - `sudo dnf install ipmitool` for Fedora//RHEL & clones
    - `sudo pacman -S ipmitool` for Arch
    - `brew install ipmitool` for MacOS

## Usage
```$ python3 server.py -p on
$ python3 server.py -p off
$ python3 server.py -f 50
$ python3 server.py -t
```

## Notes
I'm currently testing this script on my server as a temperature monitoring solution. I have it set as a cronjob on my pihole server to run every 5 minutes.