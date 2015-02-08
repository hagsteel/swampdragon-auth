import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="SwampDragon-auth",
    version="0.1.3",
    author="Jonas Hagstedt",
    author_email="hagstedt@gmail.com",
    description=("Access signed in django users in routers"),
    license="BSD",
    keywords="SwampDragon, SwampDragon-auth, auth, authentication",
    url = "https://github.com/jonashagstedt/swampdragon-auth",
    packages=['swampdragon_auth', ],
    include_package_data=True,
    long_description=read('README.md'),
    install_requires=[
        "SwampDragon"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
)
