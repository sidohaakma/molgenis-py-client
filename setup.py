from setuptools import setup

setup(
    name='molgenis-py-client',
    version='0.1.0',
    description='The Python client for the MOLGENIS REST API',
    url='https://github.com/molgenis/molgenis-py-client/',
    license='GNU Lesser General Public License 3.0',
    packages=['molgenis'],
    install_requires=['requests==2.21.0']
)