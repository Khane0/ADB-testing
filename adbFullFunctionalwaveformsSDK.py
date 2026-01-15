from ctypes import *
import sys


#-----load waveforms sdk - this is from chat----
if sys.platform.startswith("win"):
    dwf = cdll.dwf
elif sys.platform.startswith("darwin"):
    dwf = cdll.LoadLibrary("/Library/Frameworks/dwf.framework/dwf")
else:
    dwf = cdll.LoadLibrary("libdwf.so")

hdwf = c_int()

if dwf.FDwfDeviceOpen(c_int(-1), byref(hdwf)) == 0:
    print("error: no device found")
    sys.exit(1)
#------end of chat seg--------

print("AD3 opened successfully")

#config. channel
channel = 0          # W1
freq = 1000.0     # Hz
amp = 1.0         # voltage
offset = 0.0        #no offset

#ref manual, API functions
#https://digilent.com/reference/software/waveforms/waveforms-sdk/reference-manual?srsltid=AfmBOopnZMi4gTU3UorAPjyIwl9GfVMLqtnTCdv_NM6y_66s4Rjd_Rab
dwf.FDwfAnalogOutReset(hdwf, channel)

dwf.FDwfAnalogOutNodeEnableSet(
    hdwf, channel, c_int(0), c_bool(True)  #start editing channel W1
)

dwf.FDwfAnalogOutNodeFunctionSet(
    hdwf, channel, c_int(0), c_int(1)  #help from chat, to set sine func
)

dwf.FDwfAnalogOutNodeFrequencySet(
    hdwf, channel, c_int(0), c_double(freq) #set freq
)

dwf.FDwfAnalogOutNodeAmplitudeSet(
    hdwf, channel, c_int(0), c_double(amp) #set amp
)

dwf.FDwfAnalogOutNodeOffsetSet(
    hdwf, channel, c_int(0), c_double(offset) #set offset
)

dwf.FDwfAnalogOutConfigure(hdwf, channel, c_bool(True)) #turn channel W1 on

print("1 kHz sine wave running on W1")
print("press ENTER to stop")

input() #wait for keyboard input

dwf.FDwfAnalogOutConfigure(hdwf, channel, c_bool(False)) #close channel
dwf.FDwfDeviceClose(hdwf) #close device

print("device closed")

