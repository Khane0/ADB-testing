import pyvisa
from pyvisa.errors import VisaIOError
import time
import csv
from datetime import datetime
import sys
from ctypes import *

# Load Digilent WaveForms SDK
if sys.platform.startswith("win"):
    dwf = cdll.dwf
elif sys.platform.startswith("darwin"):
    dwf = cdll.LoadLibrary("/Library/Frameworks/dwf.framework/dwf")
else:
    dwf = cdll.LoadLibrary("libdwf.so")

hdwf = c_int()

if dwf.FDwfDeviceOpen(c_int(-1), byref(hdwf)) == 0:
    print("failed to open DWF device")
    sys.exit(1)
