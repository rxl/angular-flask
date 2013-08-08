import sys
import os

#hack around absolute paths
current_dir =  os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(current_dir + "/../")
	
#make sure the parent_dir is in the path
sys.path.insert(0, parent_dir)

from angular_flask import app as application