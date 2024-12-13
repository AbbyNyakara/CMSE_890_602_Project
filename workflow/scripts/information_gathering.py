import json
import os

# Regenerated this function with chatgpt - in order to produce a json file
# original provides a python dictionary


def information_gathering(output_file):
    """
    Simulates the reconnaissance phase of a penetration test.

    The function reads the dummy data from data/network_log_data.json instead of performing
    actual network scans, and writes the result to a specified output file.

    Args:
        output_file (str): Path to the output file where the result will be written.

    Returns:
        None
    """
    try:
        with open('CMSE_890_602_Project/src/data/network_log_data.json', 'r', encoding='UTF-8') as file:
            network_logs = json.load(file)

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write the network logs to the output file
        with open(output_file, 'w', encoding='UTF-8') as outfile:
            json.dump(network_logs, outfile, indent=4)

        print(f"Information gathering results written to {output_file}")
    except FileNotFoundError:
        print("Input file not found")
    except json.JSONDecodeError:
        print("Error decoding JSON from input file")
    except IOError:
        print("Error writing to output file")
