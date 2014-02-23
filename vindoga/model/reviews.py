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

class ReviewsModel(QAbstractListModel):
    COLUMNS = ('_appname',)

    def __init__(self, parent=None):
        super(ReviewsModel, self).__init__()
        self._docs = []
        roles = dict(enumerate(self.COLUMNS))
        self.setRoleNames(roles)

    # QAbstractListModel code
    def rowCount(self, parent=QModelIndex()):
        return len(self._docs)

    def data(self, index, role):
        if not index.isValid():
            return None

    @QtCore.Slot()
    def refreshReviewStats(self):
        pass
#         self.reviews.refresh_review_stats()

