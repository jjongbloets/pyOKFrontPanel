# -*- coding: utf-8 -*-
""" Classes
"""

import sys
import ctypes
import definitions as okd

if sys.platform.startswith('linux'):
    dll = ctypes.CDLL('libokFrontPanel.so')
elif sys.platform.startswith('win32'):
    dll = ctypes.CDLL('okFrontPanel')
#elif sys.platform.startswith('darwin'):
#    dll = ctypes.CDLL('libokFrontPanel')
else:
    raise Exception('Platform {0} not supported.'.format(sys.platform))
print(dll)


class PLL22150:
    def __init__(self):
        self._handle = dll.okPLL22150_Construct()

    def __del__(self):
        dll.okPLL22150_Destruct(self._handle)

    def SetCrystalLoad(self, capload):
        dll.okPLL22150_SetCrystalLoad(self._handle, float(capload))

    def SetReference(self, freq, extosc):
        dll.okPLL22150_SetReference(self._handle, float(freq), bool(extosc))

    def GetReference(self):
        return dll.okPLL22150_GetReference(self._handle)

    def SetVCOParameters(self, p, q):
        return dll.okPLL22150_SetVCOParameters(self._handle, int(p), int(q))

    def GetVCOP(self):
        return dll.okPLL22150_GetVCOP(self._handle)

    def GetVCOQ(self):
        return dll.okPLL22150_GetVCOQ(self._handle)

    def GetVCOFrequency(self):
        return dll.okPLL22150_GetVCOFrequency(self._handle)

    def SetDiv1(self, divsrc, n):
        dll.okPLL22150_SetDiv1(self._handle, divsrc, n)

    def SetDiv2(self, divsrc, n):
        dll.okPLL22150_SetDiv2(self._handle, divsrc, n)

    def GetDiv1Source(self):
        return dll.okPLL22150_GetDiv1Source(self._handle)

    def GetDiv2Source(self):
        return dll.okPLL22150_GetDiv2Source(self._handle)

    def GetDiv1Divider(self):
        return dll.okPLL22150_GetDiv1Divider(self._handle)

    def GetDiv2Divider(self):
        return dll.okPLL22150_GetDiv2Divider(self._handle)

    def SetOutputSource(self, output, clksrc):
        dll.okPLL22150_SetOutputSource(self._handle, output, clksrc)

    def SetOutputEnable(self, output, enable):
        dll.okPLL22150_SetOutputEnable(self._handle, output, enable)

    def GetOutputSource(self, output):
        dll.okPLL22150_GetOutputSource(self._handle, output)

    def GetOutputFrequency(self, output):
        dll.okPLL22150_GetOutputFrequency(self._handle, output)

    def IsOutputEnabled(self, output):
        return dll.okPLL22150_IsOutputEnabled(self._handle, output)

    def InitFromProgrammingInfo(self, info):
        buf = ctypes.create_string_buffer()
        dll.okPLL22150_InitFromProgrammingInfo(self._handle, buf)

    def GetProgrammingInfo(self):
        buf = ctypes.create_string_buffer()
        dll.okPLL22150_GetProgrammingInfo(self._handle, buf)
        return buf.value


class PLL22393:
    def __init__(self):
        self._handle = dll.okPLL22393_Construct()

    def __del__(self):
        dll.okPLL22393_Destruct(self._handle)

    def SetCrystalLoad(self, capload):
        dll.okPLL22393_SetCrystalLoad(self._handle, capload)

    def SetReference(self, freq):
        dll.okPLL22393_SetReference(self._handle, freq)

    def GetReference(self):
        return dll.okPLL22393_GetReference(self._handle)

    def SetPLLParameters(self, n, p, q, enable):
        return dll.okPLL22393_SetPLLParameters(self._handle, n, p, q, enable)

    def SetPLLLF(self, n, lf):
        return dll.okPLL22393_SetPLLLF(self._handle, n, lf)

    def SetOutputDivider(self, n, div):
        return dll.okPLL22393_SetOutputDivider(self._handle, n, div)

    def SetOutputSource(self, n, clksrc):
        return dll.okPLL22393_SetOutputSource(self._handle, n, clksrc)

    def SetOutputEnable(self, n, enable):
        dll.okPLL22393_SetOutputEnable(self._handle, n, enable)

    def GetPLLP(self, n):
        return dll.okPLL22393_GetPLLP(self._handle, n)

    def GetPLLQ(self, n):
        return dll.okPLL22393_GetPLLQ(self._handle, n)

    def GetPLLFrequency(self, n):
        return dll.okPLL22393_GetPLLFrequency(self._handle, n)

    def GetOutputDivider(self, n):
        return dll.okPLL22393_GetOutputDivider(self._handle, n)

    def GetOutputSource(self, n):
        return dll.okPLL22393_GetOutputSource(self._handle, n)

    def GetOutputFrequency(self, n):
        return dll.okPLL22393_GetOutputFrequency(self._handle, n)

    def IsOutputEnabled(self, n):
        return dll.okPLL22393_IsOutputEnabled(self._handle, n)

    def IsPLLEnabled(self, n):
        return dll.okPLL22393_IsPLLEnabled(self._handle, n)

    def InitFromProgrammingInfo(self, info):
        buf = ctypes.create_string_buffer()
        dll.okPLL22393_InitFromProgrammingInfo(self._handle, buf)

    def GetProgrammingInfo(self):
        buf = ctypes.create_string_buffer()
        dll.okPLL22393_GetProgrammingInfo(self._handle, buf)
        return buf.value

class DeviceSensors:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def Construct(self):
        pass

    def Destruct(self):
        pass

    def GetSensorCount(self):
        pass

    def GetSensor(self, n):
        pass

class FirmwarePackage:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def Load(filename):
        pass

    def Destruct(self):
        pass

    def GetFirmwareCount(self):
        pass

    def GetFirmware(self, num):
        pass

class FrontPanelManager:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def StartMonitoring(self):
        pass

    def Open(self, serial):
        pass

class FrontPanelDevices:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def GetCount(self):
        pass

    def GetSerial(self, num, buf):
        pass

    def Open(self, serial):
        pass


class FrontPanel:
    """Main wrapper class for controlling the Opal Kelly FPGA-Board."""
    def __init__(self):
        self._handle = dll.okFrontPanel_Construct()

    def __del__(self):
        self._handle = dll.okFrontPanel_Destruct(self._handle)

    def GetErrorString(self, ec):
        """int okFrontPanel_GetErrorString(int ec, char *buf, int length);"""
        buf = ctypes.create_string_buffer(okd.MAX_ERROR_NAME_LENGTH)
        dll.okFrontPanel_GetErrorString(ec,ctypes.byref(buf), okd.MAX_ERROR_NAME_LENGTH)
        return buf.value.decode() # converts byte to string

    def AddCustomDevice(matchInfo, devInfo):
        pass

    def RemoveCustomDevice(productID):
        pass

    def WriteI2C(self, addr, length, data):
        pass

    def ReadI2C(self, addr, length, data):
        pass

    def FlashEraseSector(self, address):
        pass

    def FlashWrite(self, address, length, buf):
        pass

    def FlashRead(self, address, length, buf):
        pass

    def GetFPGAResetProfile(self, method, profile):
        pass

    def GetFPGAResetProfileWithSize(self, method, profile, size):
        pass

    def SetFPGAResetProfile(self, method, profile):
        pass

    def SetFPGAResetProfileWithSize(self, method, profile, size):
        pass

    def ReadRegister(self, addr, data):
        pass

    def ReadRegisters(self, num, regs):
        pass

    def WriteRegister(self, addr, data):
        pass

    def WriteRegisters(self, num, regs):
        pass

    def GetHostInterfaceWidth(self):
        pass

    def IsHighSpeed(self):
        pass

    def GetBoardModel(self):
        pass

    def GetBoardModelString(self, model=0):
        #buf = ctypes.create_string_buffer(self.OK_MAX_BOARD_MODEL_STRING_LENGTH)
        #self._dll.okFrontPanel_GetBoardModelString(model,ctypes.byref(buf))
        #return buf.value.decode() # converts byte to string
        return self.ok_BoardModel(model).name

    def GetDeviceCount(self):
        """int okFrontPanel_GetDeviceCount(okFrontPanel_HANDLE hnd);"""
        count = self._dll.okFrontPanel_GetDeviceCount(self._handle)
        return count

    def GetDeviceListModel(self, num):
        pass

    def GetDeviceListSerial(self, num, buf):
        pass

    def OpenBySerial(self, serial=""):
        """ok_ErrorCode okFrontPanel_OpenBySerial(okFrontPanel_HANDLE hnd, const char *serial);"""
        return self.check(self._dll.okFrontPanel_OpenBySerial(self._handle, serial.encode()))

    def IsOpen(self):
        pass

    def EnableAsynchronousTransfers(self, enable):
        pass

    def SetBTPipePollingInterval(self, interval):
        pass

    def SetTimeout(self, timeout):
        pass

    def GetDeviceMajorVersion(self):
        pass

    def GetDeviceMinorVersion(self):
        pass

    def ResetFPGA(self):
        pass

    def Close(self):
        """void okFrontPanel_Close(okFrontPanel_HANDLE hnd);"""
        self._dll.okFrontPanel_Close(self._handle)

    def GetSerialNumber(self, buf):
        pass

    def GetDeviceSensors(self, settings):
        pass

    def GetDeviceSettings(self, settings):
        pass

    def GetDeviceInfo(self, info):
        pass

    def GetDeviceInfoWithSize(self, info, size):
        pass

    def GetDeviceID(self, buf):
        pass

    def SetDeviceID(self, strID):
        pass

    def ConfigureFPGA(self, strFilename):
        """ok_ErrorCode okFrontPanel_ConfigureFPGA(okFrontPanel_HANDLE hnd, const char *strFilename);"""
        return self.check(self._dll.okFrontPanel_ConfigureFPGA(self._handle, strFilename.encode()))

    def ConfigureFPGAWithReset(self, strFilename, reset):
        pass

    def ConfigureFPGAFromMemory(self, data, length):
        pass

    def ConfigureFPGAFromMemoryWithReset(self, data, length, reset):
        pass

    def ConfigureFPGAFromFlash(self, configIndex):
        pass

    def GetPLL22150Configuration(self, pll):
        pass

    def SetPLL22150Configuration(self, pll):
        pass

    def GetEepromPLL22150Configuration(self, pll):
        pass

    def SetEepromPLL22150Configuration(self, pll):
        pass

    def GetPLL22393Configuration(self, pll):
        pass

    def SetPLL22393Configuration(self, pll):
        pass

    def GetEepromPLL22393Configuration(self, pll):
        pass

    def SetEepromPLL22393Configuration(self, pll):
        pass

    def LoadDefaultPLLConfiguration(self):
        pass

    def IsFrontPanelEnabled(self):
        """Bool okFrontPanel_IsFrontPanelEnabled(okFrontPanel_HANDLE hnd);"""
        bool_val = self._dll.okFrontPanel_ConfigureFPGA(self._handle)
        return True if (bool_val == 0) else False

    def IsFrontPanel3Supported(self):
        pass

    def UpdateWireIns(self):
        """void okFrontPanel_UpdateWireIns(okFrontPanel_HANDLE hnd);"""
        self._dll.okFrontPanel_UpdateWireIns(self._handle)

    def GetWireInValue(self, epAddr, val):
        """ok_ErrorCode okFrontPanel_GetWireInValue(okFrontPanel_HANDLE hnd, int epAddr, UINT32 *val);"""
        pass

    def SetWireInValue(self, ep, val, mask):
        """ok_ErrorCode okFrontPanel_SetWireInValue(okFrontPanel_HANDLE hnd, int ep, unsigned long val, unsigned long mask);"""
        pass

    def UpdateWireOuts(self):
        """void okFrontPanel_UpdateWireOuts(okFrontPanel_HANDLE hnd);"""
        self._dll.okFrontPanel_UpdateWireOuts(self._handle)

    def GetWireOutValue(self, epAddr):
        """unsigned long okFrontPanel_GetWireOutValue(okFrontPanel_HANDLE hnd, int epAddr);"""
        pass

    def ActivateTriggerIn(self, epAddr, bit):
        pass

    def UpdateTriggerOuts(self):
        """void okFrontPanel_UpdateTriggerOuts(okFrontPanel_HANDLE hnd);"""
        self._dll.okFrontPanel_UpdateTriggerOuts(self._handle)

    def IsTriggered(self, epAddr, mask):
        pass

    def GetLastTransferLength(self):
        pass

    def WriteToPipeIn(self, epAddr, length, data):
        pass

    def ReadFromPipeOut(self, epAddr, length, data):
        pass

    def WriteToBlockPipeIn(self, epAddr, blockSize, length, data):
        pass

    def ReadFromBlockPipeOut(self, epAddr, blockSize, length, data):
        pass
