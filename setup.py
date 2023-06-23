from setuptools import setup, find_namespace_packages


setup(
    packages=find_namespace_packages(exclude=['test']),
    include_package_data=True,
)
