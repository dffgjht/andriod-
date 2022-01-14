import uiautomator2 as u2
import time,os,datetime
from uiautomator2 import xpath
import random
import re
try:
  os.popen(r'"D:\Program Files\Microvirt\MEmu\MEmu.exe" MEmu_1','r')#填写模拟器所在位置路径
  time.sleep(30)
except:
  pass
while 1:
    try:
        d = u2.connect('127.0.0.1:21513')#填写对应模拟器端口号
        print(d.info)
        d.unlock()
        break
    except:
        os.system('adb kill-server')
        os.system('adb start-server')
        os.system('adb connect 127.0.0.1:21513')
d.app_start('cn.xuexi.android')
time.sleep(3)
def dl(user,pwd):
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

def part1():#浏览文章
    print('文章浏览开始...')
    try:
        d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
        d(text="成长总积分").exists(timeout=5)
        d.swipe_ext('up')   
        time.sleep(1)
    except:
        pass
    while True:
        try:
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
            else:
                print('文章阅读完毕')
                break
        except Exception as e3:
            print(e3)
            break
    

def part2():#视频学习以百灵观看为主
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


def part3():#每日答题部分，每周答题目前暂不做，需要加日期判断，本人懒，目前不想弄
    try:
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
                        if  d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]').exists:
                            d.xpath('//*[@resource-id="app"]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]').click()
                            os.system('adb shell input text {}'.format(random.choice('qwertyuiopasdfghjklzxcvbnm')))#填空题随机填写一个字母，肯定会错的，多做几次，累计拿满5分为止
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
            finally:
                try:
                    while d(text="退出").exists():
                        d(text="退出").click()
                except:
                    pass
        print('答题结束')
        os.system('adb shell input keyevent 4')

    except Exception as e6:
        print(e6)
        os.system('adb shell input keyevent 4')

def part4():#主程序部分，判断是否拿满30分以上，30分以上停止学习
    while True:
        try:
            d(resourceId="cn.xuexi.android:id/comm_head_xuexi_score").click()
        except:
            pass
        time.sleep(5)
        try:
            jf=d(textContains='今日已累积').get_text()
            print(jf)
            j=re.compile('\d+')
            jfs=j.match(jf,6).group()
            if int(jfs) >=30:
                print('今日已满30分','目前积分数：',jfs)           
                break
            else:
                part3()
                part1()
                part2()

        except Exception as e2:
            try:
                d(text='学习强国').click()
            except:
                pass
            print(e2)

users=['']#后面加账号记得用英文逗号隔开，统一用英文单引号引用
pwds=['']
try:
    for i in range(len(users)):#账号轮流替换学习，减少多开程序的烦恼
        dl(users[i],pwds[i])
        part4()
        os.system('adb shell input keyevent 4')
        time.sleep(0.5)
        d(text='我的').click()
        d(resourceId="cn.xuexi.android:id/my_setting").click()
        time.sleep(0.2)
        d(resourceId="cn.xuexi.android:id/uidic_forms_item_text", text="退出登录").click()
        time.sleep(0.2)
        d(resourceId="android:id/button1").click()
    print('恭喜，学习完毕')
except:
    print('有未知力量干扰您的学习')

print('即将关闭程序。。。') 
d.app_stop_all()
os.system('taskkill /F /IM MEmu.exe /T')
