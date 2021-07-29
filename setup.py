from setuptools import setup, find_packages

setup(
    name = 'Message Classification',
    version = 1.0,
    author = 'Mohamed Azzam',
    author_email = 'moh3azzam@hotmail.com',
    description = 'Classify comming messages',
    python_requires = '>=3.7',
    # include_package_data=True,
    # install_requires=['Flask'],
    packages=find_packages(),
)