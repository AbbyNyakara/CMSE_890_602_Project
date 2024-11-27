
def risk_assessment(exploit_data):
    """
    Performs a risk assessment based on the exploitation results.

    Args:
        exploit_data (dict): Data from the exploitation attempt, including vulnerability, exploitability score, and potential impact.

    Returns:
        dict: A risk assessment report for the exploitation attempt.
    """
    risk_level = "Low"

    if exploit_data.get("exploitability_score", 0) > 8.0:
        risk_level = "High"
    elif exploit_data.get("exploitability_score", 0) > 5.0:
        risk_level = "Medium"

    risk_report = {
        "ip_address": exploit_data.get("ip_address"),
        "operating_system": exploit_data.get("operating_system"),
        "vulnerability": exploit_data.get("vulnerability"),
        "exploitability_score": exploit_data.get("exploitability_score"),
        "potential_impact": exploit_data.get("potential_impact"),
        "simulation_status": exploit_data.get("simulation_status"),
        "risk_level": risk_level
    }

    print("Risk Assessment Report:", risk_report)

    return risk_report
