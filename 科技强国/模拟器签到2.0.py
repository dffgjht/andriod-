import uiautomator2 as u2
import time,os
import win32api
import random

def gt():
    dd=[]
    dtime=['7:30','8:30','12:00','14:00','17:30']
    now=time.localtime()
    today=time.strftime("%Y-%m-%d",now)
    for d in dtime:
        d=today+' '+d
        d=time.strptime(d,"%Y-%m-%d %H:%M")
        d=time.mktime(d)
        dd.append(d)
    t=time.mktime(now)
    if t>dd[0] and t<dd[1]:
        x=1
        print(x)
    elif t>dd[2] and t <dd[3]:
        x=2
        print(x)
    elif t>dd[4]:
        x=3
        print(x)
    else:
        x=None
        print('已过签到时间')
    return x

n=gt()


try:
  win32api.ShellExecute(0,'open',r'D:\Program Files\Microvirt\MEmu\MEmu.exe','','',1)
  for ii in range(15):
        time.sleep(1)
        print('\r',15-ii,end='')
except:
  pass

yc=random.randint(0,10*60)
for ycs in range(1,yc+1):
    time.sleep(1)
    print('\r倒计时开始：',yc-ycs,flush=True,end='')


user=['user']
password=['password']
while 1:
    try:
        d = u2.connect('127.0.0.1:21503')
        print(d.info)
        d.unlock()
        break
    except:
        os.system('adb connect 127.0.0.1:21503')

d.unlock()

for i in range(len(user)):  
    rz=[] 
    try:
        d.app_start('com.alibaba.taurus.zhejiang')
    except:
        print('程序启动失败或者已启动')
        pass
    time.sleep(3)
    try:
        d(resourceId="com.alibaba.taurus.zhejiang:id/account").clear_text()
        d(resourceId="com.alibaba.taurus.zhejiang:id/account").set_text(user[i])
        time.sleep(0.5)
        d(resourceId="com.alibaba.taurus.zhejiang:id/password").click()
        d(text='请输入密码').set_text(password[i])
        time.sleep(0.5)
        d(resourceId="com.alibaba.taurus.zhejiang:id/login").click()
        time.sleep(3)
    except:
        print('账号登陆失败或已登陆')

    try:
        d(text="工作台").click()
        time.sleep(3)
        d(text="平阳智慧办公平台").click()
        d(textContains="签到签退").exists(timeout=60)
        d(textContains="签到签退").click()
        time.sleep(3)
    except:
        print('智慧办公签到系统异常')
    try:
        time.sleep(1)
        d.xpath('//android.widget.ListView/android.view.View[{}]'.format(n)).click()
    except:
        print('点击签到失败')
        rz.append(user[i]+'点击签到失败'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))      
    try:
        t=d.xpath('//*[@resource-id="form"]/android.view.View[5]').text
        print(t)
        time.sleep(10)
        if '异常'   in t:
            print('异常签到-1') 
            rz.append('异常签到-1')    
            time.sleep(3)
        elif d(resourceId="button").exists():
            d(resourceId="button").click()
            time.sleep(1)
            print('签到成功')
            rz.append(user[i]+'╰(￣▽￣)╭签到成功'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))            
    except:
        print('点击签到失败')
    finally:
        while 2:           
            try:
                d(text='返回').click()
                time.sleep(0.5)
            except:
                break
    try:
        d(text='消息').click()
        d.xpath('//*[@resource-id="com.alibaba.taurus.zhejiang:id/session_list"]/android.view.ViewGroup[1]').click()
        d(resourceId="com.alibaba.taurus.zhejiang:id/et_sendmessage").click()
        if rz:
            d(resourceId="com.alibaba.taurus.zhejiang:id/et_sendmessage").set_text(rz[0])
            d(resourceId="com.alibaba.taurus.zhejiang:id/btn_send").click()
        else:
            rz.append('日志为空')
            d(resourceId="com.alibaba.taurus.zhejiang:id/et_sendmessage").set_text(rz[0])
            d(resourceId="com.alibaba.taurus.zhejiang:id/btn_send").click()           
        d(resourceId="com.alibaba.taurus.zhejiang:id/img_back").click()
       
    except:
        pass
    try:
        d(resourceId="com.alibaba.taurus.zhejiang:id/name", text="我的").click()
        time.sleep(0.5)
        d(text="账号与安全").click()
        time.sleep(1)
        while d(text='退出登录').exists():
            d(text='退出登录').click()
        print('账号退出成功')
    except:
        print('账号退出失败')
print('Done')
d.app_stop_all()
os.system('taskkill /F /IM MEmu.exe /T')