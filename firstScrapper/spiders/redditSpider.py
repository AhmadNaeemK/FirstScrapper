import scrapy


class RedditAMASpider (scrapy.Spider):
    name = 'redditAMA'
    start_urls = ['https://www.reddit.com/r/blender/']

    def parse(self, response):
        for post in response.css('.Post'):
            post_title = post.css('._eYtD2XCVieq6emjKBH3m ::text').get()
            post_link = post.css('._3jOxDPIQ0KaOWpzvSQo-1s ::attr(href)').get()
            post_upvotes = post.css('._1rZYMD_4xY3gRcSS3p8ODO ::text').get()
            num_comments = int(post.css('.FHCV02u6Cp2zYL0fhQPsO ::text').get().split()[0])
            img_link = post.css('._35oEP5zLnhKEbj5BlkTBUA img::attr(src)').get()

            yield {
                'title': post_title,
                'link': post_link,
                'upVotes': post_upvotes,
                'numComments': num_comments,
                'img': img_link,
            }
