import maya.cmds as cmds
import maya.OpenMayaUI as omui
from PySide2 import QtWidgets, QtCore
from shiboken2 import wrapInstance

def get_maya_main_win():
    """Return the Maya main window widget"""
    main_window = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window), QtWidgets.QWidget)

class MultipleRename(QtWidgets.QDialog):
    """Window Tool Class"""

    def __init__(self):
        """Initialize the Object"""
        super(MultipleRename, self).__init__(parent=get_maya_main_win())
        self._set_win()
        self._define_widgets()
        self._layout_widgets()
        self._connect_signals_slots()

    def _set_win(self):
        """Window Settings"""
        self.setWindowTitle("Transfer Animation Tool")
        self.resize(400, 150)

    def _define_widgets(self):
        self.inputText1_txt = QtWidgets.QLineEdit()
        self.rename_btn = QtWidgets.QPushButton("Rename")

    def _layout_widgets(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.inputText1_txt)
        self.main_layout.addWidget(self.rename_btn)
        self.setLayout(self.main_layout)

    def _connect_signals_slots(self):
        self.rename_btn.clicked.connect(self.rename)

    @QtCore.Slot()
    def rename(self):
        rename_asset(name_1=self.inputText1_txt.text())


def rename_asset(name_1=""):
    obj = cmds.ls(selection=True)

    for name in obj:
        cmds.rename(name, name_1)


window = MultipleRename()
window.show()

if __name__ == "__main__":
    pass


