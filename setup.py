''' This setup.py file is essential part of packaging and distributing Python projects and is used 
to define the configuration of the project such as metadata , dependencies '''



from setuptools import find_packages , setup
from typing import List

def get_requirements()->List[str]:
    '''This is a function returns list of requirements. '''
    # Defining a list
    requirement_lst : List[str] = []
    try :
        with open('requirements.txt' , 'r') as file:
            lines = file.readlines()
            for line in lines :
                requirement = line.strip()
                # Ignoring all the empty lines and -e .
                if requirement and requirement != '-e .' :
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt is not found")

    return requirement_lst


setup(
    name = "NetworkSecurity" ,
    version = "0.0.1" ,
    author = "Sai Teja Pochana" ,
    author_email= "saitejapochana2324@gmail.com" ,
    packages = find_packages(),
    install_requires = get_requirements()
)