from nqrduck_spectrometer.base_spectrometer import BaseSpectrometer
from .model import ScoutModel
from .view import ScoutView
from .controller import ScoutController

Scout = BaseSpectrometer(ScoutModel, ScoutView, ScoutController)