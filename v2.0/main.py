#!/usr/bin/env python3
import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gdk

class Page(Gtk.Box):
    def __init__(self, back_label):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.back_button = Gtk.Button(label=back_label)
        self.back_button.connect("clicked", self.go_back)
        self.append(self.back_button)

    def go_back(self, button):
        main_window = self.get_root()
        main_window.stack.set_visible_child_name("main_page")

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stack = Gtk.Stack()
        self.set_child(self.stack)

        # Main Page
        self.grid = Gtk.Grid()
        self.stack.add_named(self.grid, "main_page")

        # Buttons and pages
        buttons = ["Cyber Tools", "Training Platforms", "CTF Platforms", "Job Calendars", "Research & Discovery","Cyber Frauds","Student Development Kit","Events & Entertainments","Feedback"]
        for i, button in enumerate(buttons):
            btn = Gtk.Button(label=button)
            btn.get_style_context().add_class("circular")  # Apply CSS class for circular shape
            btn.connect("clicked", self.open_page, button)
            self.grid.attach(btn, i % 3, i // 3, 1, 1)  # Arrange buttons in a 3-column grid

            # Set a fixed size for the buttons
            btn.set_size_request(200, 200)

            # Configure button properties to expand and shrink with window
            btn.set_hexpand(True)
            btn.set_vexpand(True)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)

            page = Page("Go back from " + button)
            self.stack.add_named(page, button)

    def open_page(self, button, page_name):
        button.get_style_context().add_class('clicked')
        self.stack.set_visible_child_name(page_name)

class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate',self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app, title="Cyber City")
        self.win.present()

        # Add the following code to load the CSS file:
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('style.css')
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

if __name__ == "__main__":
    app = MyApp(application_id='org.PenetrationApp.GtkApplication')
    app.run(sys.argv)
