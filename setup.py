from setuptools import setup, find_packages


setup(
    packages=find_packages(exclude=['test']) + ['src/pca/scripts'],
    include_package_data=True,
)
