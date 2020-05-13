""" SetupHandlers
"""
from Products.CMFQuickInstallerTool import interfaces as QuickInstaller
from zope.interface import implementer


@implementer(QuickInstaller.INonInstallable)
class HiddenProducts(object):
    """ HiddenProducts
    """

    def getNonInstallableProducts(self):
        """Do not show on QuickInstaller's list of installable products."""
        return [
            'eea.rabbitmq.client'
        ]
