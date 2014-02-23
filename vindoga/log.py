#!/usr/bin/python
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

import logging
import logging.handlers
import os.path

root = logging.getLogger()
fmt = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", None)
handler = logging.StreamHandler()
handler.setFormatter(fmt)
root.addHandler(handler)
# handler.addFilter(YourOwnFilter())
