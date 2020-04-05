#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0", "numpy", "pandas", "matplotlib", "pysam",
                "vcfpy", "plotly"]

setup_requirements = ["pytest-runner", ]

test_requirements = ["pytest", "opencv-python"]

setup(  # pragma: no cover
    author="Roberto Preste",
    author_email="robertopreste@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Plot variants on the human mitochondrial genome.",
    entry_points={
        "console_scripts": [
            "mitoviz=mitoviz.cli.mitoviz_plot:main",
            "mitoviz-base=mitoviz.cli.mitoviz_base:main"
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="mitoviz",
    name="mitoviz",
    packages=find_packages(include=["mitoviz"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/robertopreste/mitoviz",
    version='0.8.0',
    zip_safe=False,
)
