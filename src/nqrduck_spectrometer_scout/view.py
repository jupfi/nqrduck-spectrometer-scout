from PyQt6.QtWidgets import QWidget, QFileDialog
from nqrduck.module.module_view import ModuleView
from .widget import Ui_Form


class ScoutView(ModuleView):
    def __init__(self, module):
        super().__init__(module)

        widget = QWidget()
        self._ui_form = Ui_Form()
        self._ui_form.setupUi(self)
        self.widget = widget

        self._ui_form.loadfileButton.clicked.connect(self.load_file)

    def load_file(self):
        """Opens up a file dialog to select a file to load a pulse sequence from with the file ending .tnt"""

        file_name, _ = QFileDialog.getOpenFileName(
            self.widget, "Open File", "", "TNT Files (*.tnt)"
        )
        if file_name:
            self.module.controller.load_pulse_sequence(file_name)