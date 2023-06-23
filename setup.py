from setuptools import setup, find_packages


setup(
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    test_suite="tests",
)
