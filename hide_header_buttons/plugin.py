from gi.repository import GObject, Gedit, Gtk


__all__ = ["HideHeaderButtons"]


class HideHeaderButtons(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "HideHeaderButtons"

    window = GObject.Property(type=Gedit.Window)

    def do_activate(self):
        self.open_button.set_visible(False)
        self.new_tab_button.set_visible(False)
        self.save_button.set_visible(False)

    def do_deactivate(self):
        self.open_button.set_visible(True)
        self.new_tab_button.set_visible(True)
        self.save_button.set_visible(True)

    @property
    def open_button(self):
        return self.header_bar.get_children()[0]

    @property
    def new_tab_button(self):
        return self.header_bar.get_children()[1]

    @property
    def save_button(self):
        return self.header_bar.get_children()[3]

    @property
    def header_bar(self):
        return self.window.get_titlebar().get_children()[-1]
