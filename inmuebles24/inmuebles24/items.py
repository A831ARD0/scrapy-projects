# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Inmuebles24Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    #datos generales
    idPropiedad = scrapy.Field()
    Titulo = scrapy.Field()
    Precio_venta = scrapy.Field()
    Precio_renta = scrapy.Field()
    Precio_renta1 = scrapy.Field()
    tipo_desarrollo = scrapy.Field()
    Superficie = scrapy.Field()
    Recamaras = scrapy.Field()
    banios = scrapy.Field()
    Telefono = scrapy.Field()
    Nombre_contacto = scrapy.Field()
    Nombre_contacto1 = scrapy.Field()
    Nombre_contacto2 = scrapy.Field()
    imagen = scrapy.Field()
    Imagenes = scrapy.Field()
    codigo = scrapy.Field()
    Datos_principales = scrapy.Field()
    mapa = scrapy.Field()
    ubicacion_02 = scrapy.Field()
    estado = scrapy.Field()
    Colonia = scrapy.Field()
    Calle = scrapy.Field()
    latitud = scrapy.Field()
    longitud = scrapy.Field()
    Descripcion = scrapy.Field()
    url_pagina = scrapy.Field()
    sitio = scrapy.Field()
    col_01 = scrapy.Field()
    col_02 = scrapy.Field()
    col_03 = scrapy.Field()
    col_04 = scrapy.Field()
    col_05 = scrapy.Field()
    col_06 = scrapy.Field()

