from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='webserver',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts':
            ['startweb = webserver.webserver:run_server']
        },
    install_requires=[
        'Flask==1.1.2'
    ]
)