import os
import sys
from typing import List
from setuptools import setup, find_packages
def get_req(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
    return requirements
setup(
    name= 'cybersecurity1999dataset',
    version= '0.0.0',
    author= 'BhaskarMishra',
    author_email= 'bhaskarmishra1590@gmail.com',
    packages= find_packages(),
    install_requires = get_req('requirements.txt')
)