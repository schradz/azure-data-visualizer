import os

def load_azure_yaml_config(config_path):
    if os.path.exists(config_path) == False:
        raise FileNotFoundError(f"YAML config file not found at {config_path}")