import sys
import typing

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio


import views


class MainWindow(Adw.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(800, 600)
        self.set_size_request(600, 400)

        self.set_content(views.MainView())


class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # region actions
        self.create_action("preferences", self.on_preferences)
        self.create_action("about", self.on_about_action)
        # endregion actions

        self.connect("activate", self.on_activate)

    def create_action(self, name: str, callback: typing.Callable):
        action = Gio.SimpleAction.new(name=name)
        action.connect("activate", callback)
        self.add_action(action=action)

    def on_activate(self, app):
        self.window = MainWindow(application=app)
        self.window.present()

    def on_preferences(self, *args):
        self.window.set_content(views.PreferencesView())

    def on_about_action(self, *args):
        views.AboutWindow(self.window)


def main():
    app = App(application_id="com.github.makecraft.minecraft-launcher-gtk")
    app.run(sys.argv)


if __name__ == "__main__":
    main()
