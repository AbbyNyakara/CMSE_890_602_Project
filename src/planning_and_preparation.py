
import datetime


def planning_and_preparation():
    """
    Simulates the planning and preparation phase of a penetration test.

    This function defines the scope and goals of the penetration test, including the systems
    to be tested and the testing methods to be used, and documents these details in a report file.

    Returns:
        report_file (str): The generated report file(a text file) containing the primary information.
    """
    # Define the details
    system_info = "Sample System: Linux Server"
    scope_allowed = "In-scope: Internal network (192.168.1.0/24)\n Out-of-scope: External facing services"

    now = datetime.datetime.now()  # Create timestamp of report
    report_content = f"""Penetration Test Planning report Generated at: {now}\n
                    System Information:
                    {system_info}

                    Test Scope:
                    {scope_allowed}
                     """
    # Create and write to a report file:
    file = "pentest_planning_report.txt"

    with open(file, 'a+', encoding='UTF-8') as report_file:
        report_file.write(report_content)

    return file
