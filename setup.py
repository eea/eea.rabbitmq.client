import os
from setuptools import setup, find_packages


NAME = 'eea.rabbitmq.client'
VERSION = open('version.txt').read().strip()

setup(name=NAME,
      version=VERSION,
      description='Python rabbitmq client',
      long_description = open('README.md').read() + "\n\n" +
                         open(os.path.join("docs", "HISTORY.txt")).read(),
      author='European Environment Agency (EEA)',
      author_email='webadmin@eea.europa.eu',
      url="https://github.com/eea/eea.rabbitmq.client",
      namespace_packages=['eea', 'eea.rabbitmq'],
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      license='GPL',
      zip_safe=True,
      install_requires=[
          'pika'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,

      )
