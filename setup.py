from setuptools import setup
def readme():
    with open('Readme.Md') as f:
        README = f.read()
    return README


setup(
    name="techyshiv-evenodd",
    version="1.0.1",
    description="A Python package to Check Even and Odd for any given numbers or list and return True , False & list based on data type provided",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/techyshiv/Python-Package",
    author="Shivang Saxena",
    author_email="shivangsaxena177@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["techyshiv_evenodd"],
    include_package_data=True,
    install_requires=[]
)