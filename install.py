#!/usr/bin/env python3

import os
import subprocess

def colors():
    global white, cyan, lightred, lightgreen, yellow, lightblue, pink
    white = '\033[0;97m'
    cyan = '\033[0;36m'
    lightred = '\033[0;91m'
    lightgreen = '\033[0;92m'
    yellow = '\033[0;93m'
    lightblue = '\033[0;94m'
    pink = '\033[0;95m'
colors()

def main():
    if os.geteuid() != 0:
        print(f"{lightred}[-] {white}Execute as root mode. Use {lightgreen}'sudo python3 install.py'{white}.")
        exit(1)

    zip_file = "dottler.zip"
    dest_dir = "/usr/local/bin"
    dottler_executable = "/usr/local/bin/dottler"
    dottler_py_executable = "/usr/local/bin/dottler.py"

    if os.path.exists(dottler_executable) and os.path.exists(dottler_py_executable):
        print(f"{lightgreen}[+] {white}Dottler already installed. Use {lightgreen}'dottler' {white}to run.")
        exit(0)

    if not os.path.exists(zip_file):
        print(f"{lightred}[-] {white}File not found.")
        exit(1)

    with open(os.devnull, 'w') as nullfile:
        result = subprocess.run(["unzip", zip_file, "-d", dest_dir], stdout=nullfile, stderr=nullfile)

    if result.returncode == 0:
        os.chmod(dottler_executable, 0o755)
        os.chmod(dottler_py_executable, 0o755)
        print(f"{lightgreen}[+] {white}Dottler has been installed. Use {lightgreen}'dottler' {white}to run.")
        if not os.path.exists(dottler_py_executable):
            print(f"{lightred}[-] {white}dottler.py was not found in the package.")
        exit(0)

main()
