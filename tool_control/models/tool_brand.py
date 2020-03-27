# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Brand(models.Model):
    _name = 'library.book.brand'
    _description = 'Tools brands'

    name = fields.Char('Marca')
    description = fields.Text('Descripcion')
