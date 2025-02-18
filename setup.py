from setuptools import setup

setup(
    name="mpljourney",
    version="0.1.0",
    packages=["mpljourney"],
    description="Datasets for matplotlib-journey.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/mpljourney",
    install_requires=["matplotlib"],
    include_package_data=True,
)
