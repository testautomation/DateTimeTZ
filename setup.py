#!/usr/bin/env python
# -*- coding: utf-8 -*-


from io import open  # required for Python 2
from os.path import abspath, dirname, join
from setuptools import find_packages, setup

CURDIR = dirname(abspath(__file__))

classifiers = """
Development Status :: 4 - Beta
License :: OSI Approved :: Apache Software License
Operating System :: POSIX
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.6
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
""".strip().splitlines()


curdir = dirname(abspath(__file__))
with open(join(curdir, "src", "DateTimeTZ", "version.py"), encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split("=")[1].strip(" '\"")
            break
    else:
        version = "0.0.1"
with open(join(curdir, "README.md"), encoding="utf-8") as f:
    readme = f.read()
with open(join(curdir, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read()

setup(
    name             = "robotframework-datetime-tz",
    version          = version,
    description      = "Robot Framework library for date/time with locales and time zones",
    long_description = readme,
    long_description_content_type="text/markdown",
    author           = "Tset Noitamotua",
    author_email     = "tset.no@gmail.com",
    url              = "https://github.com/testautomation/DateTimeTZ",
    license          = "Apache License 2.0",
    keywords         = "robotframework test library date time locales time zones",
    classifiers      = classifiers,
    install_requires = requirements,
    zip_safe         = False,
    package_dir      = {"": "src"},
    packages         = find_packages("src"),
)
