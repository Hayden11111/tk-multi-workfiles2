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
New Asset Form.
"""

import sgtk
from sgtk.platform.qt import QtCore, QtGui

from .util import value_to_str

get_type_display_name = sgtk.platform.import_framework(
    "tk-framework-shotgunutils", "shotgun_globals"
).get_type_display_name


class NewAssetForm(QtGui.QWidget):
    """
    Form for requesting details needed to create a new Shotgun Asset.
    """

    @property
    def exit_code(self):
        """
        Exit code of the dialog.

        :returns: QtGui.QDialog.Accepted or QtGui.QDialog.Rejected
        """
        return self._exit_code

    @property
    def hide_tk_title_bar(self):
        """
        Hint to hide the Toolkit title bar.

        :returns: True.
        """
        return True

    def __init__(self, user, parent):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)

        self._app = sgtk.platform.current_bundle()
        self._user = user
        self._exit_code = QtGui.QDialog.Rejected

        self._task_templates = {}
        self._selected_template = {}
        self._selected_asset_type = ""

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # set up the UI
        from .ui.new_asset_form import Ui_NewAssetForm

        self._ui = Ui_NewAssetForm()
        self._ui.setupUi(self)

        validator = self._app.execute_hook_method(
            "create_new_asset_hook", "create_asset_name_validator"
        )
        if validator:
            # Take ownership since the widget doesn't.
            validator.setParent(self)
            self._ui.asset_name.setValidator(validator)

        sub_type_validator = self._app.execute_hook_method(
            "create_new_asset_hook", "create_asset_sub_type_validator"
        )
        if sub_type_validator:
            # Take ownership since the widget doesn't.
            sub_type_validator.setParent(self)
            self._ui.custom_sub_type.setValidator(sub_type_validator)

        schema = self._app.sgtk.shotgun.schema_field_read('Asset')

        # Get all asset types
        asset_types = schema.get('sg_asset_type', {}).get('properties', {}).get('valid_values', {}).get('value', [])
        for asset_type in asset_types:
            self._ui.asset_type.addItem(asset_type)

        sub_types = schema.get('sg_sub_type', {}).get('properties', {}).get('valid_values', {}).get('value', [])
        self._ui.sub_type.addItem("(Optional)")
        for sub_type in sub_types:
            self._ui.sub_type.addItem(sub_type)

        self.task_templates = self._app.sgtk.shotgun.find("TaskTemplate", [], ["id", "code", "entity_type", "tasks"])

        self._ui.sub_type.addItem("Custom")

        self.project_assets = self._app.sgtk.shotgun.find("Asset", [["project", "is", self._app.engine.context.project]], ["code"])

        for i in self.project_assets:
            self._ui.anim_asset.addItem(i["code"], i)

        # hook up controls:
        self._ui.create_btn.clicked.connect(self._on_create_btn_clicked)
        self._ui.asset_type.currentIndexChanged.connect(self._update_task_template)
        self._ui.sub_type.currentTextChanged.connect(self.init_custom_sub_type)
        self._ui.asset_name.textChanged.connect(self.title_asset_name)
        self._ui.custom_sub_type.textChanged.connect(self.title_sub_type_name)
        self._update_task_template(0)
        self._ui.anim_asset.currentIndexChanged.connect(self.update_anim_asset)

        self.init_custom_sub_type("")

        # initialize line to be plain and the same colour as the text:
        self._ui.break_line.setFrameShadow(QtGui.QFrame.Plain)
        clr = QtGui.QApplication.palette().text().color()
        self._ui.break_line.setStyleSheet(
            "#break_line{color: rgb(%d,%d,%d);}"
            % (clr.red() * 0.75, clr.green() * 0.75, clr.blue() * 0.75)
        )

        self._ui.asset_type.setCurrentText("Prop")

    def init_custom_sub_type(self, text):
        if text == self.custom_flag:
            self._ui.custom_sub_type.setEnabled(True)
            self._ui.custom_sub_type.setPlaceholderText("")
        else:
            self._ui.custom_sub_type.setEnabled(False)
            self._ui.custom_sub_type.setPlaceholderText("Select the Custom Sub Type")

    def update_anim_asset(self):

        selected_asset = self._ui.anim_asset.currentData()
        anim_entities = self._app.sgtk.shotgun.find("CustomEntity09", [["sg_asset", "is", selected_asset]], ["code"])

        self._ui.anim_asset_combo.clear()
        for i in anim_entities:
            self._ui.anim_asset_combo.addItem(i["code"], i)



    def show(self):

        self.activateWindow()
        super(NewAssetForm, self).show()

    def title_asset_name(self, text):

        valid_string = text[0].upper() + text[1:]
        self._ui.asset_name.setText(valid_string)

    def title_sub_type_name(self, text):

        valid_string = text[0].upper() + text[1:]
        self._ui.custom_sub_type.setText(valid_string)

    @property
    def custom_flag(self):
        return "Custom"

    def _update_task_template(self, x):
        """
            Displays the Task template
        @param x:
        @return:
        """
        current_asset_type = self._ui.asset_type.currentText()
        for i in self.task_templates:
            if i['code'] == current_asset_type:
                self._ui.task_template.setText(i['code'])
                self._ui.create_btn.setEnabled(True)
                return

        # did not find a template, Use Generic
        for i in self.task_templates:
            if i['code'] == "Generic":
                self._ui.task_template.setText(i['code'])
                self._ui.create_btn.setEnabled(True)
                return

        self._ui.task_template.setText("No supported Task template for asset type! - Contact Core Tech")
        self._ui.create_btn.setEnabled(False)

    def _get_asset_name(self):
        """
        :returns: The task name entered by the user.
        """
        return value_to_str(self._ui.asset_name.text())

    def _set_warning(self, msg):
        """
        Display a warning inside the dialog.

        :param msg: Message to display.
        """
        self._ui.warning.setText(
            "<p style='color:rgb%s'>Failed to create a new task: %s</p>"
            % (self._app.warning_color, msg)
        )

    def _get_sub_type(self):

        if self._ui.sub_type.currentIndex() == 0:
            return None
        else:
            current_item = self._ui.sub_type.currentText()
            if current_item == self.custom_flag:
                return value_to_str(self._ui.custom_sub_type.text())
            else:
                return current_item

    def _get_task_template(self):
        current_template = self._ui.task_template.text()

        for i in self.task_templates:
            if i['code'] == current_template:
                return i

    def _on_create_btn_clicked(self):
        """
        Called when the user is ready to create the task.
        """
        self._app.logger.debug(self._ui.tab_widget.currentIndex)

        if self._ui.tab_widget.currentIndex() == 0:
            if len(self._get_asset_name()) == 0:
                self._set_warning("Please enter an asset name.")
                return
            self._create_asset()

        if self._ui.tab_widget.currentIndex() == 1:
            self._app.logger.debug("Creating Animation")
            self._create_anim()

    def _create_asset(self):
        try:
            self._app.execute_hook_method(
                "create_new_asset_hook",
                "create_new_asset",
                name=self._get_asset_name(),
                asset_type=self._ui.asset_type.currentText(),
                task_template=self._get_task_template(),
                sub_type=self._get_sub_type()
            )
            self._exit_code = QtGui.QDialog.Accepted
            self.close()
        except sgtk.TankError as e:
            self._set_warning(str(e))

    def _create_anim(self):
        try:
            self._app.execute_hook_method(
                "create_new_asset_hook",
                "create_new_animation",
                asset=self._ui.anim_asset.currentData(),
                anim_asset=self._ui.anim_asset_combo.currentData(),
                new_anim_name=self._ui.anim_name.text(),
                action=self._ui.anim_action_name.text()
            )
            self._exit_code = QtGui.QDialog.Accepted
            self.close()
        except sgtk.TankError as e:
            self._set_warning(str(e))
