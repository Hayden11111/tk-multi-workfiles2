# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_task_form.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from sgtk.platform.qt import QtCore, QtGui

class Ui_NewAssetForm(object):
    def setupUi(self, NewAssetForm):
        NewAssetForm.setObjectName("NewAssetForm")
        NewAssetForm.resize(380, 270)
        NewAssetForm.setMinimumSize(QtCore.QSize(380, 270))

        self.verticalLayout_widget = QtGui.QVBoxLayout(NewAssetForm)

        self.tab_widget = QtGui.QTabWidget()



        self.asset_tab = QtGui.QWidget(self.tab_widget)
        self.animation_tab = QtGui.QWidget(self.tab_widget)

        self.tab_widget.addTab(self.asset_tab, "Create Asset")
        self.tab_widget.addTab(self.animation_tab, "Create Animation")

        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout_animation = QtGui.QVBoxLayout()



        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.verticalLayout_animation.setSpacing(4)
        self.verticalLayout_animation.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_animation.setObjectName("verticalLayout_animation")

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)

        # Asset Form intro
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtGui.QLabel(NewAssetForm)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)

        # Animation Form Intro
        self.verticalLayout_2_anim = QtGui.QVBoxLayout()
        self.verticalLayout_2_anim.setSpacing(20)
        self.verticalLayout_2_anim.setContentsMargins(12, 12, 12, 4)
        self.verticalLayout_2_anim.setObjectName("verticalLayout_2_anim")
        self.label_3_anim = QtGui.QLabel()
        self.label_3_anim.setWordWrap(True)
        self.label_3_anim.setObjectName("label_3_anim")


        self.verticalLayout_2_anim.addWidget(self.label_3_anim)

        # Grid for Asset
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")


        anim_asset_layout =  QtGui.QHBoxLayout()

        self.anim_asset_name = QtGui.QLabel(NewAssetForm)
        self.anim_asset_name.setObjectName("anim_asset_name")
        self.anim_asset_name.setFont(font)

        self.anim_asset = QtGui.QComboBox(NewAssetForm)
        self.anim_asset.setObjectName("anim_asset")

        anim_asset_layout.addWidget(self.anim_asset_name)
        anim_asset_layout.addWidget(self.anim_asset)
        self.verticalLayout_2_anim.addLayout(anim_asset_layout)

        anim_name_asset_layout = QtGui.QHBoxLayout()
        self.anim_name_label = QtGui.QLabel(NewAssetForm)
        self.anim_name_label.setObjectName("anim_name_label")
        self.anim_name_label.setFont(font)

        self.anim_asset_combo = QtGui.QComboBox(NewAssetForm)
        self.anim_asset_combo.setObjectName("anim_asset_combo")
        self.anim_asset_combo.setMinimumWidth(100)

        self.anim_name = QtGui.QLineEdit(NewAssetForm)
        self.anim_name.setObjectName("anim_name")
        anim_name_asset_layout.addWidget(self.anim_name_label)
        anim_name_asset_layout.addWidget(self.anim_asset_combo)
        anim_name_asset_layout.addWidget(self.anim_name)
        self.verticalLayout_2_anim.addLayout(anim_name_asset_layout)


        anim_action_layout = QtGui.QHBoxLayout()
        self.anim_action_name_label = QtGui.QLabel(NewAssetForm)
        self.anim_name_label.setFont(font)
        self.anim_action_name_label.setObjectName("anim_action_name_label")
        self.anim_action_name = QtGui.QLineEdit(NewAssetForm)
        self.anim_action_name_label.setFont(font)
        self.anim_action_name.setObjectName("anim_action_name")

        anim_action_layout.addWidget(self.anim_action_name_label)
        anim_action_layout.addWidget(self.anim_action_name)
        self.verticalLayout_2_anim.addLayout(anim_action_layout)

        #self.verticalLayout_2_anim.addLayout(self.gridLayout_anim)

        self.label_6 = QtGui.QLabel(NewAssetForm)
        self.task_template_label = QtGui.QLabel(NewAssetForm)
        self.sub_type_label = QtGui.QLabel(NewAssetForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.task_template_label.setFont(font)
        self.task_template_label.setObjectName("task_template_label")
        self.gridLayout.addWidget(self.task_template_label, 2, 0, 1, 1)
        self.sub_type_label.setFont(font)
        self.sub_type_label.setObjectName("sub_type_label")
        self.gridLayout.addWidget(self.sub_type_label, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(NewAssetForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.asset_type = QtGui.QComboBox(NewAssetForm)
        self.asset_type.setObjectName("asset_type")
        self.gridLayout.addWidget(self.asset_type, 1, 2, 1, 1)
        self.task_template = QtGui.QLabel(NewAssetForm)
        self.task_template.setObjectName("task_template")
        self.gridLayout.addWidget(self.task_template, 2, 2, 1, 1)
        self.sub_type = QtGui.QComboBox(NewAssetForm)
        self.sub_type.setObjectName("sub_type")
        self.gridLayout.addWidget(self.sub_type, 3, 2, 1, 1)
        self.custom_sub_type_label = QtGui.QLabel(NewAssetForm)
        self.custom_sub_type_label.setFont(font)
        self.gridLayout.addWidget(self.custom_sub_type_label, 4, 0, 1, 1)
        self.custom_sub_type = QtGui.QLineEdit(NewAssetForm)
        self.custom_sub_type.setObjectName("custom_sub_type")
        self.gridLayout.addWidget(self.custom_sub_type, 4, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.label = QtGui.QLabel(NewAssetForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(NewAssetForm)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.asset_name = QtGui.QLineEdit(NewAssetForm)
        self.asset_name.setObjectName("asset_name")
        self.gridLayout.addWidget(self.asset_name, 0, 2, 1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        #self.gridLayout_anim.setColumnStretch(2, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.warning = QtGui.QLabel(NewAssetForm)
        self.warning.setText("")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_animation.addLayout(self.verticalLayout_2_anim)
        spacerItem1 = QtGui.QSpacerItem(20, 11, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.break_line = QtGui.QFrame(NewAssetForm)
        self.break_line.setFrameShape(QtGui.QFrame.HLine)
        self.break_line.setFrameShadow(QtGui.QFrame.Sunken)
        self.break_line.setObjectName("break_line")
        self.verticalLayout.addWidget(self.break_line)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(12, 8, 12, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancel_btn = QtGui.QPushButton(NewAssetForm)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.create_btn = QtGui.QPushButton(NewAssetForm)
        self.create_btn.setDefault(True)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout.addWidget(self.create_btn)
        self.verticalLayout_widget.addWidget(self.tab_widget)
        self.verticalLayout_widget.addWidget(self.warning)
        self.verticalLayout_widget.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2_anim.setStretch(2, 1)

        self.asset_tab.setLayout(self.verticalLayout)
        self.animation_tab.setLayout(self.verticalLayout_animation)




        self.retranslateUi(NewAssetForm)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), NewAssetForm.close)
        QtCore.QMetaObject.connectSlotsByName(NewAssetForm)
        #NewAssetForm.setTabOrder(self.asset_name, self.asset_type)
        #NewAssetForm.setTabOrder(self.asset_type, self.create_btn)
        #NewAssetForm.setTabOrder(self.create_btn, self.cancel_btn)

    def retranslateUi(self, NewAssetForm):
        NewAssetForm.setWindowTitle(QtGui.QApplication.translate("NewAssetForm", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("NewAssetForm", "Create a new Asset using the Name and Pipeline Step entered below.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3_anim.setText(QtGui.QApplication.translate("NewAssetForm", "Create a new Animation and Action.", None, QtGui.QApplication.UnicodeUTF8))
        self.anim_name_label.setText(QtGui.QApplication.translate("NewAssetForm", "Animation Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.anim_action_name_label.setText(QtGui.QApplication.translate("NewAssetForm", "Action Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.anim_asset_name.setText(
            QtGui.QApplication.translate("NewAssetForm", "Asset:", None, QtGui.QApplication.UnicodeUTF8))

        self.asset_type.setAccessibleName(QtGui.QApplication.translate("NewAssetForm", "Asset Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("NewAssetForm", "Asset Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewAssetForm", "Asset Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.task_template_label.setText(QtGui.QApplication.translate("NewAssetForm", "Task Template:", None, QtGui.QApplication.UnicodeUTF8))
        self.custom_sub_type_label.setText(QtGui.QApplication.translate("NewAssetForm", "New Sub Type Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.sub_type_label.setText(QtGui.QApplication.translate("NewAssetForm", "Sub Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.task_template.setText(QtGui.QApplication.translate("NewAssetForm", "Template", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_name.setAccessibleName(QtGui.QApplication.translate("NewAssetForm", "Asset Name", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_btn.setText(QtGui.QApplication.translate("NewAssetForm", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.create_btn.setText(QtGui.QApplication.translate("NewAssetForm", "Create", None, QtGui.QApplication.UnicodeUTF8))

