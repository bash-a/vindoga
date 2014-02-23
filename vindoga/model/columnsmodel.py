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

from abc import abstractmethod

from PySide.QtCore import QAbstractListModel, QModelIndex

class ColumnsListModel(QAbstractListModel):

    def __init__(self, parent=None):
        super(ColumnsListModel, self).__init__()
        roles = dict(enumerate(self.getColumns()))
        self.setRoleNames(roles)

    @abstractmethod
    def getList(self):
        pass

    @abstractmethod
    def getColumns(self):
        pass

    # QAbstractListModel code
    def rowCount(self, parent=QModelIndex()):
        return len(self.getList())

    def data(self, index, role):
        if not index.isValid():
            return None
        pkg = self.getList()[index.row()]
        role = self.getColumns()[role]
        if pkg.has_key(role):
            return pkg[role]
        else:
            return None

