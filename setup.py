from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.read()

setup(
    name="coronastatisticvkapi",
    version="1.0",
    description="Monitoring COVID-19 statistics",
    package_dir={"":""},
    packages=find_packages(where=""),
    long_description=long_description,
    url="https://github.com/CoffeeSi/coronastatisticvkapi/",
    author="CoffeeSi",
    author_email="ewgenik02032006@gmail.com",
    license="MIT",
    classifiers=[
        "LICENSE :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8.2",
        "Operating System :: Windows"
    ],
    install_requires=requirements,
    python_requires=">=3.8.2",
)
