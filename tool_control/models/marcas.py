# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Brands(models.Model):
    _name = 'library.book.brand'

    name = fields.Char('Marca')
    description = fields.Text('Descripcion')
