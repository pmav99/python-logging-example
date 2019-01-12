import logging


logger = logging.getLogger(__name__)
logger.debug("Logging from subpkg1!")

from .a import func_a
from .b import func_b


func_a()
func_b()
