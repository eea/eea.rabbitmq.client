""" Installer
"""
import os
from setuptools import setup, find_packages

NAME = 'eea.rabbitmq.client'
PATH = NAME.split('.') + ['version.txt']
VERSION = open(os.path.join(*PATH)).read().strip()

setup(name=NAME,
      version=VERSION,
      description='Python RabbitMQ client',
      long_description = open('README.rst').read() + "\n\n" +
                         open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Framework :: Zope2",
          "Framework :: Zope3",
          "Framework :: Plone",
          "Framework :: Plone :: 4.3",
          "Programming Language :: Zope",
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)",
        ],
      keywords='eea RabbitMQ plone zope python',
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
