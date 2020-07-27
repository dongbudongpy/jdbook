# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# from scrapy import signals
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

# 设置UA池
# 设置UA池可以有哪些方法？除了这种
# 如果用别人维护的包比如fake_useragent 怎么在scrapy中实现？



class RandomUserAgentMiddleware(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua = random.choice(user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            print("########################### current useragent: %s" % ua)

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',


]

# 设置IP池
class ProxyPool(object):
    def process_request(self, request, spider):
        h = request.url.split(':')[0]
        if h == 'http':
            ip = random.choice(http_ip_list)
            request.meta['proxy'] = 'http://' + ip
            print("################################## current http ip: %s" % ip)
        else:
            ip = random.choice(https_ip_list)
            request.meta['proxy'] = 'https://' + ip
            print("################################## current https ip: %s" % ip)

http_ip_list = [
    '112.87.68.89:9999',
    '113.103.225.103:9999',
    '112.85.164.30:9999',
    '182.34.35.192:9999',
    '27.221.32.140:80',



]

https_ip_list = [
    '59.32.37.236:3128',
    '1.192.242.150:9999',
    '112.85.130.174:9999',
    '125.73.220.18:31036',
    '58.254.220.116:52470',



]





















# class Jdbook1SpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class Jdbook1DownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
