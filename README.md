# cs5293sp22-project1
Project Objectives: In this project, we designed a system that accepts plain text documents then detect and redact “sensitive” items. As part of this project, we were asked to redact names, addresses, genders,dates ,phonenumbers and concepts.



Setup.py: The setup.py file contains the details about the project - name, author, version,... from setuptools import setup, find_packages

setup( name='project1', version='1.0', author='Kaustubh Pande', authot_email='kaustubhpande@ou.edu', packages=find_packages(exclude=('tests','docs')) setup_requires=['pytest-runner'], tests_require=['pytest'] )

setup.cfg: contains - [aliases] test=pytest

[tool:pytest] norecursedirs = .*, CVS, _darcs, {arch}, *.egg, venv
