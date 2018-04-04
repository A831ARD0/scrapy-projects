import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from inmuebles24.items import Inmuebles24Item
from scrapy.exceptions import CloseSpider
from scrapy.item import Item, Field
#from bs4 import BeautifulSoup


class Inmuebles24Spider(CrawlSpider):
	name ='inmuebles24'
	item_count = 0
	coordenadas = ''
	img1 = ''	
	allowed_domain = ['http://www.inmuebles24.com']
	start_urls = ['http://www.inmuebles24.com/inmuebles.html']

	rules = {
				Rule(LinkExtractor(allow = (), restrict_xpaths = ('//*[@id="paginadoListado"]/div/ul/li[7]/a'))),
				Rule(LinkExtractor(allow = r'inmuebles24.com/propiedades'),
					callback = 'parse_item', follow = False),
			}
			#, restrict_xpaths = ('//div[@class="results list-view"]/div[@class="view"]/ul/li[@class="result pictures"]/div[@class="result-link"]/div[@class="container"]/div[@class="title"]')

	def parse_item(self, response):
		ml_item = Inmuebles24Item()

		#informacion del producto
		ml_item['idPropiedad'] = 'NULL'
		ml_item['Titulo']	= response.xpath('normalize-space(//*[@id="ficha"]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div[2]/h1)').extract()
		p	= response.xpath('normalize-space(//*[@id="ficha"]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/p/strong)').extract()
		pp = "".join(p)
		if(len(pp) != 0):
			ml_item['Precio_venta']	= response.xpath('normalize-space(//*[@id="ficha"]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/p/strong)').extract()
		else:
			ml_item['Precio_venta']	= response.xpath("normalize-space(//div[@class='span8 column-side']/div[@class='card zona-precios ']/div[@class='card-content']/p[@class='precios no-margin']/span[@class='valor'])").extract()
		
		ml_item['Precio_renta']	= response.xpath('normalize-space(//*[@id="ficha"]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/p/strong)').extract()
		ml_item['Precio_renta1']	= response.xpath("normalize-space(//div[@class='span8 column-side']/div[@class='card zona-precios ']/div[@class='card-content']/p[@class='precios no-margin']/span[@class='valor'])").extract()
		ml_item['tipo_desarrollo']	= response.xpath("normalize-space(//div[@class='card aviso-datos']/div[@class='card-content'][1]/ul/li[1]/span[@class='nombre'])").extract()
		ml_item['Superficie']	= response.xpath("normalize-space(//ul[@class='aviso-datos-principales']/li[1]/strong[@class='datos-valor'])").extract()
		ml_item['Recamaras']	= response.xpath("normalize-space(//div[@class='card-content'][2]/ul[@class='aviso-datos-principales']/li[2]/strong[@class='datos-valor'])").extract()
		ml_item['banios']	= response.xpath("normalize-space(//div[@class='card-content'][2]/ul[@class='aviso-datos-principales']/li[3]/strong[@class='datos-valor'])").extract()
		ml_item['Telefono']	= response.xpath('normalize-space(//*[@id="id-verdatos-aviso-1"]/div[2]/p[1])').extract()
		n = response.xpath("normalize-space(//div[@class='card-content form-contacto-wrap']/div[@class=' ']/div[@id='contactFormNew']/div[@class='datos-inmobiliaria ']/div[2]/form[@id='id-verdatos-aviso-1']/a/h3[@class='inmobiliaria-title'])").extract()
		nn = "".join(n)
		if(len(nn) != 0):
			ml_item['Nombre_contacto']	= n
		else:
			n2 = response.xpath('normalize-space(//*[@id="id-verdatos-aviso-1"]/a/h3)').extract()
			nn2 = "".join(n2)
			if(len(nn2) != 0):
				ml_item['Nombre_contacto'] = n2
			else:	
				ml_item['Nombre_contacto']	= response.xpath("normalize-space(//div[@class='datos-inmobiliaria ']/div[2]/form[@id='id-verdatos-aviso-1']/h3[@class='inmobiliaria-title'])").extract()
			
		ml_item['Nombre_contacto1']	= response.xpath("normalize-space(//div[@class='datos-inmobiliaria ']/div[2]/form[@id='id-verdatos-aviso-1']/h3[@class='inmobiliaria-title'])").extract()
		ml_item['Nombre_contacto2']	= response.xpath('normalize-space(//*[@id="id-verdatos-aviso-1"]/a/h3)').extract()
		ml_item['imagen']	= response.xpath("//div[@id='tab-foto-content']/div[@id='gallery-ficha']/div[@class='rsOverflow grab-cursor']/div[@class='rsContainer']/div[@class='rsSlide '][1]/div/img[@class='rsImg rsMainSlideImage']/@src").extract()
		ml_item['Imagenes']	= response.xpath("//div/img[contains(@class, 'rsImg rsMainSlideImage')]/@src").extract()
		ml_item['codigo']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/span[@class='code no-margin'])").extract()
		ml_item['Datos_principales']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='row']/div[@class='span8'][1]/div[@class='card aviso-datos']/div[@class='card-content']/ul/li/span)").extract()
		ml_item['mapa']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@id='map']/div[@id='imgVar']/img[@class='img-static-map']/@src)").extract()
		ml_item['ubicacion_02']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@id='map']/div[@class='card-content no-padding-bottom']/div[@class='list list-directions']/ul/li)").extract()
		x = response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[6]/a/span)").extract()
		XX = "".join(x)
		if(len(XX) != 0):	
			ml_item['col_06'] = x
			ml_item['col_03']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[3]/a/span)").extract()
			ml_item['col_04']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[4]/a/span)").extract()
			ml_item['col_05']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[5]/a/span)").extract()
		else:
			ml_item['col_03'] = 'Otros'
			ml_item['col_04']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[3]/a/span)").extract()
			ml_item['col_05']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[4]/a/span)").extract()
			ml_item['col_06']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[5]/a/span)").extract()

		ml_item['col_01']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[1]/a/span)").extract()
		ml_item['col_02']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='card'][1]/div[@class='card-content']/div/ul[@class='breadcrumb no-margin pull-left oculto-print']/li[2]/a/span)").extract()
		
		
		ml_item['latitud']	= response.xpath('normalize-space(//*[@id="lat"]/@value)').extract()
		ml_item['longitud']	= response.xpath('normalize-space(//*[@id="lng"]/@value)').extract()
		ml_item['Descripcion']	= response.xpath("normalize-space(//div[@class='span16 column-content']/div[@class='row']/div[@class='span8'][2]/div[@class='card description']/div[@class='card-content']/span[@id='id-descipcion-aviso'])").extract()
		ml_item['url_pagina'] = response.url
		ml_item['sitio'] = "inmuebles24"
		
		#self.item_count += 1  
		#print self.item_count
		#if self.item_count > 50:
			#raise CloseSpider('item_exceede') 		
		yield ml_item  

