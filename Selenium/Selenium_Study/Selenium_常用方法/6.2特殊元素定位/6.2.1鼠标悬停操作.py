# 在selenium中将键盘鼠标操作封装在 ActionChains中
# 1. click(on_element=None) 模拟鼠标单击操作
# 2. click_and_hold(on_element=None)) 模拟鼠标单击而且按住不放
# 3. double_click(on_element=None) 模拟鼠标双击
# 4. context_click(on_element=None) 模拟鼠标右击
# 5. drag_and_drop(source,target) 模拟鼠标拖拽
# 6. drag_and_drop(source,xoffset,yoffset) 模拟将目标拖拽到目标位置
# 7. key_down(value,element=None) 按住某个按键，实现快捷操作
# 8. key_up(value,element=None) 模拟松开某个键，一般和key_down一起使用
# 9. move_to_element(to_elemrnt) 模拟将鼠标移到指定的某个页面元素
# 10. move_to_element_with_offset(to_element,xoffset,yoffset) 移动鼠标至指定坐标
# 11. perform() 将之前一系列的ActionChains执行
# 12. release(on_element=None) 释放按下的鼠标

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# move_to_element()方法
def main():
    browser_driver = webdriver.Chrome()
    browser_driver.maximize_window()
    browser_driver.get('https://www.baidu.com')
    bg_config = browser_driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
    # 模拟将鼠标悬停在超链接‘设置’处
    ActionChains(browser_driver).move_to_element(bg_config).perform()
    # 鼠标悬停时，定位元素，超链接‘搜索设置’，然后实现单击操作
    browser_driver.find_element_by_link_text('搜索设置').click()
    browser_driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div/div/ul/li[2]').click()
    time.sleep(5)
    browser_driver.quit()

if __name__ == '__main__':
    main()