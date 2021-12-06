import uiautomator2 as u2
import time,os
import win32api
try:
  win32api.ShellExecute(0,'open',r'D:\Program Files\Microvirt\MEmu\MEmu.exe','','',1)
  for ii in range(15):
        time.sleep(1)
        print(15-ii,end='')
except:
  pass
user=['']#你的浙政钉账号
password=['']#你的浙政钉密码
d = u2.connect('127.0.0.1:21503')
print(d.info)
d.unlock()
p=open('./签到日志.txt','a')
for i in range(2):   
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
        d(textContains="签到签退").exists(timeout=10)
        d(textContains="签到签退").click()
        time.sleep(3)
    except:
        print('智慧办公签到系统异常')
    try:
        time.sleep(1)
        d.xpath('//android.widget.ListView/android.view.View[4]').click()
    except:
        print('点击签到失败')
        p.write(user[i],'点击签到失败',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        p.write('\n')        
    try:
        t=d.xpath('//*[@resource-id="form"]/android.view.View[5]').text
        print(t)
        time.sleep(10)
        if '异常'   in t:
            print('异常签到-1')         
            time.sleep(3)
        elif d(resourceId="button").exists():
            d(resourceId="button").click()
            time.sleep(1)
            print('签到成功')
            p.write(user[i],'值班签到成功',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
            p.write('\n')
    except:
        print('点击签到失败')
    finally:
        while d(text='返回').exists():
            time.sleep(0.5)
            d(text='返回').click()

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
p.close()
d.app_stop_all()
os.system('taskkill /F /IM MEmu.exe /T')