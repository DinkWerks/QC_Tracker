from kivy.uix.boxlayout import BoxLayout
from kivy.app import Builder
from kivy.properties import NumericProperty, StringProperty
from scripts.dbinterface import update_gis, update_gis_text, read


Builder.load_file('widgets/menu.kv')

class Lower3rdMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(Lower3rdMenu, self).__init__(**kwargs)

    def complete(self):
        self.parent.write(self.entry, self.menu_type)

    def update_data(self):
       self.parent.data = read()

class DBQC(Lower3rdMenu):
    user = StringProperty('')
    date = StringProperty('')

    def __init__(self, user, date, entry, **kwargs):
        super(DBQC, self).__init__(**kwargs)
        self.user = user
        self.date = date
        self.entry = entry
        self.menu_type = 'DB'


class PDFQC(Lower3rdMenu):
    user = StringProperty('')
    date = StringProperty('')

    def __init__(self, user, date, entry, **kwargs):
        super(PDFQC, self).__init__(**kwargs)
        self.user = user
        self.date = date
        self.entry = entry
        self.menu_type = 'PDF'


class GISQC(Lower3rdMenu):
    user = StringProperty('')
    date = StringProperty('')
    feature_size = NumericProperty(0)
    shape = NumericProperty(0)
    location = NumericProperty(0)
    duplicate = NumericProperty(0)
    other = NumericProperty(0)
    note = StringProperty('')
    entry = NumericProperty(0)

    def __init__(self, user, date, feature_size, shape, location, duplicate, other, note, entry, **kwargs):
        super(GISQC, self).__init__(**kwargs)
        self.user = user
        self.date = date
        self.feature_size = feature_size  # self.size would shadow the Kivy widget variable size
        self.shape = shape
        self.location = location
        self.duplicate = duplicate
        self.other = other
        self.note = note
        self.entry = entry
        self.menu_type = 'GIS'


    def update(self, source):
        variable_dicts = {'GISSizeINC': self.feature_size, 'GISShapeINC': self.shape, 'GISLocINC': self.location,
                          'GISDupe': self.duplicate, 'GISOther': self.other}
        value = variable_dicts[source]
        if value == 1:
            variable_dicts[source] = 0
            value = 0
        else:
            variable_dicts[source] = 1
            value = 1
        update_gis(source, value, self.entry)
        self.update_data()

    def update_note(self, text):
        update_gis_text(text, self.entry)

