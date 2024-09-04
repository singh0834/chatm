from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

# get version from __version__ variable in chat/__init__.py
from chat import __version__ as version

setup(
    name='chat',
    version=version,
    description='Chat application for frappe',
    author='Abhishek Chougule',
    author_email='abhishek.c@onehash.ai',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
