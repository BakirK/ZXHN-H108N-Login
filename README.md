# ZXHN-H108N-Login
Hacking ZXHN H108N Router (brute-force)
This project is a demonstration of how to crack the login of ZTE (ZXHN-H108N) via telnet as described here: https://jalalsela.com/hacking-zxhn-h108n-router/

## Routers that have custom firmware
For routers that have custom firmware installed on them by the ISP, use Telnet-Cracker-Custom-Firmware.py as script with provided wordlist.
On these modems, the telnet connection does not offer an option to enter username (root) and only asks for password, thus the original script won't work.

### Firmware differences
The modems with custom firmware will most likely have differently coloured interface (orange theme instead of green).
The difference it that it changes the default admin password so that it cannot be found by Googling and also locks the default administrator username so that it cannot be changed or prompted to enter upon login.

### How to guide
1. Download and install Python 2.7
2. Download script with provided wordlist
3. Run the script by entering the following command in the cmd
```python
Telnet-Cracker-Custom-Firmware.py -w wordlist.txt
```
4. Upon cracking password, log in to your modem using that password together with username "admin" or "root"

## Authors
* Jalal Sela - _initial work_ - https://jalalsela.com
* Bakir Karović - _added reworked script_

## Licence
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the LICENSE.md file for details
