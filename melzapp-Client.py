#Quantum Age Publishing presents: Melzapp - My Personal Messenger
#CLIENT
#!/usr/bin/env python3

import threading
import gtk
import gobject
import socket
import re
import time
import datetime

gobject.threads_init()

#CLIENT GRAPHICAL USER INTERFACE HERE
class MainWindow(gtk.Window):
    def __init__(self):
        
        super(MainWindow, self).__init__()
#CONTROLS
        self.set_title("MELZAPP!")
        vbox = gtk.VBox()
        hbox = gtk.Hbox()
        self.username_label = gtk.Label()
        self.text_entry = gtk.Entry()
        send_button = gtk.Button("Send")
        self.text_buffer = gtk.TextBuffer()
        text_view = gtk.TextView(self.text_buffer)
#Connect events
        self.connect("destroy" , self.graceful_quit)
        send_button.connect("clicked" , self.send_message)
        
        self.text_entry.connect("activate" , self.send_message)

        vbox.pack_start(text_view)
        hbox.pack_start(self.username_label, expand = False)
        hbox.pack_start(self.text_entry)
        hbox.pack_end(send_button, expanc = False)
        self.add(vbox)
        self.show_all()

#CONFIGURATION PROCESS
        self.configure()
    def ask_for_info(self, question):

#MESSAGE BOX AND RESPONSE
        dialog = gtk.MessageDialog(parent = self, type = gtk.MESSAGE_QUESTION, flags = gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, buttons = gtk.BUTTONS_OK_CANCEL, message_format = question)
        entry = gtk.Entry()
        entry.show()
        dialog.vbox.pack_end(entry)
        response = dialog.run()
        response_text = entry.get_text()
        dialog.destroy()
        if response == gtk.RESPONSE_OK:
            return response_text
        else:
            return None

#CONFIGURE THE CLIENT
    



