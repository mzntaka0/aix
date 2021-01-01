# -*- coding: utf-8 -*-
"""
"""
import os
import importlib
import pathlib

ABS_PATH = pathlib.Path(__file__).absolute().parent
module_list = list(map(lambda p: str(p.parent), ABS_PATH.glob('**/ai.yml')))


def get(module_name, repo=None):
    module_path = _validate_module(module_name)
    module = module_path.split('core/')[1].replace(os.path.sep, '.') + '.run'
    m = importlib.import_module('aix.core.' + module)
    run = m.Run()
    return run


def _validate_module(module_name):
    module_path = list(filter(lambda p: module_name in p, module_list))

    if len(module_path) > 2:
        raise AttributeError('Module directory exists more than two. Please delete not needed one')
    if len(module_path) < 1:
        raise AttributeError('This module {} does not exist'.format(module_name))
    return module_path[0]
