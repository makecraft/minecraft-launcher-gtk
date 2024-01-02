import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

from gi.repository import Adw, Gtk, Gio


class PreferencesView(Adw.NavigationPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_title("Preferences")

        toolbar_view = Adw.ToolbarView()

        header_bar = Adw.HeaderBar()
        header_bar.set_valign(Gtk.Align.START)
        toolbar_view.add_top_bar(header_bar)

        # region menu button
        menu_model = Gio.Menu()
        menu_model.append(label="About", detailed_action="app.about")

        menu_button = Gtk.MenuButton()
        menu_button.set_icon_name(icon_name="open-menu-symbolic")
        menu_button.set_menu_model(menu_model=menu_model)

        popover = menu_button.get_popover()
        popover.set_offset(x_offset=0, y_offset=0)

        header_bar.pack_end(menu_button)
        # endregion menu button

        # region content
        preferences_page = Adw.PreferencesPage()

        aria2_group = Adw.PreferencesGroup()
        aria2_group.set_title("Aria2")
        aria2_group.set_description(
            "Aute esse eu dolor labore elit enim ea ad mollit amet do. Elit nulla dolore laboris commodo id excepteur cupidatat nisi consequat ex."
        )

        path_entry = Adw.EntryRow()
        path_entry.set_title("Ruta")
        path_entry.set_text("aria2c")

        bc = Adw.ButtonContent()
        bc.set_icon_name("document-open-symbolic")
        bc.set_can_shrink(True)
        aria2_group.add(path_entry)

        preferences_page.add(aria2_group)

        proxy_group = Adw.PreferencesGroup()
        proxy_group.set_title("Proxy")
        proxy_group.set_description(
            "Incididunt ipsum do non nostrud eu dolor culpa irure qui id. Adipisicing ut eu esse ut proident cupidatat. Eiusmod irure consectetur aliqua dolore."
        )
        preferences_page.add(proxy_group)

        host_entry = Adw.EntryRow()
        host_entry.set_title("Host")
        proxy_group.add(host_entry)

        # region port entry
        port_entry = Adw.SpinRow()
        port_entry.set_title("Port")

        port_adjustment = Gtk.Adjustment()
        port_adjustment.set_lower(1)
        port_adjustment.set_upper(65535)
        port_adjustment.set_step_increment(1)
        port_adjustment.set_value(8000)
        port_entry.set_adjustment(port_adjustment)
        proxy_group.add(port_entry)
        # endregion port entry

        range = Gtk.Range()
        range.set_adjustment(
            Gtk.Adjustment(lower=1024, step_increment=1, upper=65535, value=8000)
        )
        proxy_group.add(range)
        # endregion content

        box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        box.append(toolbar_view)
        box.append(preferences_page)

        self.set_child(box)

    def on_previous_action(self, *args):
        pass
