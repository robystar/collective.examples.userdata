Introduction
============

With Plone 5, the registration and personal information forms are z3c.form_ forms.
These can be extended to allow any additional data to be collected on the forms.

This product aims to show how you could extend or modify the default schema
provided by plone.app.users_, and add new fields to the registration form.

If you are using a Plone version previous to Plone 5, then you need to look at the older version of
`collective.examples.userdata here <https://pypi.python.org/pypi/collective.examples.userdata/0.4>`__.

Note for upgraders
------------------

Previously, your ``IEnhancedUserDataSchema`` was registered via. a
``IUserDataSchemaProvider`` utility you registered in
``componentregistry.xml``. If this is something you did, then be sure to remove
this utility, ideally before upgrading. 
`wildcard.fixpersistentutilities <https://pypi.python.org/pypi/wildcard.fixpersistentutilities/>`__
could help here.

Adding custom userdata fields
-----------------------------

The code below is snippets from the source code from the package. Look there to
see more examples.

Creating a schema
~~~~~~~~~~~~~~~~~

We create a schema for our fields in the same manner as any other schema::

    class IEnhancedUserDataSchema(model.Schema):
        country = schema.TextLine(
            title=_(u'label_country', default=u'Country'),
            description=_(u'help_country',
                          default=u"Fill in the country you live in."),
            required=False,
            )

Extending the userdata form
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add this schema to the form, we need to define a form extender for
``UserDataPanel`` which allows us to register any new fields we want to::

    class UserDataPanelExtender(extensible.FormExtender):
        adapts(Interface, IDefaultBrowserLayer, UserDataPanel)
        def update(self):
            fields = field.Fields(IEnhancedUserDataSchema)
            fields = fields.omit('accept') # Users have already accepted.
            self.add(fields)

And register this in configure.zcml::

    <adapter
      factory=".userdataschema.UserDataPanelExtender"
      provides="plone.z3cform.fieldsets.interfaces.IFormExtender" />

Storing / retrieving custom fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To store the values alongside default fields, we need to add fields to
``profiles/default/memberdata_properties.xml``. For example::

    <?xml version="1.0"?>
    <object name="portal_memberdata" meta_type="Plone Memberdata Tool">
      <property name="country" type="string"></property>
    </object>

We don't define the "accept" field here, since that is only for signup.
They have to have accepted to have a user in the system.

Before values can be read and written by the form, there needs to be a data
manager to fetch the values. The default manager will read/write any field
defined in the schema, so most of the work is done for you::

    from plone.app.users.browser.account import AccountPanelSchemaAdapter

    class EnhancedUserDataSchemaAdapter(AccountPanelSchemaAdapter):
        schema = IEnhancedUserDataSchema

If you want to do something different, add a property for that field to
override the default behavior. The source code shows this for the ``birthdate``
field.

Finally, register the data manager in ZCML::

    <adapter
      provides=".userdataschema.IEnhancedUserDataSchema"
      for="plone.app.layout.navigation.interfaces.INavigationRoot"
      factory=".adapter.EnhancedUserDataSchemaAdapter"
      />

Extending the registration form
-------------------------------

To extend the registration form, you have 2 choices. Either using the
@@member-registration view to manipulate which of the default fields are
visible, or for full control you can register another form extender.

Defining registration field FormExtenders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Registering an extender for ``BaseRegistrationForm`` will allow us to add
fields at any point to the registration form. This is done in the same way
as before::

    class RegistrationPanelExtender(extensible.FormExtender):
        adapts(Interface, IDefaultBrowserLayer, BaseRegistrationForm)
        def update(self):
            fields = field.Fields(IEnhancedUserDataSchema)
            #NB: Not omitting the accept field this time, we want people to check it
            self.add(fields)

And register this in configure.zcml::

    <adapter
      factory=".userdataschema.RegistrationPanelExtender"
      provides="plone.z3cform.fieldsets.interfaces.IFormExtender" />

The data manager is attached to the schema, so will be shared with the user
data form. If we used a different schema, then we would have to define another
data manager too.

Various other field examples
----------------------------

There are various other extra fields with which you could extend your users'
profile. In ``userdataschema.py`` you will find examples for:

- a Date field (``birthdate``)
- a Boolean field (``newsletter``)
- a Choice field (``gender``)

The "Accept Terms" field
~~~~~~~~~~~~~~~~~~~~~~~~

A special case is the ``accept`` field. This is a Boolean field which is
required for signup. We implement it by adding a ``constraint`` to the schema::

    def validateAccept(value):
        if not value == True:
            return False
        return True

    class IEnhancedUserDataSchema(IUserDataSchema):
        # ...
        accept = schema.Bool(
            title=_(u'label_accept', default=u'Accept terms of use'),
            description=_(u'help_accept',
                          default=u"Tick this box to indicate that you have found,"
                          " read and accepted the terms of use for this site. "),
            required=True,
            constraint=validateAccept,
            )

Because this field can be ignored once registration is complete, we don't add
it to the memberdata properties. We also hide it from the userdata forms.

.. _plone.app.users: http://pypi.python.org/pypi/plone.app.users
.. _z3c.form: https://pypi.python.org/pypi/z3c.form
