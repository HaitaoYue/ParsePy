import os
from setuptools import setup, Command
from unittest import TextTestRunner, TestLoader


class TestCommand(Command):
    '''Run test suite using `python setup.py test `'''
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        '''Run test suite in parse_rest.tests'''
        tests = TestLoader().loadTestsFromNames(['parse_rest.tests'])
        t = TextTestRunner(verbosity=1)
        t.run(tests)


setup(
    name='parse_client',
    version='0.1.0',
    description='A client library for Parse.com\'.s REST API',
    url='https://github.com/HaitaoYue/ParsePy',
    packages=['parse_client'],
    package_data={"parse_client": [os.path.join("cloudcode", "*", "*")]},
    install_requires=['six'],
    maintainer='Haitao Yue',
    maintainer_email='hightallyht@gmail.com',
    cmdclass={'test': TestCommand},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ]
)
