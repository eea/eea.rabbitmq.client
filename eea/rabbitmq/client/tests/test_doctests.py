""" Doc tests
"""
import doctest
import unittest
from plone.testing import layered
from plone.app.testing import FunctionalTesting

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

def test_suite():
    """ Suite
    """
    suite = unittest.TestSuite()
    suite.addTests([
        layered(
            doctest.DocFileSuite(
                'README.txt',
                optionflags=OPTIONFLAGS,
                package='eea.rabbitmq.client'),
            layer=FUNCTIONAL_TESTING),
    ])
    return suite
