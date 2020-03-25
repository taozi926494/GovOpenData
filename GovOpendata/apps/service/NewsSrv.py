#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : NewsSrv.py
# @Time    : 2020-3-20 9:47
# @Software: PyCharm
# @Author  : Taoz
# @contact : xie-hong-tao@qq.com
import requests, re
from lxml import etree
from urllib.parse import urlencode, urljoin


class NewsSrv(object):
    @classmethod
    def news_list(cls, page):
        host = 'https://news.sogou.com/news'
        params = urlencode({
            'query': '数据开放',
            'page': str(page),
            'p': '40230447',
            'dp': '1'
        })
        url = host + '?' + params
        res = requests.get(url=url)

        tree = etree.HTML(res.text)

        total = tree.xpath('//span[@class="filt-result"]')[0].xpath('string(.)').strip()
        total_num = re.search(".*约(.*)篇.*", total).group(1)

        result = {
            'total': total_num,
            'data': []
        }

        news_rows = tree.xpath('//div[@class="results"]//div[@class="vrwrap"]')
        for news_row in news_rows:
            news = {}
            title_h3 = news_row.xpath('div/h3[@class="vrTitle"]')
            if len(title_h3) > 0:
                news['title'] = title_h3[0].xpath('string(.)').strip()
                news['url'] = news_row.xpath('div/h3[@class="vrTitle"]/a/@href')[0]
                info = news_row.xpath('div/div[@class="news-detail"]')[0]
                time_origin = info.xpath('div/p[@class="news-from"]/text()')[0].split('\xa0')
                news['time'] = time_origin[1]
                news['origin'] = time_origin[0]
                news['abstract'] = info.xpath('div/p[@class="news-txt"]/span')[0].xpath('string(.)').strip()
                result['data'].append(news)
        print(result)
        return result

