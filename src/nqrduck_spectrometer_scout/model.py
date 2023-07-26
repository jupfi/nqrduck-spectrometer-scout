import logging
from nqrduck.module.module_model import ModuleModel

logger = logging.getLogger(__name__)

class ScoutModel(ModuleModel):

    def __init__(self, module) -> None:
        super().__init__(module)

    @property
    def ntnmr_app(self):
        return self._ntnmr_app
    
    @ntnmr_app.setter
    def ntnmr_app(self, value):
        self._ntnmr_app = value

    @property
    def ntnmr_document(self):
        return self._ntnmr_document
    
    @ntnmr_document.setter
    def ntnmr_document(self, value):
        self._ntnmr_document = value