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

from conda import api as capi

from PySide import QtCore
from PySide.QtCore import QAbstractListModel, QModelIndex

class PackagesModel(QAbstractListModel):
    COLUMNS = ('_appname', '_pkgname', '_fn', '_icon', '_summary', '_description', '_installed',
               '_ratings_total', '_ratings_average', '_installremoveprogress')


    def __init__(self, parent=None):
        super(PackagesModel, self).__init__()
        roles = dict(enumerate(self.COLUMNS))
        self.setRoleNames(roles)
        self._list = list()

#         index = capi.get_index()
#         for fn,info in capi.iteritems(index):
#             version = info.get('version')
#             pkgsize = '%dkB' % (info.get('size')/1024)
#             pkgdesc = 'Size: %s\nLicense: %s' % (pkgsize, info.get('license'))
#             pkgname = info.get('name')
#             pkginst = len(capi.app_is_installed(fn)) > 0
#             self._list.append(dict(_appname=pkgname, _pkgname=pkgname, _fn=fn, _installed=pkginst, _icon='', \
#                                    _summary='v%s' % (version),_description=pkgdesc, \
#                                    _ratings_total=0, _ratings_average=0., _installremoveprogress=0))


    # QAbstractListModel code
    def rowCount(self, parent=QModelIndex()):
        return len(self._list)


    def data(self, index, role):
        if not index.isValid():
            return None
        pkg = self._list[index.row()]
        role = self.COLUMNS[role]
        if pkg.has_key(role):
            return pkg[role]
        else:
            return None

    @QtCore.Slot(str)
    def setCategory(self, category):
        print category

    @QtCore.Slot(str)
    def installPackage(self, pkgname):
        print pkgname
