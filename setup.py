import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

NAME = 'eea.rabbitmq.client'
VERSION = open('version.txt').read().strip()

setup(name=NAME,
      version=VERSION,
      description='Python rabbitmq client',
      long_description = open('README.md').read() + "\n\n" +
                         open(os.path.join("docs", "HISTORY.txt")).read(),
      author='European Environment Agency (EEA)',
      author_email='webadmin@eea.europa.eu',
      url="https://github.com/eea/eee.rabbitmq.client",
      license='GPL',
      )
