from kivy.uix.boxlayout import BoxLayout
from kivy.app import Builder

Builder.load_file('scripts/menu.kv')


class GISQC(BoxLayout):
    def __init__(self, **kwargs):
        super(GISQC, self).__init__(**kwargs)

class DBQC(BoxLayout):
    def __init__(self, **kwargs):
        super(DBQC, self).__init__(**kwargs)