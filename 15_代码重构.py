# 1. 导入相关库
import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm

# 2. 封装到类中
class CoronaVirusSpider(object):

    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_content_from_url(self, url):
        """
        根据URL获取响应的字符串数据
        :param url:请求的URL
        :return:响应内容的字符串
        """
        response = requests.get(url)
        home_page = response.content.decode()
        return home_page

    def parse_home_page(self, home_page):
        """
        解析首页内容，获取解析后的python数据
        :param home_page: 首页的内容
        :return: 解析后的python数据
        """
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id="getListByCountryTypeService2true")
        text = script.string
        json_str = re.findall(r'\[.+\]', text)[0]
        data = json.loads(json_str)
        return data

    def save(self, data, path):
        with open(path, 'w', encoding='utf8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    def crawl_last_day_corona_virus(self):
        """
        采集最近一天各国疫情信息
        :return:
        """
        # 1. 获得首页内容
        home_page = self.get_content_from_url(self.home_url)
        # 2. 解析首页内容
        last_day_corona_virus = self.parse_home_page(home_page)
        # 3. 保存数据
        self.save(last_day_corona_virus, 'data/last_day_corona_virus.json')

    def crawl_corona_virus(self):
        """
        采集各国从1月23日以来的疫情数据
        :return:
        """
        # 1. 加载各国疫情数据
        with open('data\last_day_corona_virus.json', encoding='utf8') as fp:
            last_day_corona_virus = json.load(fp)

        # 定义列表用于储存
        corona_virus = []
        # 2. 遍历各国疫情数据，获取统计的URL
        for country in tqdm(last_day_corona_virus,'采集1月23日以来的各国疫情信息'):
            # 3. 发送请求，获取各国从1月23日至今的json数据
            statistics_data_url = country['statisticsData']
            # print(statistics_data_url)
            statistics_data_json_str = self.get_content_from_url(statistics_data_url)
            # print(statistics_data_json_str)
            # 4. 把json数据转换为python类型的数据，添加到列表中
            statistics_data = json.loads(statistics_data_json_str)['data']
            # print(statistics_data)
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
                one_day['countryShortCode'] = country['countryShortCode']
            # print(statistics_data)
            corona_virus.extend(statistics_data)

        # 5. 把列表以json格式文件保存
        self.save(corona_virus,'data/corona_virus.json')

    def run(self):
        # self.crawl_last_day_corona_virus()
        self.crawl_corona_virus()


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()
