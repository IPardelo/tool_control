# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Brand(models.Model):
    _name = 'tool.provider'
    _description = 'Tools brands'

    name = fields.Char('Proveedor', required=True)
    provider_id = fields.Many2one('tool.provider', string='Proveedor')
    description = fields.Text('Descripcion')
    email = fields.Char('E-Mail', required=True)
    address = fields.Char('Direccion')
    phone = fields.Char('Telefono')
