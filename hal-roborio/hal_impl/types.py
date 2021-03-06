import ctypes as C
from hal.constants import kMaxJoystickAxes, kMaxJoystickPOVs

__all__ = [
    "ControlWord", "ControlWord_ptr",
    "JoystickAxes", "JoystickAxes_ptr",
    "JoystickPOVs", "JoystickPOVs_ptr",
    "JoystickButtons", "JoystickButtons_ptr",
    "JoystickDescriptor", "JoystickDescriptor_ptr",
    
    "Handle",
    "PortHandle",
    
    "AnalogInputHandle",
    "AnalogOutputHandle",
    "AnalogTriggerHandle",
    "CompressorHandle",
    "CounterHandle",
    "DigitalHandle",
    "DigitalPWMHandle",
    "EncoderHandle",
    "FPGAEncoderHandle",
    "GyroHandle",
    "InterruptHandle",
    "NotifierHandle",
    "RelayHandle",
    "SolenoidHandle",
]

#############################################################################
# HAL
#############################################################################

class ControlWord(C.Structure):
    _fields_ = [("enabled", C.c_uint32, 1),
                ("autonomous", C.c_uint32, 1),
                ("test", C.c_uint32, 1),
                ("eStop", C.c_uint32, 1),
                ("fmsAttached", C.c_uint32, 1),
                ("dsAttached", C.c_uint32, 1),
                ("control_reserved", C.c_uint32, 26)]
HALControlWord_ptr = C.POINTER(HALControlWord)

class JoystickAxes(C.Structure):
    _fields_ = [("count", C.c_uint16),
                ("axes", C.c_float * kMaxJoystickAxes)]
HALJoystickAxes_ptr = C.POINTER(HALJoystickAxes)

class JoystickPOVs(C.Structure):
    _fields_ = [("count", C.c_uint16),
                ("povs", C.c_int16 * kMaxJoystickPOVs)]
HALJoystickPOVs_ptr = C.POINTER(HALJoystickPOVs)

class JoystickButtons(C.Structure):
    _fields_ = [("buttons", C.c_uint32),
                ("count", C.c_uint8)]
HALJoystickButtons_ptr = C.POINTER(HALJoystickButtons)

class JoystickDescriptor(C.Structure):
    _fields_ = [("isXbox", C.c_uint8),
                ("type", C.c_uint8),
                ("name", C.c_char * 256),
                ("axisCount", C.c_uint8),
                ("axisTypes", C.c_uint8 * kMaxJoystickAxes),
                ("buttonCount", C.c_uint8),
                ("povCount", C.c_uint8)]
HALJoystickDescriptor_ptr = C.POINTER(HALJoystickDescriptor)

#############################################################################
# Handles
#############################################################################

kInvalidHandle = 0
Handle = C.c_int32

PortHandle = Handle

AnalogInputHandle = Handle
AnalogOutputHandle = Handle
AnalogTriggerHandle = Handle
CompressorHandle = Handle
CounterHandle = Handle
DigitalHandle = Handle
DigitalPWMHandle = Handle
EncoderHandle = Handle
FPGAEncoderHandle = Handle
GyroHandle = Handle
InterruptHandle = Handle
NotifierHandle = Handle
RelayHandle = Handle
SolenoidHandle = Handle

