import scrapy


class RedditAMASpider (scrapy.Spider):
    name = 'redditAMA'
    start_urls = ['https://www.reddit.com/r/AskReddit/']

    def parse(self, response):
        filename = 'redditAMA.html'