# See license.txt for license details.
# Copyright (c) 2019, Chris Withers

import os

from setuptools import setup, find_packages

base_dir = os.path.dirname(__file__)

setup(
    name='fastapi_sqlalchemy',
    version='0.0.0.dev0',
    author='Chris Withers',
    author_email='chris@withers.org',
    license='MIT',
    description=(
        "Tools to allow FastAPI and SQLAlchemy to work better together, particularly when it comes to pydantic."
    ),
    long_description=open('README.rst').read(),
    url='https://github.com/cjw296/fastapi_sqlalchemy',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(exclude=["tests"]),
    zip_safe=False,
    include_package_data=True,
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'sybil',
            'testfixtures',
        ],
        build=['sphinx', 'sphinx-rtd-theme', 'setuptools-git', 'twine', 'wheel']
    ),
)
