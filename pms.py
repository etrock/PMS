import configparser
import argparse
import sys
import pathlib
import netifaces as ni
from shells import shells

def main():

    #Build the argument parse object
    parser = argparse.ArgumentParser(
        prog="pms", 
        description="Print out revers shell", 
        add_help=False)

    # Parse config option first
    parser.add_argument("--config", "-c", help="configuration file", default="pms.conf")
    args, remaining_args = parser.parse_known_args()
    # read default configs
    defaults = read_config(args.config)
    ethernet_interface = defaults['ethernet_interface'] if 'ethernet_interface' in defaults.keys() else ""
    ip = defaults['ip'] if 'ip' in defaults.keys() else ""
    port = defaults['port'] if 'port' in defaults.keys() else ""

    #get ip address
    if ip == "" and ethernet_interface == "":
        print("ip address or ethernet_interface is required")
    elif ip == "" and ethernet_interface != "":
        ip = get_ip_from_ni(ethernet_interface)
  
    #TODO: collection of revshells
    parser.add_argument("type", help="type of reverse shell")

    parser.add_argument("--host", "-h", help="host ip address")

    parser.add_argument("--port", "-p", help="port")

    # Parse arguments
    args = parser.parse_args(remaining_args)

    if args.type is not None:
        shell_type = args.type
    
    if args.host is not None:
        ip = args.host
    
    if args.port is not None:
        port = args.port

    print_shell(shell_type, ip, port)

# read config file
def read_config(config_file):
    if config_file == "pms.conf":
        config_file = pathlib.Path(__file__).parent.absolute() / "pms.conf"
    config = configparser.RawConfigParser()
    config.read(config_file)
    details_dict = dict(config.items('default'))
    return details_dict

def print_shell(shell_type, ip, port):
    shell = shells[shell_type].replace('$IP$', ip).replace('$PORT$', port)
    print(shell)

def get_ip_from_ni(ethernet_interface):
    # ni.ifaddresses(ethernet_interface)
    ip = ni.ifaddresses(ethernet_interface)[ni.AF_INET][0]['addr']
    return ip


# debug interface list
def get_interfaces():
    ifaces = ni.interfaces()
    for iface in ifaces:
        try:
            ip = ni.ifaddresses(iface)[ni.AF_INET][0]["addr"]
            print(f"IP: {ip} from Interface {iface}")
        except:
            pass

if __name__ == "__main__":
    main()