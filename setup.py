# -*- coding:utf-8 -*-

from setuptools import setup

setup(name='logxstract',
      version='0.1.1',
      packages=['logxstract'],
      entry_points={
          'console_scripts': [
              'logxstract = logxstract.__main__:main'
          ]
      })
