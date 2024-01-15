import setuptools

VERSION = "1.1.4"
DESCRIPTION = "A package that allows you to soccer information"
LONG_DESCRIPTION = """
    A package that allows you to pull soccer statistics, player market values, and
     transfer information, primarily from FBref, Fotmob, and Transfermarkt"""

setuptools.setup(
    name="reus",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="https://github.com/ian-shepherd/reus",
    author="Ian Shepherd",
    install_requires=["pandas", "numpy", "requests", "beautifulsoup4>=4.10.0"],
    keywords=["python", "fbref", "fotmob", "transfermarkt", "soccer", "football"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
)
