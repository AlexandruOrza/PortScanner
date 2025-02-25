# Configuration constants for the port scanner application

# Maximum number of concurrent threads that can be active during port scanning.
MAX_THREADS_COUNT = 10000

# Regular expression pattern for validating IPv4 addresses.
# This pattern ensures that the IP address is in the format:
# "xxx.xxx.xxx.xxx", where each "xxx" is a number between 0 and 255.
IP_REGEX_PATTERN = ("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}"
                    "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")

# Dictionary of known ports and their corresponding service descriptions.
# The keys are port numbers, and the values are the service names
# (e.g., "HTTP" for port 80).
KNOWN_PORTS = {
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
