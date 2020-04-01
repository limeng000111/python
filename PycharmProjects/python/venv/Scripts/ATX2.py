import uiautomator2 as u2

d=u2.connect()
d.debug=True
print(d.info)
# print(d.app_info('com.zjiec.sellingworld'))
# img = d.app_icon('com.zjiec.sellingworld')
# img.save('hahaha.png')
# print(img)
print(d.window_size())
print(d.current_app())
print(d.wlan_ip)
d.unlock()