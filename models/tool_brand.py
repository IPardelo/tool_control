# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Brand(models.Model):
    _name = 'tool.brand'
    _description = 'Tool brands'

    name = fields.Char('Marca', required=True)
    description = fields.Text('Descripcion')
    imagen = fields.Binary('Foto')
    provider_id = fields.Many2one('tool.provider', string='Proveedor')