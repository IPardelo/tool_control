# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Brand(models.Model):
    _name = 'tool.brand'
    _description = 'Tools brands'

    name = fields.Char('Marca', required=True)
    description = fields.Text('Descripcion')
    provider_id = fields.Many2one('tool.provider', string='Proveedor')
    imagen = fields.Binary('Foto')