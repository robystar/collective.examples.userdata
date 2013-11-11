from zope.interface import Interface
from zope.component import adapts
from zope import schema

from z3c.form import field
from z3c.form.browser.radio import RadioFieldWidget

from plone.supermodel import model
from plone.app.users.browser.personalpreferences import UserDataPanel
from plone.app.users.browser.register import RegistrationForm, AddUserForm
from plone.z3cform.fieldsets import extensible

from collective.examples.userdata import _
from collective.examples.userdata.interfaces import IUserDataExamplesLayer


def validateAccept(value):
    if not value == True:
        return False
    return True

class IEnhancedUserDataSchema(model.Schema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    firstname = schema.TextLine(
        title=_(u'label_firstname', default=u'First name'),
        description=_(u'help_firstname',
                      default=u"Fill in your given name."),
        required=False,
        )
    lastname = schema.TextLine(
        title=_(u'label_lastname', default=u'Last name'),
        description=_(u'help_lastname',
                      default=u"Fill in your surname or your family name."),
        required=False,
        )
    gender = schema.Choice(
        title=_(u'label_gender', default=u'Gender'),
        description=_(u'help_gender',
                      default=u"Are you a girl or a boy?"),
        values = [u'Male', u'Female'],
        required=True,
        )
    birthdate = schema.Date(
        title=_(u'label_birthdate', default=u'Birthdate'),
        description=_(u'help_birthdate',
            default=u'Your date of birth, in the format dd-mm-yyyy'),
        required=False,
        )
    city = schema.TextLine(
        title=_(u'label_city', default=u'City'),
        description=_(u'help_city',
                      default=u"Fill in the city you live in."),
        required=False,
        )
    country = schema.TextLine(
        title=_(u'label_country', default=u'Country'),
        description=_(u'help_country',
                      default=u"Fill in the country you live in."),
        required=False,
        )
    phone = schema.TextLine(
        title=_(u'label_phone', default=u'Telephone number'),
        description=_(u'help_phone',
                      default=u"Leave your phone number so we can reach you."),
        required=False,
        )
    newsletter = schema.Bool(
        title=_(u'label_newsletter', default=u'Subscribe to newsletter'),
        description=_(u'help_newsletter',
                      default=u"If you tick this box, we'll subscribe you to "
                        "our newsletter."),
        required=False,
        )
    accept = schema.Bool(
        title=_(u'label_accept', default=u'Accept terms of use'),
        description=_(u'help_accept',
                      default=u"Tick this box to indicate that you have found,"
                      " read and accepted the terms of use for this site. "),
        required=True,
        constraint=validateAccept,
        )

class UserDataPanelExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, UserDataPanel)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        fields = fields.omit('accept') # Users have already accepted.
        fields['gender'].widgetFactory = RadioFieldWidget
        self.add(fields, prefix="IEnhancedUserDataSchema")

class RegistrationPanelExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, RegistrationForm)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        fields['gender'].widgetFactory = RadioFieldWidget
        self.add(fields, prefix="IEnhancedUserDataSchema")

class AddUserFormExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, AddUserForm)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        fields['gender'].widgetFactory = RadioFieldWidget
        fields = fields.omit('accept') # management form doesn't need this field
        self.add(fields, prefix="IEnhancedUserDataSchema")
