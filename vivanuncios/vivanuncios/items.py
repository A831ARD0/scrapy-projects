# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VivanunciosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #datos generales
    idPropiedad = scrapy.Field()
    category_id = scrapy.Field()
    agent_id = scrapy.Field()
    user_id = scrapy.Field() 
    type_popiedad = scrapy.Field()
    title = scrapy.Field()
    slug = scrapy.Field()
    body = scrapy.Field()
    image_name = scrapy.Field()
    image_ext = scrapy.Field()
    meta_keywords = scrapy.Field()
    meta_desc = scrapy.Field()
    status = scrapy.Field()
    create_date = scrapy.Field()
    updated_at = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip_propiedad = scrapy.Field()
    country = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    price = scrapy.Field()
    beds = scrapy.Field()
    services = scrapy.Field()
    characteristics = scrapy.Field()
    bath = scrapy.Field()
    year = scrapy.Field()
    features = scrapy.Field()
    is_delete = scrapy.Field()
    featured = scrapy.Field()
    size = scrapy.Field()
    related = scrapy.Field()
    disponible = scrapy.Field()

    tipoLetra = scrapy.Field()
    tipoPublicado = scrapy.Field()
    url_pagina = scrapy.Field()
    url_vendedor = scrapy.Field()
    nombre_vendedor = scrapy.Field()
    id_anuncio = scrapy.Field()
    
    leyenda = scrapy.Field()
    sitio = scrapy.Field()
    


    #titulo = scrapy.Field()
    #img = scrapy.Field()
    #imgs = scrapy.Field()
    #precio = scrapy.Field()
    #publicado = scrapy.Field()
    #url_pagina = scrapy.Field()

    #Datos del vendedor
    #url_vendedor = scrapy.Field()
    #nombre_vendedor = scrapy.Field()


    #atributos de la propiedad
    #atributos_01 = scrapy.Field()
    #atributos_02 = scrapy.Field()
    #atributos_03 = scrapy.Field()
    #atributos_04 = scrapy.Field()
    #atributos_05 = scrapy.Field()
    #atributos_06 = scrapy.Field()

    #mas detalles
    #descripcion = scrapy.Field()
    #id_anuncio = scrapy.Field()
    #categoria = scrapy.Field()
    #categoria_02 = scrapy.Field()
    #ubicacion = scrapy.Field()
    #coordenadas = scrapy.Field()
    #lag = scrapy.Field()
    #lng = scrapy.Field()
    #tipo = scrapy.Field()

