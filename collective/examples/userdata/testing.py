from plone.app.testing import PloneSandboxLayer, PLONE_FIXTURE, applyProfile
from plone.app.testing import TEST_USER_NAME, TEST_USER_PASSWORD
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing.layers import IntegrationTesting
from plone.testing import z2
from zope.configuration import xmlconfig

import unittest2 as unittest


class EnhancedUserdata(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # load ZCML
        import plone.formwidget.namedfile
        import collective.examples.userdata
        xmlconfig.file(
            'configure.zcml',
            collective.examples.userdata,
            context=configurationContext,
        )
        xmlconfig.file(
            'configure.zcml',
            plone.formwidget.namedfile,
            context=configurationContext,
        )

    def setUpPloneSite(self, portal):
        # install into the Plone site
        applyProfile(portal, 'collective.examples.userdata:default')


class IntegrationTestCase(unittest.TestCase):
    layer = IntegrationTesting(
        bases=(EnhancedUserdata(),),
        name="EnhancedUserdata:Functional",
    )


class FunctionalTestCase(unittest.TestCase):
    layer = FunctionalTesting(
        bases=(EnhancedUserdata(),),
        name="EnhancedUserdata:Functional",
    )

    def getBrowser(self, url=None):
        portal = self.layer['portal']
        browser = z2.Browser(self.layer['app'])
        browser.handleErrors = False
        browser.addHeader('Authorization',
                          'Basic %s:%s' % (TEST_USER_NAME, TEST_USER_PASSWORD))
        if url:
            browser.open(portal.absolute_url() + url)
        return browser
