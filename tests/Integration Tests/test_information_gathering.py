import unittest
import json
import os
import sys
from unittest.mock import patch, mock_open
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.information_gathering import information_gathering  # Replace 'your_module' with the actual module name

class TestInformationGathering(unittest.TestCase):

    def setUp(self):
        # Sample data that mimics the content of network_log_data.json
        self.sample_data = {
            "ip_addresses": ["192.168.1.1", "192.168.1.2"],
            "open_ports": [80, 443, 22],
            "services": ["HTTP", "HTTPS", "SSH"]
        }

    def test_successful_information_gathering(self):
        # Mock the open function to return our sample data
        mock_file_content = json.dumps(self.sample_data)
        with patch("builtins.open", mock_open(read_data=mock_file_content)):
            result = information_gathering()

        self.assertEqual(result, self.sample_data)

    def test_file_not_found(self):
        # Mock the open function to raise FileNotFoundError
        with patch("builtins.open", side_effect=FileNotFoundError):
            with patch("builtins.print") as mock_print:
                result = information_gathering()

        mock_print.assert_called_once_with("File not found")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()