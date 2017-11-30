from setuptools import find_packages, setup

setup(
    name='PyNotion',
    version='0.0.1',
    author='Brad Hurley',
    author_email='bradley.hurley@gmail.com',
    packages=find_packages(),
    url='https://github.com/bradleyhurley/PyNotion',
    license='license.txt',
    description='Wrapper around Notion API.',
    long_description=open('ReadMe.md').read(),
    install_requires=[
        "requests >= 2.18.4"
    ],
)
