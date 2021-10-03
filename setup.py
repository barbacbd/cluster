from setuptools import setup, find_namespace_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cluster',
    version='1.0.0',
    description='Package to assist with clustering work. Makes use of several indexing and clustering algorithms.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Brent Barbachem',
    author_email='barbacbd@dukes.jmu.edu',
    license='Proprietary',
    include_package_data=True,
    package_data={},
    python_requires='>=3.4, <4',
    install_requires=[
        'sklearn',
        'pandas',
        'numpy',
        'rpy2'
    ],
    dependency_links=[
        'https://pypi.org/simple/'
    ],
    scripts=['cluster/cluster'],
    zip_safe=False
)
