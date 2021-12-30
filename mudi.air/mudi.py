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
    logger.info("start mudi")
    stop_app("com.nemoleoliu.OnePointThreeAcres")
    sleep(5)
    start_app("com.nemoleoliu.OnePointThreeAcres")
    sleep(10)
    
def stop():
    logger.info("stop mudi")
    stop_app("com.nemoleoliu.OnePointThreeAcres")


def click_dialog():

    wait_click([Template(r"tpl1623756901348.png", record_pos=(0.003, 0.134), resolution=(900, 1600)),Template(r"tpl1623368752644.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"yes.png", record_pos=(0.123, 0.077), resolution=(900, 1600)),Template(r"tpl1623020125057.png", record_pos=(-0.009, 0.079), resolution=(900, 1600)),Template(r"tpl1623019985426.png", record_pos=(0.0, -0.06), resolution=(900, 1600)),Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)), Template(r"tpl1622984198757.png", record_pos=(0.369, 0.618), resolution=(900, 1600)),Template(r"tpl1623368961771.png", record_pos=(0.372, 0.157), resolution=(900, 1600)),Template(r"tpl1623754255589.png", record_pos=(0.281, -0.371), resolution=(900, 1600))], 3)


def screenshot(errmsg):
    name = time.strftime('%Y-%m-%d') + '-' +errmsg
    import os
    name = f'{os.getcwd()}\\errscreen\\{name}.png'
    print(name)
    snapshot(filename=name,msg='massage')
def answer_question():
#     click_dialog()
#     pwait_click(textMatches="^.*" + '点楼层内\“举报\”' +".*$")
    #todo 刚打开界面找不到?
    if pwait_click(text='  点我答题') == True:
        found = False
        with open('vagueAnswers.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for answer in lines:
                answer = answer.strip()
                if not answer:
                    continue
                if answer[-1] == '\r':
                    answer = answer[:-1] #Remove return
                if pclick(textMatches="^.*" + answer +".*$"):
                    found = True
                    logger.info(f"Found {answer}")
                    break
        with open('exactAnswers.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for answer in lines:
                answer = answer.strip()
                if not answer:
                    continue
                if answer[-1] == '\r':
                    answer = answer[:-1] #Remove return
                if pclick(text=answer):
                    found = True
                    logger.info(f"Found {answer}")
                    break
        if found:
            pwait_click(text='提交')

        else:
            logger.info(f"Can't find answers!")
            screenshot('NoAnswer')
            wait_click('返回箭头', [Template(r"tpl1640781959530.png", record_pos=(-0.415, -0.789), resolution=(720, 1280))], 3)

def qiandao():
    if pwait_click(text='点我签到') == True:
        if pwait_click(text='输入心情') == True:
            text('加油找工作!')
            pwait_click(text='提交')
            

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
        check_start()
        if wait_click('设置', [Template(r"tpl1640876553072.png", record_pos=(0.4, 0.835), resolution=(720, 1280))], 2):
            sleep(3)
            answer_question()
            
            
        check_start()
        if wait_click('设置', [Template(r"tpl1640876553072.png", record_pos=(0.4, 0.835), resolution=(720, 1280))], 2):
            sleep(3)
            qiandao()
            
        stop()
        
    except Exception as e:
        print("error", str(e))
        if type(e) is airtest.core.error.AdbShellError:
            sys.stderr.write("需要重启模拟器")
            break
        pass
    