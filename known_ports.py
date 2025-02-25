from config import KNOWN_PORTS


def get_known_ports():
    """
    Retrieves the list of known ports and their associated services.

    This function fetches a predefined dictionary of known ports and their
    corresponding service names (e.g., port 80 for HTTP, port 443 for HTTPS)
    from the configuration module (`config`). These known ports are used
    to display more informative descriptions alongside open port scans.

    Returns:
        dict: A dictionary containing port numbers as keys and service
              names/descriptions as values.
    """
    return KNOWN_PORTS
