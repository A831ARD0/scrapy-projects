import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from metroscubicos.items import MetroscubicosItem
from scrapy.exceptions import CloseSpider
from scrapy.item import Item, Field
#from bs4 import BeautifulSoup


class MetroscubicosSpider(CrawlSpider):
	name ='metroscubicos'
	item_count = 0
	coordenadas = ''
	img1 = ''	
	allowed_domain = ['https://www.metroscubicos.com/']
	start_urls = ['https://inmuebles.metroscubicos.com/']

	rules = {
				Rule(LinkExtractor(allow = (), restrict_xpaths = ("//div[@class='section']/div[@class='nav pager']/ul[@class='ch-pagination']/li[@class='last-child']/a"))),
				Rule(LinkExtractor(allow = r'metroscubicos.com/MLM-'),
					callback = 'parse_item', follow = False),
			}
			#, restrict_xpaths = ('//div[@class="results list-view"]/div[@class="view"]/ul/li[@class="result pictures"]/div[@class="result-link"]/div[@class="container"]/div[@class="title"]')

	def parse_item(self, response):
		ml_item = MetroscubicosItem()

		#informacion del producto
		ml_item['idPropiedad'] = 'NULL'
		ml_item['titulo']	= response.xpath("normalize-space(//div[@class='vip-product-info__development']/div[@class='vip-product-info__development__info']/h1[@class='vip-product-info__development__name'])").extract()
		ml_item['precio']	= response.xpath("normalize-space(//div[@class='vip-product-info__development__info']/div[@class='vip-product-info__development__bottom-block']/article[@class='vip-price ch-price']/strong)").extract()
		ml_item['m2']	= response.xpath("normalize-space(//ul[@class='vip-product-info__attributes-list']/li[@class='vip-product-info__attribute_element'][1]/span[@class='vip-product-info__attribute-value'])").extract()
		ml_item['recamaras']	= response.xpath("normalize-space(//section[@class='vip-section-product-info']/section[@class='vip-product-info__attributes']/ul[@class='vip-product-info__attributes-list']/li[@class='vip-product-info__attribute_element'][2])").extract()
		ml_item['banio']	= response.xpath("normalize-space(//section[@class='vip-section-product-info']/section[@class='vip-product-info__attributes']/ul[@class='vip-product-info__attributes-list']/li[@class='vip-product-info__attribute_element'][3])").extract()
		ml_item['telefono']	= response.xpath('normalize-space(//*[@id="questions-form"]/div[@class="contacts-input"]/span/span)').extract()
		ml_item['ubicacion']	= response.xpath("normalize-space(//div[@class='nav-main-content']/section[@class='vip-section-map container']/h2[@class='map-location'])").extract()
		ml_item['maps']	= response.xpath("normalize-space(//div[@class='nav-main-content']/section[@class='vip-section-map container']/div[@id='sectionDynamicMap']/img/@src)").extract()
		ml_item['descripcion']	= response.xpath("normalize-space(//section[@class='vip-section-description container']/div[@class='description-content']/div[@class='description-content-main-group attribute-content']/div[@class='card-section']/ul[@class='attribute-group'])").extract()
		ml_item['caracteristicas_adicionales']	= response.xpath("normalize-space(//div[@class='description-content']/div[@class='description-content-secondary-group attribute-content']/div[@class='boolean-attribute-list-container'][1]/ul[@class='boolean-attribute-list']/li)").extract()
		ml_item['comodidad']	= response.xpath("normalize-space(//div[@class='description-content']/div[@class='description-content-secondary-group attribute-content']/div[@class='boolean-attribute-list-container'][2]/ul[@class='boolean-attribute-list']/li)").extract()
		ml_item['mas']	= response.xpath("normalize-space(//section[@class='vip-section-description container']/div[@class='description-content']/pre[@class='preformated-text'])").extract()
		ml_item['imagenes']	= response.xpath("normalize-space(//div[@class='pswp pswp--supports-fs pswp--open pswp--notouch pswp--css_animation pswp--svg pswp--animated-in pswp--zoom-allowed pswp--visible pswp--has_mouse']/div[@class='pswp__scroll-wrap']/div[@class='pswp__container']/div[@class='pswp__item']/div[@class='pswp__zoom-wrap']/img[@class='pswp__img']/@src)").extract()
		ml_item['vendedor']	= response.xpath("normalize-space(//ul[@class='profile-info-list clear-floats']/li[@class='profile-info-column'][1]/span[@class='profile-info-data profile-info-name-data']/a)").extract()
		ml_item['ubicacion']	= response.xpath("normalize-space(//div[@class='vip-card']/ul[@class='profile-info-list clear-floats']/li[@class='profile-info-column'][2]/span[@class='profile-info-data']/span[@class='profile-info-location-value'])").extract()
		ml_item['publicacion']	= response.xpath("normalize-space(//section[@class='vip-section-item-info container']/p[@class='item-info-section__sku'])").extract()
		ml_item['constructora']	= response.xpath("normalize-space(//section[@class='vip-section-product-info']/div[@class='vip-product-info__development']/div[@class='vip-product-info__development__info']/h1[@class='vip-product-info__development__name'])").extract()
		ml_item['entrega']	= response.xpath("normalize-space(//section[@class='vip-section-product-info']/div[@class='vip-product-info__development']/div[@class='vip-product-info__development__info']/p[@class='vip-product-info__development__possesion-date'])").extract()
		ml_item['imagen']	= response.xpath("//div[@class='pswp__scroll-wrap']/div[@class='pswp__container']/div[@class='pswp__item'][1]/div[@class='pswp__zoom-wrap']/img[@class='pswp__img']/@src").extract()
		ml_item['url_pagina'] = response.url
		ml_item['sitio'] = "inmuebles24"
		
		#self.item_count += 1  
		#print self.item_count
		#if self.item_count > 50:
			#raise CloseSpider('item_exceede') 		
		yield ml_item  

