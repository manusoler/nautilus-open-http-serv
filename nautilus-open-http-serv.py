#!/usr/bin/env python
#Este archivo esta en encoding: utf-8

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Written by Manuel Soler Moreno <manusoler@gmail.com>

import sys
import nautilus
import gtk

sys.path.append("/usr/share/nautilus-open-http-serv/")
import gui

class OpenHTTPServExtension(nautilus.MenuProvider):
    def __init__(self):
        self.file_names = []

    def menu_activate_cb(self, menu, file):
        """Called when the user selects the menu Open Simple HTTP Server."""
        wp = gui.wPrincipal(file)
        #gtk.gdk.threads_init()
        gtk.main()

    def get_background_items(self, window, file):
        """Called when the user selects a file in Nautilus."""
        # Put an item in nautilus menu
        item = nautilus.MenuItem("NautilusPython::open_http_serv",
                                 "Open Simple HTTP Server" ,
                                 "Open Simple HTTP Server",
                                 "open-http-serv")
        item.connect("activate", self.menu_activate_cb, file)
        return item,
