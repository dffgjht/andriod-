import uiautomator2 as u2
import time,os,datetime
from uiautomator2 import xpath
import win32api
import random
try:
  win32api.ShellExecute(0,'open',r'D:\Program Files\Microvirt\MEmu\MEmu.exe','','',1)
  time.sleep(30)
except:
  pass
d = u2.connect('127.0.0.1:21503')
print(d.info)
d.unlock()
d.app_start('cn.xuexi.android')
time.sleep(3)
user=''#学习强国账号
pwd=''#学习强国密码
try:
    d(resourceId="cn.xuexi.android:id/et_phone_input").set_text(user)
    d(resourceId="cn.xuexi.android:id/et_pwd_login").set_text(pwd)
    d(text='登录').click()
    time.sleep(1)
    print('登录成功')
except:
    pass
    print('账号已登录')
now_time=datetime.datetime.now()
today=now_time.strftime('%Y-%m-%d')
yesterday=(now_time+datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
print(today)
def part1():
    print('看文章')
    try:
        d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
        d(text="成长总积分").exists(timeout=5)
        d.swipe_ext('up')   
        time.sleep(1)
        while d.xpath('//android.widget.ListView/android.view.View[2]/android.view.View[4]').get_text() == '去看看':
            d.xpath('//android.widget.ListView/android.view.View[2]/android.view.View[4]').click()
            time.sleep(2)
            d(text='新思想').click()
            time.sleep(1)
            for b in range(1,5):
                d.xpath('//android.widget.HorizontalScrollView/android.widget.LinearLayout[1]/android.widget.TextView[{}]'.format(b)).click()
                time.sleep(1)
                for bb in range(1,5):
                    try:
                        d.xpath('//android.widget.ListView/android.widget.FrameLayout[{}]'.format(bb)).click()
                        time.sleep(1)
                        print(d.xpath('//*[@resource-id="xxqg-article-header"]/android.view.View[1]').text)
                    except:
                        print('新思想查看失败')
                    try:
                        for i in range(20):
                            time.sleep(0.5)
                            d.swipe_ext('down')
                            time.sleep(0.5)
                            d.swipe_ext('up')
                        os.system('adb shell input keyevent 4')
                        time.sleep(1)
                    except Exception as e2:
                        print(e2)
    except Exception as e3:
        print(e3)
    

def part2():
    try:
        d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
        d(text="成长总积分").exists(timeout=5)
        d.swipe_ext('up')   
        time.sleep(1)
        while d.xpath('//android.widget.ListView/android.view.View[4]/android.view.View[4]').get_text() == '去学习':
            d.xpath('//android.widget.ListView/android.view.View[4]/android.view.View[4]').click()
            time.sleep(2)
            d.xpath('//*[@resource-id="cn.xuexi.android:id/home_bottom_tab_button_ding"]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]').click()
            for kk in range(1,11):
                d.xpath('//*[@resource-id="cn.xuexi.android:id/view_pager"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[{}]'.format(kk)).click()
                time.sleep(2.5)
                try:               
                    d.xpath('//android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
                    time.sleep(1)
                except:
                    pass
                try:
                    for i in range(60):
                        while d(text="点击重试").exists:
                            d(text="点击重试").click()
                        while d(text='重新播放').exists:
                            d(text='重新播放').click()
                        time.sleep(0.5) 
                    os.system('adb shell input keyevent 4')
                except Exception as e5:
                    print(e5,'视频播放失败')
                    os.system('adb shell input keyevent 4')
                time.sleep(1)    
            d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
            d(text="成长总积分").exists(timeout=5)
            d.swipe_ext('up')       
    except Exception as e:
        print(e)
        pass
        os.system('adb shell input keyevent 4')


def part3():
    try:
        win32api.ShellExecute(0,'open',r'D:\Program Files\Microvirt\MEmu\MEmu.exe','','',1)
        time.sleep(15)
    except:
        pass
    try:
        d.app_start('cn.xuexi.android')
        time.sleep(3)
    except:
        pass
    try:
        d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
        d(text="成长总积分").exists(timeout=5)
        d.swipe_ext('up')   
        time.sleep(1)
    except:
        pass
    try:
        while d.xpath('//android.widget.ListView/android.view.View[5]/android.view.View[4]').get_text() == '去答题':
            d.xpath('//android.widget.ListView/android.view.View[5]/android.view.View[4]').click()
            time.sleep(1)
            for i in range(7):  
                if d(text="多选题").exists:         
                    try:
                        d.xpath('//android.widget.ListView/android.view.View[1]').click()
                        d.xpath('//android.widget.ListView/android.view.View[2]').click()
                        if d.xpath('//android.widget.ListView/android.view.View[3]').exists:
                            d.xpath('//android.widget.ListView/android.view.View[3]').click()
                        if d.xpath('//android.widget.ListView/android.view.View[4]').exists:
                            d.xpath('//android.widget.ListView/android.view.View[4]').click()
                        else:
                            pass
                        time.sleep(1)
                    except Exception as e:
                        print(e)
                        pass
                elif d(text="单选题").exists: 
                    try:
                        d(text='查看提示').click()
                        time.sleep(2)
                        a=d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View[1]').text
                        print(d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View[1]').text)
                        os.system('adb shell input keyevent 4')
                        for ii in range(5):
                          try:
                            xx=d.xpath('//android.widget.ListView/android.view.View[{}]/android.view.View[1]/android.view.View[2]'.format(ii))
                            if xx.exists:
                                print(xx.text)
                                if xx.text in a:
                                    d.xpath('//android.widget.ListView/android.view.View[{}]'.format(ii)).click()
                                else:
                                    d.xpath('//android.widget.ListView/android.view.View[1]').click()
                            else:
                              pass
                          except:
                            pass
                    except Exception as e:
                        print(e)
                        pass
                elif d(text="填空题").exists:
                    try:
                        tt=[]
                        z1=[]
                        z2=[]
                        z3=[]
                        d2=[]
                        x1=d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]').text
                        x2=d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').text
                        x3=d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[3]').text

                        d(text='查看提示').click()
                        time.sleep(1)
                        tishi=d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View[1]').text
                        print(tishi)
                        os.system('adb shell input keyevent 4')
                        time.sleep(1)
                        if tishi=='请观看视频':
                            d.set_fastinput_ime(True) 
                            d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]').click()
                            d.send_keys(random.choice("学习强国")) # adb广播输入
                            d.set_fastinput_ime(False) # 切换成正常的输入法     
                        else:
                            for ti in tishi:
                                tt.append(ti)
                            for t1 in x1:
                                z1.append(t1)
                            for t2 in x2:
                                z2.append(t2)
                            for t3 in x3:
                                z3.append(t3)
                            try:                                 
                                for l in range(len(tt)): 
                                    if tt[l]==z1[-1]: 
                                        if tt[l-1]==z1[-2]:
                                            if tt[l-2]==z1[-3]:  
                                                if tt[l-3]==z1[-4]:
                                                    if tt[l-4]==z1[-5]:                                           
                                                        for ll in range(1,len(tt)-len(z1)-len(z3)+1):
                                                            d2.append(tt[l+ll])
                            except:
                                d.set_fastinput_ime(True) 
                                d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]').click()
                                d.send_keys(random.choice("学习强国")) # adb广播输入
                                d.set_fastinput_ime(False) # 切换成正常的输入法  
                            try: 
                                d.set_fastinput_ime(True) 
                                if len(d2)>0:
                                    print(d2)
                                    for k in range(len(d2)):
                                        if  d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[{}]'.format(k+1)).exists:
                                            d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[{}]'.format(k+1)).click()
                                        else:
                                            pass
                                        d.send_keys(d2[k]) # adb广播输入
                                d.set_fastinput_ime(False) # 切换成正常的输入法  
                            except:
                                pass
                                print('Guo')
                            finally:
                                d.set_fastinput_ime(False) # 切换成正常的输入法 
                    except Exception as e:
                        print(e)
                        pass
                time.sleep(1)
                try:
                    while  d(text='确定').exists():
                        d(text='确定').click()
                        time.sleep(1)
                    while d(text='下一题').exists():
                        d(text='下一题').click()
                        time.sleep(1)
                    while d(text='完成').exists():
                        d(text='完成').click()
                except Exception as dt:
                    print(dt)
            try:
                d(text="返回").click()
            except :
                pass
        print('答题结束')
        os.system('adb shell input keyevent 4')      
    except Exception as e6:
        print(e6)
        os.system('adb shell input keyevent 4')

part1()
part2()
part3()


print('Done') 
