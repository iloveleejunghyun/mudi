# -*- encoding=utf8 -*-
__author__ = "Administrator"

auto_setup(__file__)
import airtest
from airtest.core.settings import Settings as ST
from util import *
import sys
import os
import logging
logger1=logging.getLogger("airtest")
logger1.setLevel(logging.INFO)
ST.LOG_FILE = "log.txt"
ST.THRESHOLD = 0.9
        
def check_start():
    if not exists(Template(r"tpl1623061463746.png", record_pos=(-0.438, -0.807), resolution=(900, 1600))):
        while True:
            
            stop_app("com.kairogame.android.Paddock2")
            sleep(5)
            start_app("com.kairogame.android.Paddock2")
            sleep(5)
            if wait_click(Template(r"tpl1623062470610.png", record_pos=(-0.161, 0.086), resolution=(900, 1600)),1, False):
                keyevent("KEYCODE_HOME")
                continue
            if not wait_click(Template(r"tpl1623061904200.png", record_pos=(0.243, 0.313), resolution=(900, 1600)), 10):
                continue

            sleep(20)

            if not wait_click(Template(r"tpl1623062004226.png", record_pos=(-0.002, 0.176), resolution=(900, 1600)), 10):
                continue

            break
    return True
       

def click_dialog():

    wait_click([Template(r"tpl1623756901348.png", record_pos=(0.003, 0.134), resolution=(900, 1600)),Template(r"tpl1623368752644.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"yes.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"tpl1623020125057.png", record_pos=(-0.009, 0.079), resolution=(900, 1600)),Template(r"tpl1623019985426.png", record_pos=(0.0, -0.06), resolution=(900, 1600)),Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)), Template(r"tpl1622984198757.png", record_pos=(0.369, 0.618), resolution=(900, 1600)),Template(r"tpl1623368961771.png", record_pos=(0.372, 0.157), resolution=(900, 1600)),Template(r"tpl1623754255589.png", record_pos=(0.281, -0.371), resolution=(900, 1600))], 3)


def answer_question():
#     click_dialog()
    if wait_click('每日答题选择选项',[Template(r"selections/54.png", record_pos=(0.267, 0.811), resolution=(720, 1280))], 3) == True:
    
        wait_click('每日答题提交',[Template(r"tpl1640621845691.png", record_pos=(0.426, -0.789), resolution=(720, 1280))], 3)

def qiandao():
    if wait_click('点我签到',[Template(r"tpl1640621993281.png", record_pos=(0.36, -0.79), resolution=(720, 1280))], 3) == True:
        if wait_click('输入心情',[Template(r"tpl1640622009941.png", record_pos=(-0.374, -0.274), resolution=(720, 1280))], 2) == True:
            text('加油找工作!')
            wait_click('提交',[Template(r"tpl1640621845691.png", record_pos=(0.426, -0.789), resolution=(720, 1280))], 3)
            

while True:
    try:
        dev = connect_device("android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH")
        break
    except Exception as e:
        print(e)
        print("Try to connect the device after 10s")
        sleep(10)

for i in range(1):
    try:
#         check_start()
#         sleep(5)
        qiandao()
#         answer_question()
        
    except Exception as e:
        print("error", str(e))
        if type(e) is airtest.core.error.AdbShellError:
            sys.stderr.write("需要重启模拟器")
            break
        pass
    