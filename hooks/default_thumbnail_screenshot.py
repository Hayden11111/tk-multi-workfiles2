import sgtk
import os
from sgtk.platform.qt import QtCore, QtGui

HookClass = sgtk.get_hook_baseclass()


class CaptureScreenShot(HookClass):
    """
    Hook called to return the default no thumbnail icon
    """

    def execute(self, ctx):
        """
            Returns a Pixmap with a placeholder thumbnail

        :returns: QtGui.QPixmap

        """
        no_thumbnail = QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "../", "resources", "camera.png"))
        return no_thumbnail
