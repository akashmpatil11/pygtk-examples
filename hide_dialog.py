import pygtk
import gtk

class DialogTest:

    def rundialog(self, widget, data=None):
	print "rundialog"
        if self.visible:
            self.dia.hide()
        else:
            self.dia.show_all()
        self.visible = not self.visible
        return True

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)

        self.dia = gtk.Dialog('TEST DIALOG', self.window, gtk.DIALOG_DESTROY_WITH_PARENT)
        self.dia.vbox.pack_start(gtk.Label('A show/hide dialog'))
        self.dia.connect("delete-event", self.rundialog)
        self.visible = False

        self.button = gtk.Button("Run Dialog")    
        self.button.connect("clicked", self.rundialog, None)
        self.window.add(self.button)
        self.button.show()
        self.window.show()



if __name__ == "__main__":
    testApp = DialogTest()
    gtk.main()

