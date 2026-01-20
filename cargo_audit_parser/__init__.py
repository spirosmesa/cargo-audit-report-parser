from pathlib import Path
from os.path import join
import logging

log_output_dir = join(str(Path(__file__).parent), "log_output")
log_output_name = join(log_output_dir, "cargo_audit_parser.log")

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S")
handler = logging.FileHandler(log_output_name, 'w+')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.propagate = False
