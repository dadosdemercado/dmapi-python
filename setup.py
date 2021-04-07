from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dmapi",
    version="1.0.0",
    author="Dados de Mercado",
    author_email="api@dadosdemercado.com",
    description="A Python client for Dados de Mercado",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dadosdemercado/dmapi-python",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
)
