import pytest
from unittest.mock import patch, MagicMock
import os
import sys

#Finding modules in 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0, os.path.join(project_root, 'src'))

import configuration_loader
from configuration_loader import *

class TestConfigurationLoader:
    """
    Class for testing the functionality of the azure_retreiver.py module, 
    ensuring yaml parsing, WIQL querying, and Work item retreival
    """
    @patch('configuration_loader.os.path.exists')
    def test_error_thrown_when_no_yaml_present(self, mock_path_exists, tmp_path):
        """
        Ensure that an error is thrown if no yaml configuration file is present
        """
        mock_path_exists.return_value = False
        non_existent_config_path = tmp_path / "non_existent_config.yaml"
        
        with pytest.raises(FileNotFoundError):
            load_config(non_existent_config_path)

        mock_path_exists.assert_called_once_with(non_existent_config_path)
        

    @patch('configuration_loader.os.path.exists')    
    @patch('configuration_loader.yaml.safe_load')
    def test_cache_is_stored_after_loading_yaml(self, mock_path_exists, mock_safe_load, tmp_path):
        """
        Ensure that the configuration is cached when loaded
        """
        #Setup
        configuration_loader._cached_config = None
        test_config_load = {'queries': {'test_query':{'wiql': 'SELECT * FROM WorkItems'}}}
        mock_path_exists.return_value = True
        mock_safe_load.return_value = test_config_load
        config_path = tmp_path / "config.yaml"
        #Function Calls
        parsed_config = load_config(config_path)
        cached_config = load_config(config_path)
        #Test Checks
        assert parsed_config is test_config_load
        assert configuration_loader._cached_config is test_config_load
        assert cached_config is parsed_config
        mock_path_exists.assert_called_once_with(config_path)
        mock_safe_load.assert_called_once()
