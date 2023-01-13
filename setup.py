from setuptools import find_packages, setup

setup(
    name='django-fakeit',
    packages=find_packages(include=['django-fakeit']),
    version='0.1.0',
    description='its a django module to create dummy data based on models in django',
    author='MAzimi',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner',"django"],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)