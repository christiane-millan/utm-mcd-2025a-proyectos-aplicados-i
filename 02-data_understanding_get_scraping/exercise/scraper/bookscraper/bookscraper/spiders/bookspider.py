import scrapy
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
        
        for book in books:
            relative_url = book.css('h3 a ::attr(href)').get()
            
            yield response.follow(relative_url, callback=self.parse_book_page)
            
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
    
    def parse_book_page(self, response):
        table_rows = response.css('.table tr')
        book = BookItem()
        
        book['url'] = response.url,
        book['title'] = response.css('.product_main h1::text').get(),
        book['upc'] = table_rows[0].css('td ::text').get(),
        book['product_type'] = table_rows[1].css('td ::text').get(),
        book['price_excl_tax'] = table_rows[2].css('td ::text').get(),
        book['price_incl_tax'] = table_rows[3].css('td ::text').get(),
        book['tax'] = table_rows[4].css('td ::text').get(),
        book['availability'] = table_rows[5].css('td ::text').get(),
        book['num_reviews'] = table_rows[6].css('td ::text').get(),
        book['stars'] = response.css('p.star-rating').attrib['class'],
        book['category'] = response.xpath('//ul[@class="breadcrumb"]/li[@class="active"]/preceding-sibling::li[1]/a/text()').get(),
        book['description'] = response.xpath('//div[@id="product_description"]/following-sibling::p/text()').get(),
        book['price'] = response.css('p.price_color ::text').get(),
        
        yield book
        
        