# Define here the models for your scraped items
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

class RedditScraperMiddleware:
    # This middleware will handle all requests to the Reddit website
    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        return None

    # This middleware will handle all responses from the Reddit website
    def process_response(self, request, response, spider):
        return response

    # This middleware will handle all exceptions that occur while scraping
    def process_exception(self, request, exception, spider):
        pass

class RedditScraperDownloaderMiddleware:
    # This middleware will handle all downloads within the scraper
    def process_request(self, request, spider):
        return None

    # This middleware will handle all responses from the downloads
    def process_response(self, request, response, spider):
        return response

    # This middleware will handle all exceptions that occur while downloading
    def process_exception(self, request, exception, spider):
        pass