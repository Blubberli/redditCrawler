import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["www.reddit.com"]
    start_urls = [
        "http://www.reddit.com/r/changemyview/comments/kna7u4/cmv_i_dont_understand_the_debate_between_pro_and/"]

    def parse(self, response):
        # data-test-id = "post-content"
        post = response.xpath('//*[@id="t3_kna7u4"]')
        for _ in post:
            title = post.xpath(
                './div/div[3]/div[1]/div/h1/text()').get()
            author = post.xpath(
                './div/div[2]/div/div[1]/div[1]/div/a/@href').get()

            flair = post.xpath(
                './div/div[4]/div[2]/a/span/text()').get()

            flair_link = post.xpath(
                './div/div[4]/div[2]/a/@href').get()

            content = [
                ''.join(
                    line
                    for line in p.xpath('./text()').get()
                    if line
                )
                for p in post.xpath('./div/div[5]/div//p')
            ]

            yield{
                'title': title,
                'author': author,
                'flair': flair,
                'flair_link': flair_link,
                'content': " ".join(content),
            }
