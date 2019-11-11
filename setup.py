import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Encountertk", 
    version="0.0.1",
    author="Bennett Lambert",
    author_email="lambertb@uw.edu",
    description="Encounter rate modelling in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lambertsbennett/Encountertk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intented Audience :: Scientists",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
)