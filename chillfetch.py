#!/usr/bin/env python

import platform
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

def get_system_info():
    system = platform.system()
    release = platform.release()
    architecture = platform.architecture()[0]
    distro = get_linux_distribution() if system == 'Linux' else None
    return system, release, architecture, distro

def get_linux_distribution():
    try:
        with open('/etc/os-release', 'r') as f:
            for line in f:
                if line.startswith('PRETTY_NAME='):
                    return line.split('=')[1].strip().strip('"')
    except FileNotFoundError:
        return None

def get_cpu_info():
    try:
        cpu_info = subprocess.check_output(['lscpu']).decode().splitlines()
        for line in cpu_info:
            if "Model name:" in line:
                model_name = line.split(':')[1].strip()
                return model_name
    except FileNotFoundError:
        return "Unknown"

def get_gpu_info():
    try:
        gpu_info = subprocess.check_output(['lspci', '-v', '-nn']).decode().splitlines()
        for line in gpu_info:
            if "VGA compatible controller" in line:
                gpu_name = line.split(':')[-1].split('[')[0].strip()
                return gpu_name
    except FileNotFoundError:
        return "Unknown"

def main():
    system, release, architecture, distro = get_system_info()
    cpu = get_cpu_info()
    gpu = get_gpu_info()

    cat_ascii = """
  _
  |\\'/-..--.
 / _ _   ,  ;   chillfetch  ^\o.o/^ (by niko)
`~=`Y'~_<._./
 <`-....__.'  
"""

    print(Style.BRIGHT + Fore.MAGENTA + f"{cat_ascii}")
    if distro == "Arch Linux":
        print(Fore.CYAN + "[easter egg :3]")
        print(Fore.BLUE + "katt says   i use arch BTW.")
        print("\n")

    print(Fore.CYAN + "[os]")
    print(Fore.BLUE + f"os   {system} {release}")
    print(Fore.BLUE + f"architecture   {architecture}")
    if distro:
        print(Fore.BLUE + f"distro   {distro}")
    print("\n")
    print(Fore.CYAN + "[hardware]")
    print(Fore.BLUE + f"cpu   {cpu}") 
    print(Fore.BLUE + f"gpu   {gpu}")

if __name__ == "__main__":
    main()
