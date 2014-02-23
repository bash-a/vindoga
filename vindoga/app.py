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

from __future__ import absolute_import

import logging
import os
import sys

from PySide import QtDeclarative
from PySide.QtCore import QUrl
from PySide.QtGui import QApplication, QIcon
from PySide.QtDeclarative import QDeclarativeView

from vindoga import log
from vindoga import model

from optparse import OptionParser

LOG = logging.getLogger("vindoga")

if __name__ == "__main__":
    parser = OptionParser("usage: %prog [options] [package-name]", \
  version="%prog " + "0.0.1")
    parser.add_option("--debug", action="store_true",
                      help="enable debug mode", default=False)

    (options, args) = parser.parse_args()

    if options.debug:
        log.root.setLevel(level=logging.DEBUG)
    else:
        log.root.setLevel(level=logging.INFO)

    dirpath = os.path.dirname(__file__)
    icopath = os.path.join(dirpath, "../data/ico/128/vindoga-flower.png")
    qmlpath = os.path.join(dirpath, "../data/qml/vindoga.qml")

    qapp = QApplication(sys.argv)
    view = QDeclarativeView()

    launchermodel = model.LauncherModel()
    pkglistmodel = model.PackagesModel()
    reviewslistmodel = model.ReviewsModel()
    categoriesmodel = model.CategoriesModel()
    rc = view.rootContext()
    rc.setContextProperty('launchermodel', launchermodel)
    rc.setContextProperty('pkglistmodel', pkglistmodel)
    rc.setContextProperty('reviewslistmodel', reviewslistmodel)
    rc.setContextProperty('categoriesmodel', categoriesmodel)

    view.setSource(QUrl.fromLocalFile(qmlpath))
    view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)
    view.setWindowTitle(view.tr("Algorete Market"))
    view.setWindowIcon(QIcon(icopath))

    view.show()
    sys.exit(qapp.exec_())
