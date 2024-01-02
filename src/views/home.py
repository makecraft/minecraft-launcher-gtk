import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk, Gio


class HomeView(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing(0)

        gio_file = Gio.File.new_for_path("assets/banner/Trails & Tales banner.jpg")

        picture = Gtk.Picture.new_for_file(file=gio_file)
        picture.set_content_fit(content_fit=Gtk.ContentFit.FILL)
        pic = Gtk.Picture(file=gio_file)
        self.append(pic)

        play_button = Gtk.Button.new_with_label("Play")
        play_button.set_margin_top(300)
        play_button.set_margin_start(250)
        play_button.set_margin_end(250)
        play_button.add_css_class("pill")
        play_button.add_css_class("suggested-action")
        self.append(play_button)
