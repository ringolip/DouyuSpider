from selenium import webdriver
import json

"""
实现了爬取斗鱼网页信息的大框架
"""

class DouyuSpider():
    def __init__(self):
        self.start_url = "https://www.douyu.com/g_DNF"
        self.driver = webdriver.Chrome()

    def get_live_rooms(self):
        live_room_lists = self.driver.find_elements_by_xpath('.//ul[@id="live-list-contentbox"]/li')
        print(live_room_lists)
        for live_room in live_room_lists:
            item = {}
            item['live_room_title'] = live_room.find_element_by_xpath('.//div[@class="mes-tit"]/h3').text
            print(item)

    def get_next_page_link(self):
        next_url = self.driver.find_elements_by_xpath('.//a[@class="shark-pager-next"]')
        next_url = next_url[0] if len(next_url) > 0 else None # 判断是否是最后一页
        return next_url


    def run(self):
        self.driver.get(self.start_url)
        self.get_live_rooms()
        #发送请求
        next_url = self.get_next_page_link()
        while next_url is not None: # 循环爬取全部页面
            next_url.click()
            self.get_live_rooms()
            next_url = self.get_next_page_link()


        #获取数据
        #提取各个直播间信息
    
        #保存

if __name__ == "__main__":
    douyu = DouyuSpider()
    douyu.run()