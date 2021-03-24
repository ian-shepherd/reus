import setuptools

VERSION = '0.0.1'
DESCRIPTION = 'A package that allows you to pull soccer club information'
LONG_DESCRIPTION = 'A package that allows you to pull soccer club information, primarily from Transfermarkt'

setuptools.setup(
    name="reus",
    version=VERSION,
    author="Ian Shepherd",
    author_email="ian.shepherd123@gmail.com",
    url="https://github.com/ian-shepherd/reus",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages(),
    install_requires=['json', 'requests'],
    keywords=['python', 'transfermarkt', 'soccer', 'football'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)