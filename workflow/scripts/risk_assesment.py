
import json


def risk_assessment(input_file, output_file):
    """
    Performs a risk assessment based on the exploitation results.

    Args:
        input_file (str): Path to the input JSON file containing exploitation data.
        output_file (str): Path to the output JSON file where the risk assessment report will be written.
    """
    # Read the input JSON file
    with open(input_file, 'r') as file:
        exploit_data_list = json.load(file)

    risk_reports = []

    for exploit_data in exploit_data_list:
        for result in exploit_data.get("exploit_simulation_results", []):
            risk_level = "Low"

            if result.get("exploitability_score", 0) > 8.0:
                risk_level = "High"
            elif result.get("exploitability_score", 0) > 5.0:
                risk_level = "Medium"

            risk_report = {
                "ip_address": exploit_data.get("ip_address"),
                "operating_system": exploit_data.get("operating_system"),
                "vulnerability": result.get("vulnerability"),
                "exploitability_score": result.get("exploitability_score"),
                "potential_impact": result.get("potential_impact"),
                "simulation_status": result.get("simulation_status"),
                "risk_level": risk_level
            }

            risk_reports.append(risk_report)

    # Write the risk assessment reports to the output JSON file
    with open(output_file, 'w') as file:
        json.dump(risk_reports, file, indent=4)
