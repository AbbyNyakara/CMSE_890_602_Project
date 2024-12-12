import json


def information_gathering():
    """
    simulats the reconnaisance phase of a penetration test. 

    The function reads the dummy data from data/network_log_data.json instead of performing
    actual network scans 

    Returns:
        dict: A dictionary containing the network information read from a json file. 

    """
    try:
        with open('CMSE_890_602_Project/src/data/network_log_data.json', encoding='UTF-8') as file:
            network_logs = json.load(file)
        return network_logs
    except FileNotFoundError:
        print("File not found")
        return (None)
