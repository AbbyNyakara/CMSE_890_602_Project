import datetime

def planning_and_preparation():
    """
    Simulates the planning and preparation phase of a penetration test.

    function gathers system information, defines the scope of the test,
    and writes this information to a report file.

    Returns:
    report_file
    """

    system_info = "Sample System: Linux Server"
    scope_allowed = "In-scope: Internal network (192.168.1.0/24)\n Out-of-scope: External facing services"

    now = datetime.datetime.now()  
    report_content = f"""Penetration Test Planning report Generated at: {now}\n
                    System Information:
                    {system_info}

                    Test Scope:
                    {scope_allowed}
                     """

    file = "pentest_planning_report.txt"

    with open(file, 'a+', encoding='UTF-8') as report_file:
        report_file.write(report_content)

    return file
