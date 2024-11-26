"""
This program simulates a cybersecurity penetration testing process.

This program emulates the key stages of a network penetration test:
1. Preparation
2. Network scanning / information gathering
3. Vulnerability detection and analysis
4. Exploitation phase
5. Risk Assesment
6. Final Report generation

The simulation is limited to analyzing network logs and does not perform actual network operations.
The reports generated in this process are not actual cases, but dummy examples. 
"""

from planning_and_preparation import planning_and_preparation
from information_gathering import information_gathering
from vulnerability_analysis import vulnerability_analysis
from check_vulnerability_status import check_vulnerability_status
from attempt_exploit import attempt_exploit
from check_exploitation_status import check_exploitation_status
from risk_assesment import risk_assessment


def main():
    """
    The main function that runs the penetration testing program functions and prints the report.
    """
    pentest_report = []

    planning_and_preparation()  # working
    information_gathering_report = information_gathering()  # working
    vulnerability_analysis_report = vulnerability_analysis(
        information_gathering_report)
    vulnerability_status_report = check_vulnerability_status(
        vulnerability_analysis_report)
    pentest_report.append(vulnerability_status_report)
    exploit_report = attempt_exploit(vulnerability_status_report)
    exploit_status_report = check_exploitation_status(
        {"exploit_simulation_results": exploit_report})
    pentest_report.append(exploit_status_report)


    for report in pentest_report:
        print(report)

    return pentest_report


if __name__ == "__main__":
    main()
