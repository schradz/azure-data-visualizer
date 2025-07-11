import pytest
from unittest.mock import patch, MagicMock
import os
import sys

from azure_retreiver import *

class TestAzureRetreiver:
    """
    Class for testing the functionality of the azure_retreiver.py module, 
    ensuring yaml parsing, WIQL querying, and Work item retreival
    """
    @patch('azure_retreiver.os.path.exists')
    def test_error_thrown_when_no_yaml_present(self, mock_path_exists, tmp_path,):
        """
        Ensure that an error is thrown if no yaml configuration file is present
        """
        mock_path_exists.return_value = False
        non_existent_config_path = tmp_path / "non_existent_config.yaml"
        
        with pytest.raises(FileNotFoundError):
            load_azure_yaml_config(non_existent_config_path)

        mock_path_exists.assert_called_once_with(non_existent_config_path)
        
        
        
        

