SOURCES := $(shell find . -name '*.py')

configure:
	apt install python3-pip
	pip install pyinstaller

build: SOURCES
	python3 -m PyInstaller main.py --onefile --name image-control

install:
	cp dist/image-control /usr/local/bin
	cp image-control-completion /etc/bash_completion.d
	rm /usr/local/bin/vc
	ln -s /usr/local/bin/image-control /usr/local/bin/vc

uninstall:
	rm -rf /usr/local/bin/image

.PHONY: SOURCES