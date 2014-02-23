/*
 * Copyright 2011 Canonical Ltd.
 *
 * Authors:
 *  Michael Vogt <mvo@ubuntu.com>
 *  Olivier Tilloy <olivier@tilloy.net>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; version 3.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

import QtQuick 1.0

FocusScope {
    id: launchview

    signal launchApp(string appname)

    clip: true

    SystemPalette {
        id: activePalette
        colorGroup: SystemPalette.Active
    }

    Rectangle {
        color: activePalette.base
        anchors.fill: parent
    }

    CloudsHeader {
        anchors.top: parent.top
        anchors.left: parent. left
        anchors.right: parent.right
    }

    ScrollBar {
        id: scrollbar
        width: 6
        height: parent.height
        orientation: Qt.Vertical

        anchors.right: parent.right
        position: catgrid.visibleArea.yPosition
        pageSize: catgrid.visibleArea.heightRatio
    }

    Text {
        id: depheader
//         anchors.top: parent.top
//         anchors.left:  parent.left
//         anchors.margins: 24
//
//         text: qsTr("Apps")
//         font.pointSize: 18
//         font.bold: true
    }

    GridView {
        id: catgrid
        anchors.top: depheader.bottom
        anchors.bottom: parent.bottom
        anchors.left: parent.left
        anchors.right: scrollbar.left
        anchors.margins: 10
        focus: true

        cellWidth: 160
        cellHeight: 140

        model: launchermodel
        delegate: Item {
            property string appname: _appname
            property string icopath: _icopath
            property string wrap:"Text.WordWrap"

            width: catgrid.cellWidth
            height: catgrid.cellHeight

            Image {
                id: caticonimg
                source: icopath
                anchors.horizontalCenter: parent.horizontalCenter
            	width: catgrid.cellHeight * .5
            	height: catgrid.cellHeight * .5
            }

            Text {
                text: appname
                wrapMode: wrap
                width:catgrid.cellWidth
                anchors.top: caticonimg.bottom
                anchors.margins: 10
                anchors.horizontalCenter: parent.horizontalCenter
            }

            MouseArea {
                anchors.fill: parent
                onClicked: {
                    catgrid.currentIndex = index
                    launchview.launchApp(index)
                }
            }
        }
    }
}
