# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ToolCategory(models.Model):
    _name = 'tool.category'
    _description = 'Tool category'
    _parent_store = True
    _parent_name = "parent_id"

    name = fields.Char('Categoria', required=True)
    description = fields.Text('Descripcion')
    parent_id = fields.Many2one(
        'tool.category',
        string='Categoria padre',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'tool.category', 'parent_id',
        string='Subcategorias')
    parent_path = fields.Char(index=True)

    contar = fields.Integer(
        string='Num. subcategorias',
        compute='_contar',
        store=False,
        compute_sudo='False',
    )

    @api.model
    def _contar(self):
        for record in self:
            record.contar = len(record.child_ids)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! No puedes crear categorias recursivas.')