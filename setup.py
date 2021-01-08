from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='altai64',
    version='0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts':
            ['startweb = altai64.webserver:run_server']
        },
    install_requires=[
        'Flask==1.1.2'
    ]
)