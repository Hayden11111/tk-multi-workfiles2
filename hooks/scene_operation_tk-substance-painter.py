# Copyright (c) 2015 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

from tank_vendor import six

import substance_painter.project
import substance_painter.resource
import substance_painter.display

import sgtk
from sgtk.platform.qt import QtGui, QtCore

HookClass = sgtk.get_hook_baseclass()


class PrepareScene(QtGui.QDialog):
    def __init__(self, sg, context, parent=None):
        super(PrepareScene, self).__init__(parent)

        layout = QtGui.QVBoxLayout(self)

        self.publish_mappings = {}
        # Do shotgun lookup to find published files
        filters = [["published_file_type", "is", {'type': 'PublishedFileType', 'id': 34, 'code': 'Static Mesh Export'}],
                   ["entity", "is", context.entity]]
        fields = ["sg_revision", "code", "path", "sg_name"]
        order = [{'field_name': 'sg_revision', 'direction': 'desc'}]
        asset_publish = sg.find("PublishedFile", filters, fields, order)

        for i in asset_publish:
            self.publish_mappings["{} #{}".format(i['code'], i['sg_revision'])] = i

        self.branch_lbl = QtGui.QLabel("Choose Branch name")
        self.vspc1 = QtGui.QSpacerItem(
            20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )
        self.graph_name = QtGui.QComboBox()
        self.graph_name.addItems(list(self.publish_mappings.keys()))
        self.vspc2 = QtGui.QSpacerItem(
            20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding
        )

        layout.addWidget(self.branch_lbl)
        layout.addItem(self.vspc1)
        layout.addWidget(self.graph_name)
        layout.addItem(self.vspc2)

        # OK and Cancel buttons
        buttons = QtGui.QDialogButtonBox(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel,
            QtCore.Qt.Horizontal,
            self,
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def selected_publish_data(self):
        return self.publish_mappings.get(self.graph_name.currentText())

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def createGraphTypeDialog(sg, context, parent=None):
        dialog = PrepareScene(sg, context, parent)
        result = dialog.exec_()
        data = dialog.selected_publish_data()
        return (data, result == QtGui.QDialog.Accepted)


class SceneOperation(HookClass):
    """
    Hook called to perform an operation with the
    current scene
    """

    def execute(
            self,
            operation,
            file_path,
            context,
            parent_action,
            file_version,
            read_only,
            **kwargs
    ):
        """
        Main hook entry point

        :param operation:       String
                                Scene operation to perform

        :param file_path:       String
                                File path to use if the operation
                                requires it (e.g. open)

        :param context:         Context
                                The context the file operation is being
                                performed in.

        :param parent_action:   This is the action that this scene operation is
                                being executed for.  This can be one of:
                                - open_file
                                - new_file
                                - save_file_as
                                - version_up

        :param file_version:    The version/revision of the file to be opened.  If this is 'None'
                                then the latest version should be opened.

        :param read_only:       Specifies if the file should be opened read-only or not

        :returns:               Depends on operation:
                                'current_path' - Return the current scene
                                                 file path as a String
                                'reset'        - True if scene was reset to an empty
                                                 state, otherwise False
                                all others     - None
        """

        if operation == "current_path":
            if substance_painter.project.is_open():
                return substance_painter.project.file_path()
            else:
                return ""
        elif operation == "open":
            # Open a project
            substance_painter.project.open(file_path)
        elif operation == "save":
            # Save Project
            substance_painter.project.save_as(file_path, substance_painter.project.ProjectSaveMode.Full)
            # substance_painter.project.save(substance_painter.project.ProjectSaveMode.Full)
        elif operation == "save_as":
            # first rename the scene as file_path:
            substance_painter.project.save_as(file_path, substance_painter.project.ProjectSaveMode.Full)

        elif operation == "reset":
            """
            Reset the scene to an empty state
            """
            if substance_painter.project.is_open():
                while substance_painter.project.needs_saving():
                    # changes have been made to the scene
                    res = QtGui.QMessageBox.question(None,
                                                     "Save your scene?",
                                                     "Your scene has unsaved changes. Save before proceeding?",
                                                     QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)

                    if res == QtGui.QMessageBox.Cancel:
                        return False
                    elif res == QtGui.QMessageBox.No:
                        break
                    else:
                        substance_painter.project.save(substance_painter.project.ProjectSaveMode.Full)

                # do new file:
                substance_painter.project.close()
                return True
            else:
                return True
