import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def read_file(fname) -> str:
    with open(fname, encoding='utf-8') as f:
        return f.read()


setuptools.setup(
    name="open_fun_nas", 
    version="1",
    author="chomes/NetRunner",
    author_email="jaayjay@gmail.com",
    description="Python/Ansible based NAS server management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chomes/open_fun_nas",
    packages=setuptools.find_packages(exclude=["test*"]),
    install_requires=[

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)