import sgtk

HookBaseClass = sgtk.get_hook_baseclass()


class CustomActions(HookBaseClass):
    """
    Implementation of the CustomActions class
    """

    def execute(self, button):
        """

        @param button: QPushButton
        @return:
        """

        button.setVisible(False)
