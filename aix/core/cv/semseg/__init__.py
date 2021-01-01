# -*- coding: utf-8 -*-
"""
"""
import pathlib
import yaml


ABS_PATH = pathlib.Path(__file__).absolute().parent


def load_config():
    config_path = ABS_PATH / 'config.yml'
    with open(config_path, 'r') as f:
        config = yaml.load(f)
    return config


config = load_config()
print(config)
