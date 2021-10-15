from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires=">=3.6",
    test_suite='tests',
    packages=find_packages())