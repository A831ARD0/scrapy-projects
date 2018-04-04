# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MetroscubicosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #datos generales
    idPropiedad = scrapy.Field()
    titulo = scrapy.Field()
    precio = scrapy.Field()
    m2 = scrapy.Field()
    recamaras = scrapy.Field()
    banio = scrapy.Field()
    telefono = scrapy.Field()
    ubicacion = scrapy.Field()
    maps = scrapy.Field()
    descripcion = scrapy.Field()
    caracteristicas_adicionales = scrapy.Field()
    comodidad = scrapy.Field()
    mas = scrapy.Field()
    imagenes = scrapy.Field()
    vendedor = scrapy.Field()
    ubicacion = scrapy.Field()
    publicacion = scrapy.Field()
    constructora = scrapy.Field()
    entrega = scrapy.Field()
    imagen = scrapy.Field()
    url_pagina = scrapy.Field()
    sitio = scrapy.Field()