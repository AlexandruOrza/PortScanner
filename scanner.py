import socket
import threading
from time import sleep
from config import MAX_THREADS_COUNT
from known_ports import get_known_ports


class PortScanner:
    """
    A class responsible for scanning ports on a given IP address.

    This class allows for scanning individual or multiple ports on a remote
    server or device to determine if they are open or closed. It performs
    the scanning concurrently using threads to improve performance. Additionally,
    the known services associated with open ports are displayed.

    Attributes:
        open_ports (dict): A dictionary storing the status (OPEN/CLOSED) of each port.
        threads (list): A list storing the threads used for concurrent scanning.
        known_ports (dict): A dictionary containing port numbers as keys and service
                             descriptions as values (e.g., HTTP, FTP).
    """

    def __init__(self):
        """
        Initializes the PortScanner object.

        The constructor initializes the attributes needed for scanning, including
        an empty dictionary for storing open ports, a list for managing threads,
        and a dictionary for known port services fetched from the `get_known_ports` function.
        """
        self.open_ports = {}  # stores open ports for a given scan
        self.threads = []     # stores threads for concurrent scanning
        self.known_ports = get_known_ports()  # known ports and their descriptions

    def scan_port(self, ip, port):
        """
        Scans a single port on the provided IP address to check if it is open.

        This function creates a socket, attempts to connect to the specified
        port on the given IP address, and records whether the port is open
        or closed. It updates the `open_ports` dictionary with the result.

        Args:
            ip (str): The target IP address to scan.
            port (int): The port number to scan.

        Returns:
            None
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(2.0)  # Set socket timeout to 2 seconds
        check_open = sock.connect_ex((ip, port))  # Returns 0 if port is open
        if check_open == 0:
            self.open_ports[port] = "OPEN"
        else:
            self.open_ports[port] = "CLOSED"
        sock.close()

    def scan_ports(self, ip, ports):
        """
        Scans a range of ports on a target IP address.

        This function launches multiple threads to scan each port concurrently.
        It ensures that no more than the maximum allowed threads (defined in `MAX_THREADS_COUNT`)
        are running simultaneously. It waits for all threads to finish before returning.

        Args:
            ip (str): The target IP address to scan.
            ports (list): A list of port numbers to scan.

        Returns:
            None
        """
        for port in ports:
            thread = threading.Thread(target=self.scan_port, args=[ip, port])
            thread.start()
            self.threads.append(thread)
            while threading.active_count() >= MAX_THREADS_COUNT:
                sleep(1)  # Prevent too many threads from being created at once
        for thread in self.threads:
            thread.join()  # Wait for all threads to finish

    def display_open_ports(self):
        """
        Displays the open ports along with their associated services.

        This function prints out the list of open ports, and if a port is
        listed in the `known_ports` dictionary, the service name associated
        with the port is appended to the output. It also lets the user know
        if no open ports were found.

        Returns:
            None
        """
        for port in sorted(self.open_ports):
            if self.open_ports[port] == "OPEN":
                if port in self.known_ports:
                    self.open_ports[port] += f" [{self.known_ports[port]}]"
                print(f"Port {port}: {self.open_ports[port]}")

        if "OPEN" not in self.open_ports.values():
            print("No open ports found!")
