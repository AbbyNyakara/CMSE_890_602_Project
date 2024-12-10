import unittest
import os
import datetime
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.planning_and_preparation import planning_and_preparation

class TestPlanningAndPreparation(unittest.TestCase):
    """
    Simulates the planning and preparation phase of a penetration test.

    This function performs the following tasks:
    1. Defines system information and scope of the penetration test.
    2. Creates a timestamp for the report.
    3. Generates a report content string with the gathered information.
    4. Writes the report content to a file named 'pentest_planning_report.txt'.

    The report includes:
    - Timestamp of report generation
    - System information (e.g., "Sample System: Linux Server")
    - Test scope, including in-scope and out-of-scope areas

    Returns:
    str: The name of the file where the report is written ('pentest_planning_report.txt').

    Note:
    - The function appends to the file if it already exists.
    - The file is created in the current working directory.
    - The function uses UTF-8 encoding when writing to the file.

    Raises:
    IOError: If there's an issue writing to the file.

    Example:
    >>> file_name = planning_and_preparation()
    >>> print(file_name)
    'pentest_planning_report.txt'
    """

    def setUp(self):
        self.report_file = "pentest_planning_report.txt"

    def tearDown(self):
        if os.path.exists(self.report_file):
            os.remove(self.report_file)

    def test_planning_and_preparation(self):
        # Call the function
        result = planning_and_preparation()

        # Check if the function returns the correct filename
        self.assertEqual(result, self.report_file)

        # Check if the file was created
        self.assertTrue(os.path.exists(self.report_file))

        # Read the content of the file
        with open(self.report_file, 'r', encoding='UTF-8') as file:
            content = file.read()

        # Check if the content contains expected information
        self.assertIn(
            "Penetration Test Planning report Generated at:", content)
        self.assertIn("Sample System: Linux Server", content)
        self.assertIn("In-scope: Internal network (192.168.1.0/24)", content)
        self.assertIn("Out-of-scope: External facing services", content)

        # Check if the timestamp in the report is recent (within the last minute)
        report_time_str = content.split("Generated at: ")[1].split("\n")[0]
        report_time = datetime.datetime.strptime(
            report_time_str, "%Y-%m-%d %H:%M:%S.%f")
        time_difference = datetime.datetime.now() - report_time
        self.assertLess(time_difference.total_seconds(), 60)


if __name__ == '__main__':
    unittest.main()
