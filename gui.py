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

'''
Contains app main gui class.
'''

import pygtk
import gtk
import gtk.glade
import os
import os.path
import string
import subprocess
import webbrowser
pygtk.require("2.0")

import ipinfo

PROY_PATH = "/usr/share/nautilus-open-http-serv"
GLADE_PATH = os.path.join(PROY_PATH, "glade")
PIX_PATH = os.path.join(PROY_PATH, "pixmaps")


class wPrincipal:
    '''
    Main windows
    '''

    def __init__(self, file, port=8000):
        '''Constructor de la clase'''
        # Construimos a partir del archivo glade la ventana wPrincipal
        self.glade = gtk.glade.XML(os.path.join(GLADE_PATH, "nautilus-open-http-serv.glade"), root="wPrincipal")
        # Conectamos todas las señales especificadas en el archivo
        self.glade.signal_autoconnect(self)
        # Establecemos un icono
        self.glade.get_widget("wPrincipal").set_icon(gtk.gdk.pixbuf_new_from_file(os.path.join(PIX_PATH, "web.png")))

        # Establecemos todas las imagenes
        self.glade.get_widget("image").set_from_file(os.path.join(PIX_PATH, "bigweb.png"))
        self.glade.get_widget("btnBrowser").set_image(gtk.image_new_from_file(os.path.join(PIX_PATH, "browser.png")))
        # self.glade.get_widget("btnStop").set_image(gtk.image_new_from_file(os.path.join(PIX_PATH, "stop.png")))

        self.port = port
        work_dir = file.get_uri()[7:]
        work_dir = string.replace(work_dir, "%20", " ")
        # Check if it is invoqued from desktop 
        if file.get_uri() == "x-nautilus-desktop:///":
            work_dir = os.getenv("HOME")
        self.glade.get_widget("lblLocation").set_markup("<b>%s</b>" % work_dir)
        self.glade.get_widget("lblPort").set_markup("<b>%d</b>" % self.port)
        # Get an active ifaz ip
        ifaces = ipinfo.all_interfaces()
        ip = ifaces[0] # IP = IP 'lo' = 127.0.0.1
        if len(ifaces) > 1:
            ip = ipinfo.get_ip(ifaces[1])
        self.glade.get_widget("lblIP").set_markup("<b>%s</b>" % ip)
        self.buf = gtk.TextBuffer()
        self.buf.set_text("SimpleHTTPServer running...")
        self.glade.get_widget("txtMessages").set_buffer(self.buf)

        # self.stop = False
        # Ejecutamos el servidor
        self.popen = subprocess.Popen(["python", "-m", "SimpleHTTPServer",
                                       str(self.port)], cwd=work_dir)
        # TODO thread.start_new_thread(self.get_info, ())

    def on_wPrincipal_delete_event(self, widget, event):
        '''
        Evento al cerrar la ventana.
        Abortamos la ejecución del SimpleHTTPServ y salimos
        '''
        #self.stop = True
        try:
            os.kill(self.popen.pid, 9)
            self.popen.wait()
        except OSError:
            pass
        gtk.main_quit()

    def on_btnStop_clicked(self, widget):
        '''Evento al pulsar sobre para.
            Abortamos la ejecución del SimpleHTTPServ y salimos'''
        try:
            os.kill(self.popen.pid, 9)
            self.popen.wait()
        except OSError:
            pass
        self.glade.get_widget("wPrincipal").destroy() # Destroy the window
        gtk.main_quit()

    def on_btnBrowser_clicked(self, widget):
        '''
        Evento al pulsar sobre el boton de Open in Browser
        Abre la pagina servida por el simple http server en localhost
        '''
        webbrowser.open("http://localhost:%d" % self.port)
