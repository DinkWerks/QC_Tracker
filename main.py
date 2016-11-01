from datetime import date

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from scripts.dbinterface import read, read_users, complete
from scripts.user import User

from widgets.lower3rdmenu import PDFQC, GISQC, DBQC
from widgets.recordwidget import Resource


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
        self.load()
        self.add_menu(2, ent-1)

    def clear(self, ent, src):
        pass

    def add_menu(self, menu_type, entry):
        self.data = read()
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