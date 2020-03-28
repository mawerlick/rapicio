import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rapicio", # Replace with your own username
    version="0.1.5",
    author="Alperen Yalçın - M. Salim Turgut",
    author_email="alpyalcin9@gmail.com",
    description="Rapicio package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mawerlick/rapicio",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
)
