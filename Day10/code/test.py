from selenium import webdriver
from time import sleep
import base64
import os
 
# 接入既有的浏览器进程
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)
 
# 取出页面的宽度和高度
page_width = driver.execute_script("return document.body.scrollWidth")
page_height = driver.execute_script("return document.body.scrollHeight")
save_path = os.path.join(r'D:\VScode\Crawler\Day10\output',r'test.png')
# 直接开启设备模拟，不要再手动开devtools了，否则截图截的是devtools的界面！
driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {'mobile':False, 'width':page_width, 'height':page_height, 'deviceScaleFactor': 1})
 
# 执行截图
res = driver.execute_cdp_cmd('Page.captureScreenshot', { 'fromSurface': True})
 
# 返回的base64内容写入PNG文件
with open(save_path, 'wb') as f:
    img = base64.b64decode(res['data'])
    print('writing...')
    f.write(img)
 
# 等待截图完成
print("wait...")
sleep(15)
 
# 关闭设备模拟
driver.execute_cdp_cmd('Emulation.clearDeviceMetricsOverride', {})
print('success!')
 