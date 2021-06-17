# -*- mode: python ; coding: utf-8 -*-

import os
import platform
import gooey

from PyInstaller.building.api import EXE, PYZ, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.building.datastruct import Tree
from PyInstaller.building.osx import BUNDLE

gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')

block_cipher = None


a = Analysis(['autosub/__main__.py'])
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION')]


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          gooey_languages,
          gooey_images,
          options,
          name='autosub',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))

locale_data = [('data', 'autosub/data', 'DATA')]
coll = COLLECT(exe, locale_data, name='autosub')


info_plist = {'addition_prop': 'additional_value'}
app = BUNDLE(exe,
             name='autosub.app',
             bundle_identifier=None,
             info_plist=info_plist
            )
