# -*- coding: utf-8 -*-
"""
"""
import importlib
import pathlib
import yaml

from bpdb import set_trace


class Run(object):
    """
    """
    ABS_PATH = pathlib.Path(__file__).absolute().parent

    def __init__(self):
        self.config = self._load_config()

    def __call__(self, x):
        module = self._load_estimate_module()
        y = module(x)
        return y

    def __repr__(self):
        return str(self.config)

    def _load_config(self):
        config_path = self.ABS_PATH / 'config.yml'
        with open(config_path, 'r') as f:
            config = yaml.load(f)
        return config

    def _load_estimate_module(self):
        estimate_path = self.ABS_PATH / 'repos' / self._repo_name / 'estimate.py'
        if not estimate_path.exists():
            raise FileNotFoundError  # TODO: need to separate error pattern whether from not found file or module.
        m = importlib.import_module('repos.{}.estimate'.format(self._repo_name))
        estimate = m.Estimate()
        return estimate

    @property
    def _module_name(self):
        return self.config['Module']['name']

    @property
    def _repo_name(self):
        return self.config['Module']['repo']

    def update_repo(self, repo_name):
        self.config['Module']['repo'] = repo_name

