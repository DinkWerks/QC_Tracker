from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

from datetime import date

from scripts.menu import PDFQC, GISQC, DBQC
from scripts.dbinterface import read, read_users, complete
from scripts.user import User

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


class ResourcesScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ResourcesScreen, self).__init__(**kwargs)
        self.menu_open = 0
        self.menu = ''
        self.data = read()
        self.user_data = read_users()
        self.load()

    def load(self):
        self.ids.rsrclist.clear_widgets()
        for rsrc in self.data:
            entry = Resource(rsrc[2], rsrc[3],
                             self.user_data[rsrc[4]][1], self.user_data[rsrc[8]][1], self.user_data[rsrc[11]][1],
                             rsrc[0]-1)
            self.ids.rsrclist.add_widget(entry)

    def write(self, ent, src):
        d = date.today()
        complete(src, User.user_id, d, self.data[ent-1][0])
        self.data = read()
        self.load()
        self.add_menu(2, ent-1)

    def clear(self, ent, src):
        pass

    def add_menu(self, menu_type, entry):
        d = self.data[entry]
        if self.menu_open == 1:
            self.remove_widget(self.menu)
        if menu_type == 1:
            self.menu = DBQC(self.user_data[d[5]][2], d[6], d[0])
        elif menu_type == 2:
            self.menu = PDFQC(self.user_data[d[8]][2], d[9], d[0])
        else:
            self.menu = GISQC(self.user_data[d[11]][2], d[12], d[15], d[16], d[17], d[18], d[19], d[20], d[0])
        self.menu_open = 1
        self.add_widget(self.menu)



class Main(App):
    def build(self):
        self.resources = ResourcesScreen()
        return self.resources

Main().run()