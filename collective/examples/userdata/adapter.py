from plone.app.users.browser.personalpreferences import UserDataPanelAdapter


class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_nome(self):
        return self.context.getProperty('nome', '')
    def set_nome(self, value):
        return self.context.setMemberProperties({'nome': value})
    nome = property(get_nome, set_nome)
    def get_cognome(self):
        return self.context.getProperty('cognome', '')
    def set_cognome(self, value):
        return self.context.setMemberProperties({'cognome': value})
    cognome = property(get_cognome, set_cognome)
    def get_ragionesociale(self):
        return self.context.getProperty('ragionesociale', '')
    def set_ragionesociale(self, value):
        return self.context.setMemberProperties({'ragionesociale': value})
    ragionesociale = property(get_ragionesociale, set_ragionesociale)
    def get_piva(self):
        return self.context.getProperty('piva', '')
    def set_piva(self, value):
        return self.context.setMemberProperties({'piva': value})
    piva = property(get_piva, set_piva)
    def get_codfis(self):
        return self.context.getProperty('codfis', '')
    def set_codfis(self, value):
        return self.context.setMemberProperties({'codfis': value})
    codfis = property(get_codfis, set_codfis)
    def get_indirizzo(self):
        return self.context.getProperty('indirizzo', '')
    def set_indirizzo(self, value):
        return self.context.setMemberProperties({'indirizzo': value})
    indirizzo = property(get_indirizzo, set_indirizzo)
    def get_comune(self):
        return self.context.getProperty('comune', '')
    def set_comune(self, value):
        return self.context.setMemberProperties({'comune': value})
    comune = property(get_comune, set_comune)
    def get_provincia(self):
        return self.context.getProperty('provincia', '')
    def set_provincia(self, value):
        return self.context.setMemberProperties({'provincia': value})
    provincia = property(get_provincia, set_provincia)
    def get_cap(self):
        return self.context.getProperty('cap', '')
    def set_cap(self, value):
        return self.context.setMemberProperties({'cap': value})
    cap = property(get_cap, set_cap)    
    def get_telefono(self):
        return self.context.getProperty('telefono', '')
    def set_telefono(self, value):
        return self.context.setMemberProperties({'telefono': value})
    telefono = property(get_telefono, set_telefono)
    def get_pec(self):
        return self.context.getProperty('pec', '')
    def set_pec(self, value):
        return self.context.setMemberProperties({'pec': value})
    pec = property(get_pec, set_pec)
