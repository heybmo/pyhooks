#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup Python file.

Copyright Brian Mo 2019. MIT license, see LICENSE file.
"""
import io
import os
import re
import sys
from setuptools import setup
from typing import Tuple


# See following URL for more info:
# https://devguide.python.org/devcycle/

REQUIRED_PY_VER: Tuple[int, int] = (3, 6)

# Project versions.

if sys.version_info[:2] < REQUIRED_PY_VER:
    raise RuntimeError(
        "Required Python version: {} not met. Version detected: {}".format(
            REQUIRED_PY_VER, sys.version_info[:2]
        )
    )

with io.open("pyhooks/__version__.py") as f:
    version = re.search(r'__version__ = \"(.*?)\"', f.read()).group(1)
