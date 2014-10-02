import datetime

from DateTime.DateTime import DateTime
from zope.interface import Interface
from zope.component import adapts
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from z3c.form import field
from z3c.form.browser.radio import RadioFieldWidget

from plone.supermodel import model
from plone.formwidget.datetime.z3cform.widget import DateFieldWidget
from plone.app.users.browser.account import AccountPanelSchemaAdapter
from plone.app.users.browser.userdatapanel import UserDataPanel
from plone.app.users.browser.register import RegistrationForm, AddUserForm
from plone.z3cform.fieldsets import extensible

from collective.examples.userdata.interfaces import IUserDataExamplesLayer
from collective.examples.userdata import _





def validateAccept(value):
    if value is not True:
        return False
    return True


class IEnhancedUserDataSchema(model.Schema):
    """Use all the fields from the default user data schema, and add various
    extra fields.
    """
    
    privacy = schema.Bool(
        title=_(u'label_accept', default=u'Autorizzazione al trattamento dei dati personali'),
        description=_(u'help_accept',
                      default=u"Autorizzazione rilasciata ai sensi dell'art.13 del Decreto Legislativo \"Codice in materia del trattamento dei dati personali\""),
        required=True,
        constraint=validateAccept,
        )


class EnhancedUserDataSchemaAdapter(AccountPanelSchemaAdapter):
    schema = IEnhancedUserDataSchema

    def get_birthdate(self):
        bd = self._getProperty('birthdate')
        return None if bd == '' else bd.asdatetime().date()

    def set_birthdate(self, value):
        return self._setProperty('birthdate',
            DateTime(datetime.datetime(value.year, value.month, value.day,
                                       0, 0)))

    birthdate = property(get_birthdate, set_birthdate)


class UserDataPanelExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, UserDataPanel)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        fields = fields.omit('privacy')  # Users have already accepted.
        
        self.add(fields)


class RegistrationPanelExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, RegistrationForm)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        self.add(fields)


class AddUserFormExtender(extensible.FormExtender):
    adapts(Interface, IUserDataExamplesLayer, AddUserForm)

    def update(self):
        fields = field.Fields(IEnhancedUserDataSchema)
        # management form doesn't need this field
        fields = fields.omit('privacy')
        self.add(fields)
