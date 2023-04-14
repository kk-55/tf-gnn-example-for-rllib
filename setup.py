from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tfgnn-rllib",
    version="0.0.1",
    author="Klaus Kuchler",
    author_email="klausk55@hotmail.de",
    description="TF-GNN example for RLlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kk-55/tf-gnn-example-for-rllib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=find_packages(include=["tfgnn_rllib", "tfgnn_rllib.*"]),
    python_requires=">=3.8",
    install_requires=[
        "ray[default]", "ray[air]" ,"ray[tune]", "ray[rllib]", "ray[serve]",
        "tensorflow<2.11", "tensorflow_gnn"
    ],
)