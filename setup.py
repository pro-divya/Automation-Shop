from setuptools import setup, find_packages

setup(
    name='tracing',
    version='0.1',
    description='Tools for tracing',
    author='G2 Team',
    install_requires=[
        'requests', 'lxml', 'image', 'Pillow',
        'scipy', 'mongoengine', 'pika', 'configparser',
        'selenium', 'beautifulsoup4', 'tensorflow', 'tracing'
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={'tracing': ['tracing/js/*.js']}
)
