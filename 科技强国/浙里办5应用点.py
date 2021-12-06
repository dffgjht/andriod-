import uiautomator2 as u2
import time,os
import win32api
#python -m weditor#
try:
  win32api.ShellExecute(0,'open',r'D:\Program Files\Microvirt\MEmu\MEmu.exe','','',1)
  for ii in range(15):
        time.sleep(1)
        print(ii,end='.')
except:
  pass
time.sleep(3)
d = u2.connect('127.0.0.1:21503')
print(d.info)
d.unlock()
user=''#浙里办账号
pwd=''#浙里办密码
try:
    d.app_start('com.hanweb.android.zhejiang.activity')
except:
    print('程序启动失败或者已启动')
    pass
time.sleep(8)
try:
    d(resourceId="com.hanweb.android.zhejiang.activity:id/rl_user_password").set_text(user)
    d(resourceId="com.hanweb.android.zhejiang.activity:id/et_user_password").set_text(pwd)
    d(resourceId="com.hanweb.android.zhejiang.activity:id/tv_login").click()
except:
    pass
time.sleep(5)
try:
    d.click(0.695, 0.053)
    time.sleep(1)
    d.click(0.695, 0.053)
except:
    print('账号登陆失败')

yy=['']
xx=[]
for y in yy:
    try:
        d(resourceId="com.hanweb.android.zhejiang.activity:id/et_search").set_text(y)
        time.sleep(0.5)
        os.system('adb shell input keyevent 66')
        time.sleep(2)
        d(textContains='应用').click()
        time.sleep(10)
        print(y,' 打开成功 ')
        d(resourceId="com.hanweb.android.zhejiang.activity:id/iv_back").click()
        time.sleep(3)
        d(resourceId="com.hanweb.android.zhejiang.activity:id/et_search").clear_text()
    except:
        print(y,' 失败 ')
        xx.append(y)
while len(xx)!=0:
    for x in xx:
        try:
            d(resourceId="com.hanweb.android.zhejiang.activity:id/et_search").set_text(x)
            time.sleep(0.5)
            os.system('adb shell input keyevent 66')
            time.sleep(2)
            d(textContains='应用').click()
            time.sleep(10)
            print(x,' 打开成功 ',time.strftime('%Y-%m-%D %H:%M:%S',time.localtime()))
            xx.remove(x)
            d(resourceId="com.hanweb.android.zhejiang.activity:id/iv_back").click()
            time.sleep(3)
            d(resourceId="com.hanweb.android.zhejiang.activity:id/et_search").clear_text()
        except:
            print(x,' 失败 ')




print('Done')
