import logging
from nqrduck.module.module_model import ModuleModel

logger = logging.getLogger(__name__)

class ScoutModel(ModuleModel):

    def __init__(self, module) -> None:
        super().__init__(module)
