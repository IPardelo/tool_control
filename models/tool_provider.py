# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Brand(models.Model):
    _name = 'tool.provider'
    _description = 'Tools brands'

    name = fields.Char('Proveedor', required=True)
    description = fields.Text('Descripcion')
    email = fields.Char('E-Mail', required=True)
    address = fields.Char('Direccion')
    phone = fields.Char('Telefono')
    brand_id = fields.One2many('tool.brand', 'provider_id', string='Marcas')
    contar = fields.Integer(
        string='Num. marcas',
        compute='_contar',
        store=False,
        compute_sudo='False',
    )

    @api.model
    def _contar(self):
        for record in self:
            record.contar = len(record.brand_id)
