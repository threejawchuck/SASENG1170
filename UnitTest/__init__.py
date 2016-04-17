import os
import sys

# get the full parent path
parent_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../')

print parent_path
# add it to the beginning of the system path
sys.path.insert(0, parent_path); 

