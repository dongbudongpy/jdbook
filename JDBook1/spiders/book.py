# -*- coding: utf-8 -*-
import scrapy
from JDBook1.items import Jdbook1Item
import json



class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['jd.com','p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    # 加个标示 测试前五页
    page = 0

    # 解析分类页
    def parse(self, response):
        # 解析分类页 包括一级分类和二级分类
        # 解析一级分类
        first_catalog = response.xpath('//div[@class="mc"]/dl/dt')


        # 取一级分类
        for first_cat in first_catalog[:1]:
            item = Jdbook1Item()
            item['first_catalog'] = first_cat.xpath('./a/text()').extract_first()

            # print(item['first_catalog'])

            # 解析二级分类
            second_catalog = first_cat.xpath('./following-sibling::dd[1]/em')

            # 取二级分类的
            for second_cat in second_catalog[:1]:
                item['second_catalog'] = second_cat.xpath('./a/text()').extract_first()

                # print(item['second_catalog'])

                second_catalog_url = "https:" + second_cat.xpath('./a/@href').extract_first()

                # 发送二次请求 获取列表页
                yield scrapy.Request(
                    second_catalog_url,
                    callback=self.parse_book_list,
                    meta={'book':item}
                )

    # 解析列表页
    def parse_book_list(self, response):
        # 接收上个页面传过来的item
        item = response.meta['book']

        # 解析列表页
        book_list = response.xpath('//div[@id="plist"]/ul/li')
        for book in book_list[:1]:
            item['book_name'] = book.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            item['picture_url'] = "https:" + book.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            item['book_author'] = book.xpath('.//div[@class="p-bookdetails"]/span/span/a/text()').extract_first().strip()
            item['publish_house'] = book.xpath('.//div[@class="p-bookdetails"]/span/a/text()').extract_first()
            item['publish_time'] = book.xpath('.//div[@class="p-bookdetails"]/span[@class="p-bi-date"]/text()').extract_first().strip()
            # item['book_price'] = book.xpath('.//div/div/strong/i/text()').extract_first()
            # 这样拿不到价格

            # 获取价格需要动态发送ajax请求 源码没有数据
            # 单独发送获取价格的ajax请求
            # 调试参数 区分哪些参数是必传 哪些是非必传
            # 参数中的callback可直接删除 前端跨域用的 其余的参数从多到少依次删除测试

            url = 'https://p.3.cn/prices/mgets?skuIds=J_{}'
            sku_id = book.xpath('./div/@data-sku').extract_first()
            price_url = url.format(sku_id)

            # 每遍历一本书 发送一次价格请求
            yield scrapy.Request(
                price_url,
                callback=self.parse_price,
                meta={'book':item}
            )

        # # 测试前五页
        # self.page += 1
        # if self.page > 4:
        #     return

        # 翻下一页代码

        # 方法一
        # 拼接URL
        # 观察列表页的url 其中有两个参数需要获取后再拼接 
        # https://list.jd.com/list.html?cat=1713,{},{}&page={}

        # 方法二
        # 抓取 下一页 按钮 用follow跟进
        next_page_url = response.xpath('//div/span/a[@class="pn-next"]/@href').extract_first()
        yield response.follow(
            next_page_url,
            callback=self.parse_book_list,
            meta={'book':item}
        )

        


        # 爬取完毕后终止
        if not next_page_url:
            return

    # 解析价格
    def parse_price(self, response):
        item = response.meta['book']
        response_str = response.body.decode()

        # print(response_str)

        item['book_price'] = json.loads(response_str)[0]['p']

        # print(item)

        yield item

    # 解析详情页
    def parse_detail(self, response):
        pass






