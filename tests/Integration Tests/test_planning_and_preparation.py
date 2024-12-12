#from src.planning_and_preparation import planning_and_preparation
import unittest
import os
import datetime
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def planning_and_preparation():
    """
    Import not quite working as expected!
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


class TestPlanningAndPreparation(unittest.TestCase):

    def setUp(self):
        self.report_file = "pentest_planning_report.txt"

    def tearDown(self):
        if os.path.exists(self.report_file):
            os.remove(self.report_file)

    def test_planning_and_preparation(self):
        result = planning_and_preparation()
        self.assertEqual(result, self.report_file)
        self.assertTrue(os.path.exists(self.report_file))
        with open(self.report_file, 'r', encoding='UTF-8') as file:
            content = file.read()

        # Check if the content contains expected information
        self.assertIn(
            "Penetration Test Planning report Generated at:", content)
        self.assertIn("Sample System: Linux Server", content)
        self.assertIn("In-scope: Internal network (192.168.1.0/24)", content)
        self.assertIn("Out-of-scope: External facing services", content)


if __name__ == '__main__':
    unittest.main()  # allows me to run directly from script::
