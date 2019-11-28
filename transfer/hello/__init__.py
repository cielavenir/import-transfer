import os
import sys

if sys.version_info[0]>=3:
    from importlib import reload

sys.path.insert(0,os.path.abspath(os.path.join(__file__,'..','..','..','real')))
import hello
reload(hello)
