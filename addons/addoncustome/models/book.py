# -*- coding: utf-8 -*-

from odoo import models, fields, api


class addoncustome(models.Model):
    _name = 'addoncustome.book'
    _description = 'addoncustome.book'

    name = fields.Char(string="Nama Buku")
    author = fields.Char(string="Penulis")
    price = fields.Float(string="Harga")