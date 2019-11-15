import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ikakao",
    version="0.0.5",
    description="Kakao i Open Builder SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hanjun Kim",
    author_email="hallazzang@gmail.com",
    python_requires=">=3.6",
    url="https://github.com/hallazzang/ikakao",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
    ],
)

