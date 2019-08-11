"""
Do not edit using from a template
"""

import os
import sys

python = sys.executable

build_cmd = "setup.py sdist bdist_wheel"
cmd_build = " ".join([python, build_cmd])

deploy_cmd = "-m twine upload dist/*"
cmd_deploy = " ".join([python, deploy_cmd])

script_dir = os.path.dirname(os.path.realpath(__file__))

os.system(cmd_build)
os.system(cmd_deploy)
