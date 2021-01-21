import re
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("enamel/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setuptools.setup(
    name="enamelware", 
    version=version,
    author="John Allen",
    author_email="allen.john.e@gmail.com",
    description="Enamelware - a simple application framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sinoia",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

