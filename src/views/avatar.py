import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio, Gtk


class AvatarView(Adw.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        box = Gtk.Box()
        box.set_orientation(Gtk.Orientation.VERTICAL)
        box.set_spacing(16)
        box.set_margin_top(16)
        box.set_margin_end(16)
        box.set_margin_bottom(16)
        box.set_margin_start(16)

        buttons_box = Gtk.Box()
        buttons_box.set_orientation(Gtk.Orientation.HORIZONTAL)
        buttons_box.set_halign(Gtk.Align.END)
        buttons_box.set_spacing(10)

        username_entry = Adw.EntryRow()
        username_entry.set_title("Username")

        cancel_button = Gtk.Button()
        cancel_button.set_label("Cancel")
        cancel_button.connect("clicked", self.on_cancell)
        cancel_button.add_css_class("popup")
        buttons_box.append(cancel_button)

        ok_button = Gtk.Button()
        ok_button.set_label("OK")
        ok_button.connect("clicked", self.on_ok)
        ok_button.add_css_class("suggested-action")
        ok_button.add_css_class("popup")
        buttons_box.append(ok_button)

        box.append(username_entry)
        box.append(buttons_box)

        self.set_content(box)

    def on_ok(self, *args):
        self.close()

    def on_cancell(self, *args):
        self.close()
