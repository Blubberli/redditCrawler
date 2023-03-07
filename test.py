import scrapy
from scrapy.http.request import Request

# class TestSpider(scrapy.Spider):
#     name = "test"
#     allowed_domains = ["www.reddit.com"]
#     start_urls = [
#         "http://www.reddit.com/r/changemyview/comments/kna7u4/cmv_i_dont_understand_the_debate_between_pro_and/"]

#     def parse(self, response):
#         # data-test-id = "post-content"
#         post = response.xpath('//*[@id="t3_kna7u4"]')
#         for _ in post:
#             title = post.xpath(
#                 './div/div[3]/div[1]/div/h1/text()').get()
#             author = post.xpath(
#                 './div/div[2]/div/div[1]/div[1]/div/a/@href').get()

#             flair = post.xpath(
#                 './div/div[4]/div[2]/a/span/text()').get()

#             flair_link = post.xpath(
#                 './div/div[4]/div[2]/a/@href').get()

#             content = [
#                 ''.join(
#                     line
#                     for line in p.xpath('./text()').get()
#                     if line
#                 )
#                 for p in post.xpath('./div/div[5]/div//p')
#             ]

#             yield{
#                 'title': title,
#                 'author': author,
#                 'flair': flair,
#                 'flair_link': flair_link,
#                 'content': " ".join(content),
#             }


# class TestSpider(scrapy.Spider):
#     name = "test"
#     allowed_domains = ["old.reddit.com"]
#     start_urls = [
#         "https://old.reddit.com/r/changemyview/search?q=flair_name%3A%22Removed+-+Submission+Rule+E%22&restrict_sr=on&sort=relevance&t=all"]

#     def parse(self, response):
#         # data-test-id = "post-content"
#         next_selector = response.xpath(
#             '//a[@rel="nofollow next"]/@href')

#         posts = response.xpath(
#             '//div[@class=" search-result search-result-link has-linkflair "]')

#         for post in posts:
#             title = post.xpath(
#                 './div/header/a/text()').get()
#             author = post.xpath(
#                 './div/div[1]/span[4]/a/text()').get()

#             flair = post.xpath(
#                 './div/header/span/text()').get()

#             point = post.xpath('./div/div[1]/span[2]/text()').get()

#             comment_num = post.xpath('./div/div[1]/a/text()').get()

#             content = post.xpath(
#                 "./div/div[2]/div/div/p/text()"
#             ).getall()

#             yield{
#                 'title': title,
#                 'author': author,
#                 'flair': flair,
#                 'point': point.split(" ")[0],
#                 'comment_num': comment_num.split(" ")[0],
#                 'content': content

#             }

#         for url in next_selector.extract():
#             yield Request(url, callback=self.parse)

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["old.reddit.com"]
    start_urls = [
        "https://old.reddit.com/r/changemyview/search?q=flair_name%3A%22Removed+-+Submission+Rule+A%22&restrict_sr=on&sort=relevance&t=all"]

    def parse(self, response):
        # data-test-id = "post-content"
        next_selector = response.xpath(
            '//a[@rel="nofollow next"]/@href')

        posts = response.xpath(
            '//div[@class=" search-result search-result-link has-linkflair "]')

        for post in posts:
            title = post.xpath(
                './div/header/a/text()').get()
            # author = post.xpath(
            #     './div/div[1]/span[4]/a/text()').get()

            # flair = post.xpath(
            #     './div/header/span/text()').get()

            # point = post.xpath('./div/div[1]/span[2]/text()').get()

            # comment_num = post.xpath('./div/div[1]/a/text()').get()

            # content = post.xpath(
            #     "./div/div[2]/div/div/p/text()"
            # ).getall()
            comment_link = post.xpath('./div/header/a/@href').get()

            yield response.follow(url=comment_link, callback=self.parse_page, meta={'title': title})

        # for url in next_selector.extract():
        #     yield Request(url, callback=self.parse)

    def parse_page(self, response):
        title = response.request.meta['title']
        comments = response.xpath(
            '//div[@class="commentarea"]/div[@class="sitetable nestedlisting"]//div[contains(@class, "thing")]')

        # print("length: ", len(comments))

        for comment in comments:
            c_author = comment.xpath(
                "./div[2]/p/a[2]/text()").get()
            # c_point = comment.xpath(
            #     "//span[@span='score unvoted']/text()").get()

            c_content = comment.xpath(
                "./div[2]/form/div/div/p/text()").getall()
            # c_delta = comment.xpath(
            #     "//span[@class='flair']/text()").get()

            yield{
                'title': title,
                'author': c_author,
                # 'point': c_point,
                'content': c_content,
                # 'author_delta': c_delta

            }

        # yield{
        #     'title': title,
        #     'author': author,
        #     'flair': flair,
        #     'point': point.split(" ")[0],
        #     'comment_num': comment_num.split(" ")[0],
        #     'content': content

        # }
