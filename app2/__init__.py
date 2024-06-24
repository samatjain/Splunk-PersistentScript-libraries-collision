import sys
from pathlib import Path
libraries_path = Path(__file__).parent / "lib"
sys.path.append(str(libraries_path))

import m
m.doesnt_exist_in_app1_m()
