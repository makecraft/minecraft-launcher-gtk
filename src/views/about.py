import gi

gi.require_version(namespace="Gtk", version="4.0")
gi.require_version(namespace="Adw", version="1")

from gi.repository import Adw, Gio, Gtk


class AboutWindow:
    def __init__(self, parent: Adw.Window) -> None:
        dialog = Adw.AboutWindow.new()
        dialog.set_transient_for(parent=parent)
        dialog.set_application_name("Minecraft Launcher GTK")
        dialog.set_version("0.0.1")
        dialog.set_license_type(Gtk.License(Gtk.License.GPL_3_0))
        dialog.set_comments("A Minecraft Launcher using Gnome modern tecnologies")
        dialog.set_website("https://github.com/makecraft/minecraft-launcher-gtk")
        dialog.set_issue_url(
            "https://github.com/makecraft/minecraft-launcher-gtk/issues"
        )
        dialog.set_designers(["Make https://github.com/makecraft"])
        dialog.set_developers(["GHOST https://github.com/GHOSTsama2503"])
        dialog.set_application_icon("help-about-symbolic")
        dialog.present()
