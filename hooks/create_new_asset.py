# Copyright (c) 2016 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Task creation hook.
"""

import sgtk
from sgtk.platform.qt import QtGui, QtCore

HookClass = sgtk.get_hook_baseclass()


class CreateNewAssetHook(HookClass):
    """
    Hook called to create a task for a given entity and step.
    """

    def create_asset_name_validator(self):
        """
        Create a QtGui.QValidator instance that will be used by the task name field to interactively
        inform if the name is valid or not. The caller will take ownership of the validator.

        For example, this simple validator will prevent the user from entering spaces in the field.

        .. code-block:: python

            class _Validator(QtGui.QValidator):

                def validate(self, text, pos):
                    if " " in text:
                        return QtGui.QValidator.Intermediate, text.replace(" ", ""), pos - 1
                    else:
                        return QtGui.QValidator.Acceptable, text, pos

        .. note:: The calling convention for fixup and validate have been modified to make them more pythonic.
            http://pyside.readthedocs.org/en/1.2.2/sources/pyside/doc/pysideapi2.html?highlight=string#qstring

        :returns: A QtGui.QValidator derived object.
        """

        alphanumeric_regex = QtCore.QRegExp("^[a-zA-Z0-9]*$")

        return QtGui.QRegExpValidator(alphanumeric_regex)

    def create_new_asset(self, name, asset_type, task_template, sub_type=None):
        """
        Create a new task with the specified information.

        :param name: Name of the task to be created.

        :param asset_type: Pipeline step associated with the task.
        :type asset_type: dictionary with keys 'Type' and 'id'

        :param task_template: Entity associated with this task.
        :type task_template: dictionary with keys 'Type' and 'id'

        :param sub_type: User assigned to the task. Can be None.
        :type sub_type: dictionary with keys 'Type' and 'id'

        :returns: The created task.
        :rtype: dictionary with keys 'step', 'project', 'entity', 'content' and 'task_assignees' if
            'assigned_to' was set.

        :raises sgtk.TankError: On error, during validation or creation, this method
            raises a TankError.
        """
        app = self.parent

        #'# construct the data for the new Task entity:
        data = {
            "code": name,
            "project": app.context.project,
            "sg_asset_type": asset_type,
            "task_template": task_template
        }

        if sub_type:
            data["sg_sub_type"] = sub_type


        # create the asset:
        sg_result = app.shotgun.create("Asset", data)
        if not sg_result:
            raise sgtk.TankError("Failed to create new asset - reason unknown!")

        return None
