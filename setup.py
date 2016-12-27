#coding=utf-8
import os
from setuptools import setup


setup(
    name="redis-cache",
    version="0.1",
    author="Alexander Kuts",
    author_email="redrush85@gmail.com",
    description="redis-cache is a pythonic interface for creating a cache over redis. "
                "It provides simple decorators that can be added to any function to cache its return values. ",
    license="MIT",
    keywords=["redis", "cache", "decorator"],
    url="https://github.com/redrush85/redis-cache",
    download_url='https://github.com/redrush85/redis-cache',
    packages=['redis_cache'],
    install_requires=["redis>=2.7.1"],
    classifiers=[],
)