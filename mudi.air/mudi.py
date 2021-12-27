# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)
from airtest.aircv import *
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.settings import Settings as ST

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

dev = connect_device("android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH")

def match_in_predict_area(template,screen=None,rect=None):
    if screen is None:
        screen=G.DEVICE.snapshots()
    if rect is None:
        return template.match_in(screen)
    if not isinstance(rect,(list,tuple)):
        raise Exception("crop a image,rect should be a list")
    else:
        predict_screen=aircv.crop_image(screen,rect)
        focus_pos=template.match_in(predict_screen)
        if not focus_pos:
            return False
        else:
            return focus_pos[0]+rect[0],focus_pos[1]+rect[1]


def mutiple_exists(targets,area=None,threshold=0.80,rgb=False,inti=5):
    if (G.DEVICE.display_info['orientation']%2):
        height=G.DEVICE.display_info['height']
        width=G.DEVICE.display_info['width']
    else:
        height = G.DEVICE.display_info['height']
        width = G.DEVICE.display_info['width']
    for i in range(inti):
        fullScreen=G.DEVICE.snapshot()
        for target in targets:
            if target:
                focus_pos=match_in_predict_area(target, fullScreen,area)
                if focus_pos:
                    ref=targets.index(target)
                    return ref,focus_pos
        sleep(0.2)
    return -1,None


def wait_click(temp_list, disapear=True):
    if type(temp_list) is not list:
        temp_list = [temp_list]
    res = False
    while True:
        ref, pos = mutiple_exists(temp_list)
        
        if ref > -1:
            touch(pos)
            res = True
            sleep(2)
            if disapear == False:
                return res
        else:
            return res
#         for temp in temp_list:
#             pos =  exists(temp)
#             if pos:
#                 try:
#                     touch(pos)
#                     find = True
#                     sleep(2)
#                 except:
#                     pass
#         if find == False:
#             return

        
def click_dialog():
    wait_click(Template(r"tpl1622893722615.png", record_pos=(0.369, 0.618), resolution=(900, 1600)))
    wait_click(Template(r"tpl1622984198757.png", record_pos=(0.369, 0.618), resolution=(900, 1600)))

    wait_click(Template(r"tpl1622895401210.png", record_pos=(-0.322, 0.137), resolution=(900, 1600)))

wait_click(Template(r"tpl1623139637227.png", record_pos=(-0.24, -0.021), resolution=(900, 1600)))
    
# click_dialog()
# wait_click(Template(r"tpl1622984917583.png", record_pos=(0.371, 0.618), resolution=(900, 1600)))
# wait_click(Template(r"tpl1622981912990.png", record_pos=(0.356, 0.154), resolution=(900, 1600)))
# sleep(5)
# keyevent("KEYCODE_BACK")
# sleep(5)
# keyevent("KEYCODE_BACK")
# count = 0
# while not exists(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))) and count < 12:
#     sleep(10)
#     count += 1
# wait_click(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600)))
# sleep(60*15)



# -*- encoding=utf8 -*-
__author__ = "Administrator"

auto_setup(__file__)
import airtest
from airtest.core.settings import Settings as ST
from util import *
import sys
#只能在未连接模拟器时使用
# dev = connect_device("Android:///")
ST.LOG_FILE = "log.txt"
# ST.CVSTRATEGY = ['tpl']
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




def getBonus():
    click_dialog()
    wait_click(Template(r"tpl1622984917583.png", record_pos=(0.371, 0.618), resolution=(900, 1600)), 3)
    
    if exists(Template(r"tpl1623147781059.png", record_pos=(0.291, 0.178), resolution=(900, 1600))):

        wait_click(Template(r"tpl1623147781059.png", record_pos=(0.291, 0.178), resolution=(900, 1600)), 3, False)
        count = 0

        while not exists(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))) and count < 12: 
#             keyevent("KEYCODE_BACK")
            count += 1
            sleep(10)

            
        if not wait_click([Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600))], 3):
            sys.stderr.write("can't find close advertisement")
            touch((71,62))
            print(f"touch (71,62)")
        wait_click([Template(r"tpl1623229848480.png", record_pos=(0.267, 0.811), resolution=(900, 1600)),Template(r"exit2.png", resolution=(900, 1600))], 3)
        sleep(5)
        wait_click(Template(r"tpl1622981974455.png", record_pos=(-0.422, -0.826), resolution=(900, 1600)), 1)
        click_dialog()
        for i in range(11):
            sleep(60)
            print(f"waited for {i+1} minutes")
        return True
    else:
        return False

def collect_rice():
#     click_dialog()
    wait_click([Template(r"tpl1623229848480.png", record_pos=(0.267, 0.811), resolution=(900, 1600)),Template(r"exit2.png", resolution=(900, 1600))], 3)


while True:
    try:
        dev = connect_device("android://127.0.0.1:5037/127.0.0.1:62025?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH")
        break
    except Exception as e:
        print(e)
        print("Try to connect the device after 10s")
        sleep(10)

for i in range(1):
    try:
#         check_start()
#         sleep(5)
        collect_rice()
        
    except Exception as e:
        print("error", str(e))
        if type(e) is airtest.core.error.AdbShellError:
            sys.stderr.write("需要重启模拟器")
            break
        pass
    