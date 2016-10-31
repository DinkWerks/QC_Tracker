from kivy.uix.boxlayout import BoxLayout
from kivy.app import Builder
from kivy.properties import NumericProperty, StringProperty
from scripts.dbinterface import update_gis, update_gis_text, read

Builder.load_file('scripts/menu.kv')


class DBQC(BoxLayout):
    user = StringProperty('')
    date = StringProperty('')

    def __init__(self, user, date, entry, **kwargs):
        super(DBQC, self).__init__(**kwargs)
        self.user = user
        self.date = date
        self.entry = entry

    def complete(self):
        self.parent.write(self.entry, 'DB')


class PDFQC(BoxLayout):
    user = StringProperty('')
    date = StringProperty('')

    def __init__(self, user, date, entry, **kwargs):
        super(PDFQC, self).__init__(**kwargs)
        self.user = user
        self.date = date
        self.entry = entry

    def complete(self):
        self.parent.write(self.entry, 'PDF')


class GISQC(BoxLayout):
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
        self.parent.data = read()

    def update_note(self, text):
        #  This line throws errors at when creating the menu class.
        #  It is being called when the grid is being placed into the layout, and before self.parent has been established.
        #  I need to either move updating to a separate class, or learn to postpone the call to re-read until after the textbox is placed.
        #  This happens here, and not during the checkboxes, because they are drawn after the grid layout is added.
        print self.parent
        update_gis_text(text, self.entry)

    def complete(self):
        self.parent.write(self.entry, 'GIS')
