"""
Do not edit using from a template
"""

import os
import sys

python = sys.executable
install_cmd = "setup.py install"
script_dir = os.path.dirname(os.path.realpath(__file__))

cmd_install = " ".join([python, install_cmd])
os.system(cmd_install)
