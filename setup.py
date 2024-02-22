from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    description='Example python package',
    long_description=open('readMe.md').read(),
    url='',
    author='my Name',
    install_requires = ['numpy'],
    author_email='myEmail@email.com'
)