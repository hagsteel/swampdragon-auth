import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="SwampDragon-auth",
    version="0.1.0",
    author="Jonas Hagstedt",
    author_email="hagstedt@gmail.com",
    description=("Access signed in django users in routers"),
    license="BSD",
    keywords="SwampDragon, SwampDragon-auth, auth, authentication",
    url = "https://github.com/jonashagstedt/swampdragon-auth",
    packages=['swampdragon_auth', ],
    long_description=read('README.md'),
    install_requires=[
        "SwampDragon"
    ],
    classifiers=[
        "Development Status :: Beta",
        "Topic :: User access",
        "License :: OSI Approved :: BSD License",
    ],
)
