from setuptools import setup, find_packages

setup(
    name='hipp_mapping',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hipp_mapping = main:main'
        ]
    },
)
