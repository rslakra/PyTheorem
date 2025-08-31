#!/usr/bin/env python

from setuptools import setup

from core.context import handler

setup(
    name="contextvars",
    description="Context variables framework for Python",

    py_modules=["contextlibs"],
    # test_suite = "test_context",

    version=handler.__version__,
    author=handler.__author__,
    author_email=handler.__email__,
    url="https://github.com/rslakra/PyTheorem",
    license=handler.__license__,
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)
