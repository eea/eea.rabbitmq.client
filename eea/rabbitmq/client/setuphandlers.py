""" SetupHandlers
"""
from Products.CMFQuickInstallerTool import interfaces as QuickInstaller
from zope.interface import implements


class HiddenProducts(object):
    """ HiddenProducts
    """

    implements(QuickInstaller.INonInstallable)

    def getNonInstallableProducts(self):
        """Do not show on QuickInstaller's list of installable products."""
        return [
            'eea.rabbitmq.client'
        ]
