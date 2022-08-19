# a part of pywinmm project
from .pywinmm import *
import os

if os.name != 'nt':
	raise Exception("pywinmm can't run on your operating system.")

def load(file):
	return player(file)
def loadrec():
	return player(rec=True)