import logging
import win32com.client
from nqrduck_spectrometer.base_spectrometer_controller import BaseSpectrometerController
from nqrduck.module.module_controller import ModuleController

logger = logging.getLogger(__name__)

class ScoutController(BaseSpectrometerController):
    def __init__(self, module):
        super().__init__(module)

    def start_measurement(self):
        logger.debug("Starting measurement with spectrometer: %s", self.module.model.name)

    def load_pulse_sequence(self, file_name):
        logger.debug("Loading pulse sequence: %s", file_name)
        try:
            self.module.model.ntnmr_app = win32com.client.Dispatch('ntnmr.application')
        except Exception as e:
            logger.error(e)
            return
        
        try:
            self.module.model.ntnmr_document = win32com.client.Dispatch('ntnmr.document')
        except Exception as e:
            logger.error(e)
            return
        
        try:
            self.module.model.ntnmr_document.open(file_name)
        except Exception as e:
            logger.error(e)
            return
