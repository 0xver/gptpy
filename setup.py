from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gptpy",
    version="1.0.2",
    author="Sam Larsen",
    license="GPL-3.0-only",
    python_requires=">=3.9",
    install_requires=[requirements],
    zip_safe=False
)
