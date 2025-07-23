'''
the setup.py file is an essetial part of packing and
distributing python projects. it is used by setuptools (or 
distutils in older python versions) to define the configuration
or your project,such as its metadata, dependencies , and more'''
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''this function will return list of requirements'''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines = file.readlines()
            # process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file is not found")
    
    return requirement_lst

print(get_requirements())

# setup the metadata
setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author = "Renjini Thomas",
    author_email="renjini2539thomas@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)