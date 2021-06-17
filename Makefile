# TODO: use "autosub.exe" as the filename in Windows and "autosub" otherwise.

.PHONY: clean build-executable

all: build-executable

clean:
	rm -r build dist

build-executable:
	pyinstaller build.spec
