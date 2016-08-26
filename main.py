from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

from scripts.menu import GISQC, DBQC

data = [['p-01-001', 'BUT-001', 'a', 'b', 'c'], ['p-01-002', 'BUT-002', 'x', 'y', 'z']]


class Resource(BoxLayout):
    primary = StringProperty('')
    trinomial = StringProperty('')
    rc = StringProperty('')
    dc = StringProperty('')
    gc = StringProperty('')

    def __init__(self, primary, trinomial, rc, dc, gc, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.primary = primary
        self.trinomial = trinomial
        self.rc = rc
        self.dc = dc
        self.gc = gc

    def callmenu(self, source):
        self.parent.parent.parent.parent.add_menu(source)


class ResourcesScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ResourcesScreen, self).__init__(**kwargs)
        self.menu_open = 0
        self.menu = GISQC()
        self.load()

    def load(self):
        for rsrc in data:
            entry = Resource(rsrc[0], rsrc[1], rsrc[2], rsrc[3], rsrc[4])
            self.ids.rsrclist.add_widget(entry)

    def add_menu(self, menu_type):
        if self.menu_open == 1:
            self.remove_widget(self.menu)
        # Insert IF statement to change self.menu's class depending on menu type here.
        if menu_type == 1:
            pass
        elif menu_type == 2:
            self.menu = DBQC()
        else:
            self.menu = GISQC()
        self.menu_open = 1
        self.add_widget(self.menu)



class Main(App):
    def build(self):
        self.resources = ResourcesScreen()
        return self.resources

Main().run()