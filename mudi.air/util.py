# -*- encoding=utf8 -*-
__author__ = "Administrator"
# import os
# os.system("shutdown -r -t 60")
from airtest.core.api import *
from airtest.core.api import *
from airtest.aircv import *
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.settings import Settings as ST
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import os
import logging
# logger=logging.getLogger("airtest")
def initLog(level=logging.DEBUG,filename="pocoLog.txt"):
    '''初始化日志配置
    @param level:设置的日志级别。默认：DEBUG
    @param filename: 日志文件名。默认：当前目录下的pocoLog.txt，也可为绝对路径名
    '''
    logger = logging.getLogger(__name__.split('.')[0])    #日志名为当前包路径project.util.common的
    logger.setLevel(level)
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    streamHandler = logging.StreamHandler(sys.stderr) #输出到控制台
    fileHandler=logging.FileHandler(filename=filename,mode='a',encoding='utf-8',delay=False)
    LOG_FORMAT1='[%(asctime)s] [%(levelname)s] <%(name)s> (%(lineno)d) %(message)s'  
    LOG_FORMAT2='[%(asctime)s] [%(levelname)s] <%(name)s> <%(pathname)s]> (%(lineno)d) %(message)s'
    formatter1 = logging.Formatter(
        fmt=LOG_FORMAT1,
        datefmt='%Y-%m-%d  %H:%M:%S'
    )
    formatter2 = logging.Formatter(
        fmt=LOG_FORMAT2,
        datefmt='%Y-%m-%d  %H:%M:%S'
    )    
    streamHandler.setFormatter(formatter1)
    fileHandler.setFormatter(formatter2)
    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)
    #logger.debug('这里是测试用，initlog的logger的debug日志') 
def setPocoLog(name):
    '''设置poco日志配置'''
    pocoLogDIR= os.path.join(ST.PROJECT_ROOT, 'logDir') #poco日志目录
    pocoLogFile=os.path.join(pocoLogDIR,'pocoLog.txt')  #poco日志文件名
    initLog(level=logging.INFO,filename=pocoLogFile)    #poco日志初始化
    print(name)
    logger=logging.getLogger(name)
    return logger
logger = setPocoLog(__name__) #日志方法调用


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

import time
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
#                 print(time.time())
                if focus_pos:
                    ref=targets.index(target)
                    return ref,focus_pos
        sleep(0.2)
    return -1,None

def wait_click(name,temp_list, search_times=1, disapear=True, double=False):
    
    if type(temp_list) is not list:
        temp_list = [temp_list]
    res = False
    cur_times = 0
    ref = -1
    while cur_times < search_times:
        cur_times += 1
        ref, pos = mutiple_exists(temp_list)
        
        if ref > -1:
            if double:
                touch(pos)
                sleep(1)
            touch(pos)
            logger.info(f"touch {pos}, index = {ref}")
            res = True
            sleep(2)
            if disapear == False:
                return res
        else:
            if res == True: #如果之前找到了就返回。没有找到过就继续找. 这里无法处理多图重复出现之间时间间隔过大的情况
                break
        sleep(1)
    if res:
        logger.info(f"Found {name}")
    else:
        logger.info(f"Didn't find {name}")
    return res


def pclick(id = None, text = None, textMatches = None):
    try:
        if id != None:
            ele = poco(id)
            if ele:
                ele.click()     
                return True
         #   logger.info(f"Didn't Find {id}") 
        elif text != None:
            ele = poco(text = text)
            if ele:
                ele.click()
           #     logger.info(f"Found {text}")
                return True
           # logger.info(f"Didn't Find  {text}")
        else:
            ele = poco(textMatches = textMatches)
            if ele:
                ele.click()
           #     logger.info(f"Found {textMatches}")
                return True
           # logger.info(f"Didn't Find  {textMatches}")
    except Exception as e:
        logger.error(""+e)
    return False

def pwait_click(id = None, text = None, textMatches = None, times=2, disapear=True):
    res = False
    cur_res = False
    for i in range(times):
        cur_res = pclick(id, text, textMatches)
        if cur_res:
            if disapear == False:
                break
            res = cur_res
        else:
            if res: #如果之前找到了就返回。没有找到过就继续找. 这里无法处理多图重复出现之间时间间隔过大的情况
                break
        if i == times-1:
            break
        sleep(1)
    if res:
        if id:
            logger.info(f"Found {id}")
        elif text:
            logger.info(f"Found {text}")
        else:
            logger.info(f"Found {textMatches}")
    else:
        if id:
            logger.info(f"Didn't Find {id}")
        elif text:
            logger.info(f"Didn't Find {text}")
        else:
            logger.info(f"Didn't Find {textMatches}")
    return res

def pwait_until(id = None, text = None, textMatches = None, times = 10):
    if id == None and text == None:
        return True
    for _ in range(times):
        try:
            if id != None:
                if poco(id):
                    logger.info(f"Found {id}")
                    return True
            elif text != None:
                if poco(text = text):
                    logger.info(f"Found {text}")
                    return True
            else:
                if poco(textMatches = textMatches):
                    logger.info(f"Found {textMatches}")
                    return True
        except Exception as e:
            logger.error(""+e)
        sleep(1)
    if id != None:
        logger.info(f"Didn't Find {id}")
    elif text != None:
        logger.info(f"Didn't Find  {text}")
    else:
        logger.info(f"Didn't Find  {textMatches}")
    return False

def screenshot(errmsg):
    name = time.strftime('%Y%m%d %H%M%S') + '-' +errmsg
    
    if not os.path.exists('errscreen'):
        os.mkdir('errscreen')
    name = f'{os.getcwd()}\\errscreen\\{name}.png'
    print(name)
    snapshot(filename=name,msg='massage')