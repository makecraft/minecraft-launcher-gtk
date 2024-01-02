import sys
import typing

import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gio, Gtk


import views
import navigation


class MainView(Adw.NavigationPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        toolbar_view = Adw.ToolbarView()
        self.set_child(toolbar_view)

        header_bar = Adw.HeaderBar()
        toolbar_view.add_top_bar(header_bar)

        # region view switcher
        view_stack = Adw.ViewStack()
        toolbar_view.set_content(view_stack)

        view_stack.add_titled_with_icon(
            child=views.InstancesView(),
            name="instances_view",
            title="Instances",
            icon_name="view-grid-symbolic",
        )

        view_stack.add_titled_with_icon(
            child=views.HomeView(),
            name="home",
            title="Home",
            icon_name="user-home-symbolic",
        )

        mods_view = Gtk.Box()
        view_stack.add_titled_with_icon(
            child=mods_view,
            name="mods",
            title="Mods",
            icon_name="application-x-addon-symbolic",
        )

        view_stack.set_visible_child_name("home")

        view_switcher = Adw.ViewSwitcher()
        view_switcher.set_stack(view_stack)
        view_switcher.set_policy(Adw.ViewSwitcherPolicy.WIDE)
        header_bar.set_title_widget(view_switcher)
        # endregion view switcher

        # region avatar button
        avatar_button = Gtk.Button()
        avatar_button.set_icon_name("avatar-default-symbolic")
        avatar_button.connect("clicked", self.on_avatar_action)
        header_bar.pack_end(avatar_button)
        # endregion avatar button

        # region menu button
        menu_model = Gio.Menu()
        menu_model.append(label="Preferences", detailed_action="app.preferences")
        menu_model.append(label="About", detailed_action="app.about")

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name="open-menu-symbolic")
        menu_button.set_menu_model(menu_model=menu_model)

        popover = menu_button.get_popover()
        popover.set_offset(x_offset=0, y_offset=0)

        header_bar.pack_end(menu_button)
        # endregion menu button

    def on_avatar_action(self, *args):
        views.AvatarView().present()


class MainWindow(Adw.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(800, 600)
        self.set_size_request(400, 200)

        self.set_icon_name("minecraft-launcher")

        navigation.stack.add(MainView())
        navigation.stack.add(views.PreferencesView())
        self.set_content(navigation.stack)


class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # fix unsupported gtk-application-prefer-dark-theme
        style_manager = self.get_style_manager()
        style_manager.set_color_scheme(Adw.ColorScheme.PREFER_DARK)

        # region actions
        self.create_action("preferences", self.on_preferences_action)
        self.create_action("about", self.on_about_action)
        # endregion actions

        self.connect("activate", self.on_activate)

    def create_action(self, name: str, callback: typing.Callable):
        action = Gio.SimpleAction(name=name)
        action.connect("activate", callback)
        self.add_action(action=action)

    def on_activate(self, app):
        self.window = MainWindow(application=app)
        self.window.present()

    def on_main_action(self, *args):
        self.window.set_content(views.HomeView())

    def on_preferences_action(self, *args):
        navigation.stack.push(views.PreferencesView())

    def on_about_action(self, *args):
        views.AboutWindow(self.window)


def main():
    app = App(application_id="com.github.makecraft.minecraft-launcher-gtk")
    app.run(sys.argv)


if __name__ == "__main__":
    main()
