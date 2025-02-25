from scanner import PortScanner
from utils import get_valid_ip_input, get_valid_port_input


def scan_all_ports():
    """
    Initiates the scanning of all ports (1-65535) for a user-specified IP address.

    This function asks the user for a valid IP address, then creates an instance of the
    PortScanner class to scan all ports. It outputs a list of open ports and their
    corresponding services if known.

    Returns:
        None
    """
    ip_address = get_valid_ip_input()  # Get a valid IP address from the user
    print("Scanning all ports...")

    # Scan all ports from 1 to 65535
    ports = list(range(1, 65536))

    # Instantiate the PortScanner class and perform the port scan
    scanner = PortScanner()
    scanner.scan_ports(ip_address, ports)
    scanner.display_open_ports()


def scan_target_ports():
    """
    Initiates the scanning of a user-defined range of ports for a specified IP address.

    This function asks the user for a valid IP address and a valid port range, then creates
    an instance of the PortScanner class to scan the specified port range. It displays the
    open ports and their corresponding services if known.

    Returns:
        None
    """
    ip_address = get_valid_ip_input()  # Get a valid IP address from the user
    start_port = get_valid_port_input("Select the starting port (1 - 65535): ", 1, 65535)
    finish_port = get_valid_port_input(f"Select the finish port ({start_port} - 65535): ", start_port, 65535)
    print(f"Scanning ports {start_port} - {finish_port}...")

    # Scan the user-defined range of ports
    ports = list(range(start_port, finish_port + 1))

    # Instantiate the PortScanner class and perform the port scan
    scanner = PortScanner()
    scanner.scan_ports(ip_address, ports)
    scanner.display_open_ports()


def main():
    """
    Main function that provides a user interface for selecting scan options.

    This function displays a menu and prompts the user to choose one of the following options:
    1. Scan all ports.
    2. Scan a user-defined range of ports.
    0. Exit the program.

    The chosen option is executed, and the user is returned to the menu after each scan.

    Returns:
        None
    """
    print("Welcome to PortScanner!")
    while True:
        try:
            # Present the menu and get the user's choice
            menu_choice = int(input(f"What do you want to do?\n"
                                    f"1. Scan all ports\n"
                                    f"2. Scan target ports\n"
                                    f"0. Exit\n"))

            if menu_choice == 0:
                exit(0)  # Exit the program
            elif menu_choice == 1:
                scan_all_ports()  # Perform a full port scan (1-65535)
            elif menu_choice == 2:
                scan_target_ports()  # Perform a scan on a user-specified range of ports
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Please input a number!")


if __name__ == "__main__":
    main()  # Run the program
