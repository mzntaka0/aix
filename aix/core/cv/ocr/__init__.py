# -*- coding: utf-8 -*-
"""
"""
import pathlib
import yaml

# TODO: may be no needed all of codes below
ABS_PATH = pathlib.Path(__file__).absolute().parent


def load_config():
    config_path = ABS_PATH / 'ai.yml'
    with open(config_path, 'r') as f:
        config = yaml.load(f)
    return config


config = load_config()
