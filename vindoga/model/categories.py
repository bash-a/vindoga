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

import os

from PySide import QtCore
from PySide.QtCore import QAbstractListModel, QModelIndex

from vindoga.model.columnsmodel import ColumnsListModel

icopath = '../../data/ico/128/'
categories = [dict(_name='BioInformatics', _iconname=icopath+'app-spyder.png'),
              dict(_name='General',        _iconname=icopath+'app-ipython.png'),
              dict(_name='Physics',        _iconname=icopath+'app-ipython.png'),
              dict(_name='Development',    _iconname=icopath+'app-ipython.png'),
              dict(_name='Misc',           _iconname=icopath+'app-ipython.png'),]

class CategoriesModel(ColumnsListModel):
    def __init__(self, parent=None):
        super(CategoriesModel, self).__init__()

    def getList(self):
        return categories

    def getColumns(self):
        return ('_name', '_iconname')

