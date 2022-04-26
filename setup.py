import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jacob_karlstrom",
    version="0.0.1",
    author="jacob_karlstrom",
    author_email="jacob.karlstrom@gmail.com",
    description="A small sriq package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fattigman/pySRIQ",
    project_urls={
        "Bug Tracker": "https://github.com/Fattigman/pySRIQ/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
