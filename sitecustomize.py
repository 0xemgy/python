import sys
sys.path.insert(0, '')

import os

module_paths = os.environ.get("PYTHONPATH")
if module_paths:
    sys.path.extend(module_paths.split(";"))