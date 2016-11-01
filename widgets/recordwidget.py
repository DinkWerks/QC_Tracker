from kivy.app import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

Builder.load_file('widgets/recordwidget.kv')


class Resource(BoxLayout):
    primary = StringProperty('')
    trinomial = StringProperty('')
    rc = ObjectProperty('')
    dc = ObjectProperty('')
    gc = ObjectProperty('')

    def __init__(self, primary, trinomial, rc, dc, gc, entry, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.primary = primary
        self.trinomial = trinomial
        self.rc = rc
        self.dc = dc
        self.gc = gc
        self.entry = entry

    def callmenu(self, source):
        self.parent.parent.parent.parent.add_menu(source, self.entry)