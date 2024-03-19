import scrapy
from crawldata.items import CrawldataItem
import os,json
class DoanhnghiepSpider(scrapy.Spider):
    name = "dienthoai"
    allowed_domains = ["tinhte.vn"]
    # start_urls = ["https://tinhte.vn/dienthoai"]

    def start_requests(self):
        for page_number in range(2,3):
            yield scrapy.Request(url='https://tinhte.vn/dienthoai/page-{page_number}'.format(page_number=page_number),callback=self.parse)

    def parse(self, response):
        questionURLs = response.xpath('//div[@class="titleText"]/descendant::h3/a[1]/@href').getall()
        for questionURL in questionURLs:
            item = CrawldataItem()
            item['Link'] = response.urljoin(questionURL)
            request = scrapy.Request(url= response.urljoin(questionURL), callback=self.parseQA)
            request.meta['item'] = item
            yield request
    
    def parseQA(self,response):
        item = response.meta['item']
        item['BlogName'] = "dienthoai"
        item['Title'] =response.xpath('normalize-space(//h1)').get()
        item['Author'] =response.xpath('normalize-space(//div[@class="jsx-89440 author-name"]/a)').get()
        item['Description'] =response.xpath('normalize-space(//span[@class="xf-body-paragraph"])').get() 
        # Cach 1

        yield item


        # Cach 2

        # current_dir = os.getcwd()
        # file_path = os.path.join(current_dir,'data1.json')
        # with open(file_path,'a') as f:
        #     line = json.dumps({
        #         'Link':item['Link'],
        #         'BlogName':item['BlogName'],
        #         'Title':item['Title'],
        #         'Author':item['Author'],
        #         'Description':item['Description']},ensure_ascii=False) + '\n'
        #     f.write(line)

