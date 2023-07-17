```python
import scrapy
from reddit_scraper.items import RedditScraperItem

class PyplSpider(scrapy.Spider):
    name = 'pypl_spider'
    allowed_domains = ['www.reddit.com']
    start_urls = ['https://www.reddit.com/r/stocks/search?q=PYPL&restrict_sr=1']

    def parse(self, response):
        for post in response.css('div.thing'):
            item = RedditScraperItem()
            item['title'] = post.css('a.title::text').get()
            item['url'] = post.css('a.title::attr(href)').get()
            item['date'] = post.css('time::attr(datetime)').get()
            item['content'] = post.css('div.expando div.usertext-body::text').get()
            yield item

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```