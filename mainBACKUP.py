import socket
import threading
import re
from time import sleep

MAX_THREADS_COUNT = 10000
IP_REGEX_PATTERN = ("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.)"
                    "{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
IP_REGEX_CHECK_LETTERS_PATTERN = "[a-zA-Z]"


open_ports = {}
threads = []
known_ports = {
    20: "FTP Data Transfer",
    21: "FTP Command",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    143: "IMAP",
    161: "SNMP",
    194: "IRC",
    443: "HTTPS",
    445: "Microsoft-DS",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP Submission",
    636: "LDAPS",
    989: "FTPS Data",
    990: "FTPS Command",
    993: "IMAPS",
    995: "POP3S",
    1433: "Microsoft SQL Server",
    1434: "Microsoft SQL Server Resolution",
    1521: "Oracle Database",
    3306: "MySQL",
    3389: "RDP (Remote Desktop Protocol)",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Proxy",
    8443: "HTTPS Alternate",
    9000: "PHP-FPM",
    27017: "MongoDB",
    50000: "SAP",
}


def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket
    socket.setdefaulttimeout(2.0)
    check_open = sock.connect_ex((ip, port))
    if check_open == 0:
        open_ports[port] = "OPEN"
    else:
        open_ports[port] = "CLOSED"

    sock.close()


def scan_ports(host, ports):
    for port in ports:
        thread = threading.Thread(target=scan_port, args=[host, port])
        thread.start()
        threads.append(thread)
        while threading.active_count() >= MAX_THREADS_COUNT:
            sleep(1)
    for thread in threads:
        thread.join()


def scan_all_ports():
    ports = []

    ip_address = input(f"Input the ip address: ")

    print("Scanning all ports...")

    for port in range(1, 65535 + 1, 1):
        ports.append(port)

    scan_ports(ip_address, ports)
    for port in sorted(open_ports):
        if open_ports[port] == "OPEN":
            if port in known_ports:
                open_ports[port] += f" [{known_ports[port]}]"
            print(f"Port {port}: {open_ports[port]}")


def scan_target_ports():
    ports = []

    while True:
        ip_address = input(f"Input the ip address: ")
        if re.match(IP_REGEX_PATTERN, ip_address):
            break
        elif re.match(IP_REGEX_CHECK_LETTERS_PATTERN, ip_address):
            print("IP can contain only numbers and periods")
        else:
            print("IP is invalid! Valid IP format: 255.255.255.255")

    while True:
        try:
            start_port = int(input(f"Select the starting port (1 - 65535): "))
            if 1 <= start_port <= 65535:
                break
            elif start_port > 65535:
                print("Please input a port lower than 65536!")
            elif start_port < 1:
                print(f"Please input a port higher than 0!")
        except TypeError:
            print("Please input only numbers!")

    while True:
        try:
            finish_port = int(input(f"Select the finish port ({start_port} - 65535): "))
            if start_port <= finish_port <= 65535:
                break
            elif finish_port > 65535:
                print("Please input a port lower than 65536!")
            elif finish_port < start_port:
                print(f"Please input a port higher than {start_port}!")
        except TypeError:
            print("Please input only numbers!")

    print(f"Scanning ports {start_port} - {finish_port}...")

    for port in range(start_port, finish_port + 1, 1):
        ports.append(port)

    scan_ports(ip_address, ports)
    for port in sorted(open_ports):
        if open_ports[port] == "OPEN":
            if port in known_ports:
                open_ports[port] += f" [{known_ports[port]}]"
            print(f"Port {port}: {open_ports[port]}")


def main():
    print("Welcome to PortScanner!")
    print("_" * 30)

    while True:
        try:
            menu_choice = int(input(f"What do you want to do?\n"
                                    f"1. Scan all ports\n"
                                    f"2. Scan target ports\n"
                                    f"0. Exit\n"))
            if menu_choice == 0:
                exit(0)
            elif menu_choice == 1:
                scan_all_ports()
            elif menu_choice == 2:
                scan_target_ports()
            else:
                print("Please input a valid choice!")
        except ValueError:
            print("Please input a number!")


#if __name__ == "__main__":
   # main()
