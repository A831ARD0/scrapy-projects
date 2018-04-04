import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from vivanuncios.items import VivanunciosItem
from scrapy.exceptions import CloseSpider
from scrapy.item import Item, Field
#from bs4 import BeautifulSoup


class VivanunciosSpider(CrawlSpider):
	name ='vivanuncios'
	item_count = 0
	coordenadas = ''
	img1 = ''	
	allowed_domain = ['https://www.vivanuncios.com.mx']
	start_urls = ['https://www.vivanuncios.com.mx/s-venta-inmuebles/v1c1097p1']

	rules = {
				Rule(LinkExtractor(allow = (), restrict_xpaths = ('//div[@class="desktop-pagination"]/span/a[@class="arrows icon-right-arrow"]'))),
				Rule(LinkExtractor(allow = r'www.vivanuncios.com.mx/a-venta-inmuebles/'),
					callback = 'parse_item', follow = False),
			}
			#, restrict_xpaths = ('//div[@class="results list-view"]/div[@class="view"]/ul/li[@class="result pictures"]/div[@class="result-link"]/div[@class="container"]/div[@class="title"]')

	def parse_item(self, response):
		ml_item = VivanunciosItem()

		#informacion del producto
		ml_item['idPropiedad'] = 'NULL'
		tipo	= response.xpath('normalize-space(//div[@class="ad-details-container"]/div[@class="pri-attrs"]/ul[@class="category-pri-attrs"]/li[1]/a)').extract()
		
		for i in tipo:
			if i == 'Casas en Venta':
				ml_item['category_id'] = 25
			else: 
				if i == 'Departamentos en Venta':
					ml_item['category_id'] = 26
				else: 
					if i == 'Oficinas en Venta':
						ml_item['category_id'] = 27
					else: 
						if i == 'Bodegas en Venta':
							ml_item['category_id'] = 28
						else:
							if i == 'Roomies en Venta':
								ml_item['category_id'] = 29
							else:
						 		if i == 'Terrenos en Venta':
									ml_item['category_id'] = 30
								else: 
									if i == 'Desarrollo':
										ml_item['category_id'] = 31
									else:
										if i == 'Estudio en Venta':
											ml_item['category_id'] = 32
										else:
											if i == 'Inmobiliaria en Venta':
												ml_item['category_id'] = 33
											else: 
												if i == 'Particular en Venta':
													ml_item['category_id'] = 34
												else: 
													if i == 'Remate hipotecario en Venta':
														ml_item['category_id'] = 35
													else:
														ml_item['category_id'] = 36

		ml_item['tipoLetra'] = tipo
		
		ml_item['agent_id'] = 0
		ml_item['user_id'] = 0
		ml_item['type_popiedad'] = 'SALE'
		ml_item['title'] = response.xpath('normalize-space(//h2[@class="item-title"]/span[@class="ad-title"]/text())').extract()
		ml_item['slug'] = ''
		
		body = ""
		body1 = ""
		body = response.xpath('normalize-space(//div[@class="sec-attrs"]/div[@class="ad-description"])').extract()
		body1 = [e.replace('"',"") for e in body ]
		ml_item['body'] = body1

		self.img1 = response.xpath('//div/img/@src').extract()
		
		indice = 0
		bandera = 0
		imgs = ""

		while bandera == 0:
			if self.img1[indice] == ',':
				bandera = 1
			else:
				imgs = imgs + self.img1[indice]
			indice += 1
			if indice < len(self.img1)-1:
				bandera = 0
			else: 
				bandera = 1


		ml_item['image_name'] = imgs
		ml_item['image_ext'] = response.xpath('//img/@data-lazy').extract()
		ml_item['meta_keywords'] = 'NULL'
		ml_item['meta_desc'] = 'NULL'
		ml_item['status'] = 1
		ml_item['create_date'] = 'NULL'
		ml_item['updated_at'] = 'NULL'
		ml_item['tipoPublicado'] = response.xpath('normalize-space(//div[@class="ad-last-posted"]/span[2]/text())').extract()
		ml_item['address'] = response.xpath('normalize-space(//div[@class="sec-attrs"]/div[@class="ad-user-attrs"]/div[@class="ad-showup-location"]/div/a/text())').extract()
		ml_item['city'] = response.xpath('normalize-space(//div[@class="sec-attrs"]/div[@class="ad-user-attrs"]/div[@class="ad-showup-location"]/div/a/text())').extract()
		ml_item['state'] = response.xpath('normalize-space(//div[@class="sec-attrs"]/div[@class="ad-user-attrs"]/div[@class="ad-showup-location"]/div/a/text())').extract()
		ml_item['zip_propiedad'] = ''
		ml_item['country'] = 'Mexico'
		#ml_item['coordenadas'] = response.xpath('normalize-space(//div[@class="google-maps"]/script)').extract()
		self.coordenadas = response.xpath('normalize-space(//div[@class="map-wrapper"]/script)').extract()

		#extrae_coordenadas(self.coordenadas)
		coor = "".join(self.coordenadas)
		indice = 0
		bandera = 0
		lag = ""
		lng = ""

		while indice < len(coor):
		    if bandera == 1:
		    	if coor[indice] != ',':
		    		lag = lag + coor[indice]
		    	else:
		    		bandera += 1
		    if bandera == 3:
		    	if coor[indice] != '}':
		    		lng = lng + coor[indice]
		    	else:
		    		bandera += 1
		    if coor[indice]== ':':
		    	bandera += 1
		    if bandera == 4:
		    	break
		    indice += 1	

		ml_item['latitude'] = lag
		ml_item['longitude'] = lng
		
		precio = 0
		precio = response.xpath('normalize-space(//div[@class="price-update"]/span[@class="value"]/meta[@itemprop="price"]/@content)').extract()
		if(precio != ''):	
			ml_item['price'] = precio
		banios = response.xpath('normalize-space(//ul[@class="category-pri-attrs"]/li[starts-with(span,"Ba")])').extract()
		numBanios = "".join(banios)
		indice = 0
		bandera = 0
		num = ""

		while indice < len(numBanios):
			if numBanios[indice] == 's':
				num = num + numBanios[indice+1]
				#num = num + numBanios[indice+2]
				bandera += 1
			if bandera > 0:
				break
			indice += 1
		if(len(num)==0):
			num = 0

		ml_item['beds'] = num
		
		ml_item['services'] = 'NULL'
		ml_item['characteristics'] = 'NULL'
		recamara = response.xpath('normalize-space(//ul[@class="category-pri-attrs"]/li[starts-with(span,"Rec")])').extract()
		numRecamara = "".join(recamara)
		indice = 0
		bandera = 0
		num = ""

		while indice < len(numRecamara):
			if numRecamara[indice] == ')':
				num = num + numRecamara[indice+1]
				bandera += 1
			if bandera > 0:
				break
			indice += 1
		
		if(len(num)==0):
			num = 0

		if num == 'E':
			num = 0

		ml_item['bath'] = num
		ml_item['year'] = '2017'
		ml_item['features'] = ''
		ml_item['is_delete'] = '0'
		ml_item['featured'] = '0'
		superficie = response.xpath('normalize-space(//ul[@class="category-pri-attrs"]/li[starts-with(span,"Superficie")])').extract()
		numSuperficie = "".join(superficie)
		indice = 0
		bandera = 0
		num = ""

		while indice < len(numSuperficie):
			if bandera == 1:
				num = num + numSuperficie[indice+6]
			if numSuperficie[indice] == ' ':
				bandera = 1
			indice += 1

		if(len(num)==0):
			num = 0

		ml_item['size'] = num

		ml_item['related'] = ''
		ml_item['disponible'] = 0
		ml_item['url_pagina'] = response.url
		ml_item['url_vendedor'] = response.xpath('//div[@class="seller-profile-container"]/a/@href').extract()
		ml_item['nombre_vendedor'] = response.xpath('normalize-space(//div[@class="seller-profile-container"]/a/span/text())').extract()
		#ml_item['atributos_03'] = response.xpath('normalize-space(//ul[@class="category-pri-attrs"]/li[starts-with(span,"GARAGE")])').extract()
		#ml_item['atributos_04'] = response.xpath('normalize-space(//ul[@class="category-pri-attrs"]/li[starts-with(span,"DISPONIBILIDAD")])').extract()
		#ml_item['atributos_06'] = response.xpath('normalize-space(//ul[@class="category-pri-attrs"]/li[starts-with(span,"VENDEDOR(A)")])').extract()
		ml_item['id_anuncio'] = response.xpath('normalize-space(//div[@class="sec-attrs"]/div[@class="ad-description-id"]/text())').extract()
		#ml_item['categoria'] = response.xpath('normalize-space(//div[@class="sec-attrs"]/div[@class="ad-category"]/div)').extract()
		
		ml_item['leyenda'] = response.xpath('normalize-space(//div[@class="exact-location-text"]/text())').extract()
		ml_item['sitio'] = "vivanuncios"

		
		#self.item_count += 1  
		#print self.item_count
		#if self.item_count > 1000:
		#	raise CloseSpider('item_exceede') 
		yield ml_item 

