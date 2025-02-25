import re
from config import IP_REGEX_PATTERN


def validate_ip(ip_address):
    """
    Validates the format of the given IP address.

    This function checks if the provided IP address matches the pattern
    defined for a valid IP address. The pattern must consist of four octets
    (0-255) separated by periods (e.g., 192.168.1.1). Leading or trailing
    whitespace is removed before validation.

    Args:
        ip_address (str): The IP address string to be validated.

    Returns:
        bool: True if the IP address is valid according to the regex pattern,
              False otherwise.
    """
    ip_address = ip_address.strip()  # Remove any leading/trailing spaces
    return bool(re.match(IP_REGEX_PATTERN, ip_address))


def validate_port_range(start_port, finish_port):
    """
    Ensures that the provided port range is valid.

    This function checks if the specified port range is within the valid range
    (1-65535) and that the start port is less than or equal to the finish port.

    Args:
        start_port (int): The starting port number in the range.
        finish_port (int): The finishing port number in the range.

    Returns:
        bool: True if the port range is valid, False otherwise.
    """
    return 1 <= start_port <= 65535 and start_port <= finish_port <= 65535


def get_valid_ip_input():
    """
    Prompts the user to input a valid IP address.

    This function repeatedly asks the user for an IP address until a valid one
    is entered. It uses the `validate_ip` function to check the format of the
    entered IP address.

    Returns:
        str: A valid IP address entered by the user.
    """
    while True:
        ip_address = input("Input the IP address: ")
        if validate_ip(ip_address):
            return ip_address
        print("Invalid IP format! Please enter a valid IP.")


def get_valid_port_input(prompt, min_value, max_value):
    """
    Prompts the user to input a valid port number within a specified range.

    This function repeatedly asks the user to enter a port number, checking
    that the input is an integer and lies within the specified range.
    If the input is invalid, an error message is displayed and the prompt
    is repeated.

    Args:
        prompt (str): The message displayed to the user to input a port.
        min_value (int): The minimum valid port number.
        max_value (int): The maximum valid port number.

    Returns:
        int: A valid port number entered by the user.
    """
    while True:
        try:
            port = int(input(prompt))
            if min_value <= port <= max_value:
                return port
            else:
                print(f"Please enter a port between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
