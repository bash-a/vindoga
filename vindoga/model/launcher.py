#!/usr/bin/env python
# Copyright (C) 2014 Algorete
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

# import os
# import subprocess

from conda import api as capi

from PySide import QtCore
from PySide import QtGui as gui
# from PySide.QtCore import Slot

from vindoga.model.columnsmodel import ColumnsListModel

class LauncherModel(ColumnsListModel):
    def __init__(self, parent=None):
        super(LauncherModel, self).__init__()
        self.apps = list()
        for fn,info in capi.iteritems(capi.app_get_index()):
            self.apps.append( {'_appname':info['summary'], '_fn':fn, '_icopath':capi.app_get_icon_url(fn) })

    def getList(self):
        return self.apps

    def getColumns(self):
        return ('_appname', '_icopath')

    @QtCore.Slot(int)
    def launchApp(self, index):
        fn = self.apps[index]['_fn']
        appname = self.apps[index]['_appname']

        # Launch the app from Root or return None if does not exist
        if capi.app_launch(fn):
            return

        ret = gui.QMessageBox.question(None, "%s" % appname, \
                                       "Application is not installed.\nShould I install it?", \
                                        gui.QMessageBox.Ok | gui.QMessageBox.Cancel, gui.QMessageBox.Ok)
        if ret == gui.QMessageBox.Ok:
            capi.app_install(fn)
            capi.app_launch(fn)
        return
