from plone.app.users.userdataschema import IUserDataSchema
from plone.app.users.userdataschema import IUserDataSchemaProvider
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.interface import implements
from collective.examples.userdata import _


codfis_options = SimpleVocabulary([
    SimpleTerm(value='Male', title=_(u'Male')),
    SimpleTerm(value='Female', title=_(u'Female')),
    ])

def validateAccept(value):
    if not value == True:
        return False
    return True

class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema

class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """
    nome = schema.TextLine(
        title=_(u'label_nome', default=u'Nome'),
        description=_(u'help_nome',
                      default=u"Indicare il nome."),
        required=False,
        )
    cognome = schema.TextLine(
        title=_(u'label_cognome', default=u'Cognome'),
        description=_(u'help_cognome',
                      default=u"Indicare il cognome."),
        required=False,
        )
    ragionesociale = schema.TextLine(
        title=_(u'label_ragionesociale', default=u'Ragione sociale'),
        description=_(u'help_ragionesociale',
                      default=u"Indicare la ragione sociale delle ditta come compare nella registrazione in Camera di Commercio."),
        required=False,
        )
    codfis = schema.TextLine(
        title=_(u'label_codfis', default=u'Codice Fiscale'),
        description=_(u'help_codfis',
                      default=u"Indicare il codice fiscale."),
        required=False,
        )
    piva = schema.TextLine(
        title=_(u'label_piva', default=u'Partita IVA'),
        description=_(u'help_piva',
                      default=u"Indicare la partita iva."),
        required=False,
        )
    indirizzo = schema.TextLine(
        title=_(u'label_indirizzo', default=u'Sede legale azienda'),
        description=_(u'help_indirizzo',
                      default=u"Indicare l'indirizzo della sede legale."),
        required=False,
        )
    comune = schema.TextLine(
        title=_(u'label_comune', default=u'Comune'),
        description=_(u'help_comune',
                      default=u"Indicare il Comune della sede legale."),
        required=False,
        )
    provincia = schema.TextLine(
        title=_(u'label_provincia', default=u'Provincia'),
        description=_(u'help_provincia',
                      default=u"Indicare la Provincia della sede legale."),
        required=False,
        )
    telefono = schema.TextLine(
        title=_(u'label_telefono', default=u'Telefono/Cell'),
        description=_(u'help_telefono',
                      default=u"Indicare un recapito telefonico."),
        required=False,
        )
    cap = schema.TextLine(
        title=_(u'label_cap', default=u'CAP'),
        description=_(u'help_cap',
                      default=u"Indicare il CAP."),
        required=False,
        )    
    pec = schema.TextLine(
        title=_(u'label_pec', default=u'PEC'),
        description=_(u'help_pec',
                      default=u"Indicare un indirizzo di posta elettronica certificato."),
        required=False,
        )