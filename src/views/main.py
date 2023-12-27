import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk, Gio


class MainView(Adw.NavigationPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        toolbar_view = Adw.ToolbarView()

        header_bar = Adw.HeaderBar()
        header_bar.set_valign(Gtk.Align.START)

        # region menu button
        menu_model = Gio.Menu()
        menu_model.append(label="Preferences", detailed_action="app.preferences")
        menu_model.append(label="About", detailed_action="app.about")

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name="open-menu-symbolic")
        menu_button.set_menu_model(menu_model=menu_model)

        popover = menu_button.get_popover()
        popover.set_offset(x_offset=0, y_offset=0)

        header_bar.pack_end(child=menu_button)
        # endregion menu button

        # region avatar button
        avatar_button = Gtk.MenuButton.new()
        avatar_button.set_icon_name("avatar-default-symbolic")

        header_bar.pack_end(avatar_button)
        # endregion avatar button

        toolbar_view.set_content(header_bar)

        gio_file = Gio.File.new_for_path("assets/banner/Trails & Tales banner.jpg")

        picture = Gtk.Picture.new_for_file(file=gio_file)
        picture.set_content_fit(content_fit=Gtk.ContentFit.FILL)
        pic = Gtk.Picture(file=gio_file)

        button = Gtk.Button.new_with_label("Play")
        button.set_margin_top(300)
        button.set_margin_start(250)
        button.set_margin_end(250)
        button.add_css_class("suggested-action")

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.append(toolbar_view)
        box.append(pic)
        box.append(button)

        self.set_child(box)
