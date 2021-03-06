# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017, 2018 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
"""REANA-Workflow-Monitor."""

from __future__ import absolute_import, print_function

import os
import re

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = [
    "check-manifest>=0.25",
    "coverage>=4.0",
    "pydocstyle>=1.0.0",
    "pytest-cache>=1.0",
    "pytest-cov>=1.8.0",
    "pytest-pep8>=1.0.6",
    "pytest>=3.8.0",
]

extras_require = {
    "docs": ["Sphinx>=1.4.4", "sphinx-rtd-theme>=0.1.9",],
    "tests": tests_require,
}

extras_require["all"] = []
for key, reqs in extras_require.items():
    if ":" == key[0]:
        continue
    extras_require["all"].extend(reqs)

setup_requires = [
    "pytest-runner>=2.7",
]

install_requires = [
    "adage==0.10.0",
    "celery==4.3.0",
    "Flask>=0.12.2",
    "gevent==1.4.0",
    "gevent-websocket==0.10.1",
    "packtivity==0.14.21",
    "python-socketio==4.3.1",
    "pyzmq==18.1.0",
    "yadage==0.20.0",
    "yadage-schemas==0.10.6",
]

packages = find_packages()

# Get the version string. Cannot be done with import!
with open(os.path.join("reana_workflow_monitor", "version.py"), "rt") as f:
    version = re.search('__version__\s*=\s*"(?P<version>.*)"\n', f.read()).group(
        "version"
    )

setup(
    name="reana-workflow-monitor",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    author="REANA",
    author_email="info@reana.io",
    url="https://github.com/reanahub/reana-workflow-monitor",
    packages=["reana_workflow_monitor",],
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
