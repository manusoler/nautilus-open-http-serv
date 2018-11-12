# Name of the package
PACKAGE=nautilus-open-http-serv
PACK_DIR=/usr/share/$(PACKAGE)
GLADE_DIR=$(PACK_DIR)/glade/
PIX_DIR=$(PACK_DIR)/pixmaps/
EXTENSIONS_DIR=/usr/lib/nautilus/extensions-2.0/python/
PIXMAPS_DIR=/usr/share/pixmaps/

all:

install: make-install-dirs
	install -m 755 $(PACKAGE).py $(DESTDIR)$(EXTENSIONS_DIR)
	install -m 644 gui.py $(DESTDIR)$(PACK_DIR)
	install -m 644 ipinfo.py $(DESTDIR)$(PACK_DIR)
	install -m 644 *.glade $(DESTDIR)$(GLADE_DIR)
	install -m 644 pixmaps/*.png $(DESTDIR)$(PIX_DIR)
	install -m 644 $(PACKAGE).png $(DESTDIR)$(PIXMAPS_DIR)

make-install-dirs:
	mkdir -p $(DESTDIR)$(PACK_DIR)
	mkdir -p $(DESTDIR)$(GLADE_DIR)
	mkdir -p $(DESTDIR)$(PIX_DIR)
	mkdir -p $(DESTDIR)$(EXTENSIONS_DIR)
	mkdir -p $(DESTDIR)$(PIXMAPS_DIR)

uninstall:
	rm $(DESTDIR)$(EXTENSIONS_DIR)$(PACKAGE).py
	rm $(DESTDIR)$(PACK_DIR)gui.py
	rm $(DESTDIR)$(PACK_DIR)ipinfo.py
	rm $(DESTDIR)$(GLADE_DIR)*.glade
	rm $(DESTDIR)$(PIX_DIR)*.png
	rm $(DESTDIR)$(PIXMAPS_DIR)$(PACKAGE).png

clean:
	rm -f *-stamp
	rm -rf debian/$(PACKAGE)
	rm -f debian/files
	find . -type f -iregex '.*~$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.pyc$$'  -print | xargs rm -rf
	find . -type f -iregex '.*\.bak$$'  -print | xargs rm -rf


