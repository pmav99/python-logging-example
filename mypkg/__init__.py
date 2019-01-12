import logging


logger = logging.getLogger(__name__)
logger.debug("Logging from mypkg!")


from . import subpkg1
from . import subpkg2

