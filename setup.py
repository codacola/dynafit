import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynafit-codacola",
    version="0.1",
    author="Florian Helmhold",
    author_email="florian.helmhold@uni-tuebingen.de",
    description="Fit dynamical models to traces of system states",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codacola/dynafit",
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy',
        'scipy',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
