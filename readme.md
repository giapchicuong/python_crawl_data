tạo project
scrapy startproject crawldata

tạo file
scrapy genspider doanhnghiep 'https://tinhte.vn/dienthoai'

chạy shell
scrapy shell 'https://tinhte.vn/dienthoai/page-2'
    chạy lệnh response.body   để test xem có lấy dc data ko
    response.xpath('//h1').getall()  
    response.xpath('normalize-space(//h1)').get()                            


scrapy shell 'https://tinhte.vn/thread/mua-may-moi-thi-chon-15-prm-hay-14-prm.3770865/'

chạy file doanh nghiệp và tạo data.json
scrapy crawl dienthoai -o data.json

scrapy crawl dienthoai   

