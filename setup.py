from setuptools import setup, find_packages


setup(
    # @TODO to evade warning when running "python -m build", the ["pca.scripts"] package was added
    packages = find_packages(exclude=["test"]) + ["pca.scripts"],
    include_package_data=True,
)
