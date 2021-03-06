# -*- coding: utf-8 -*-
import logging
from datetime import time, datetime

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)


class Tool(models.Model):
    _name = 'tool'
    _description = 'Tools base'
    _defaults = {
        'date_updated': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S')
    }

    name = fields.Char('Herramienta', required=True)
    date_updated = fields.Datetime('Ultimo uso', readonly=True)
    description = fields.Text('Descripcion')
    brand_id = fields.Many2one('tool.brand', string='Marca', required=True)
    current_user = fields.Many2one('res.users', 'Ultimo usuario', default=lambda self: self.env.user, readonly=True)
    category_id = fields.Many2many('tool.category', string='Categoria', required=True)
    contar = fields.Integer('Veces usado',readonly=True)
    state = fields.Selection([
        ('available', 'Disponible'),
        ('notavailable', 'Usandose'),
        ('lost', 'Perdida'),
        ('broken', 'Rota')],
        'Estado', default="available")


    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('available', 'notavailable'),
                   ('available', 'lost'),
                   ('notavailable', 'available'),
                   ('notavailable', 'lost'),
                   ('notavailable', 'broken'),
                   ('lost', 'available'),
                   ('lost', 'broken')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for tool in self:
            if tool.is_allowed_transition(tool.state, new_state):
                tool.state = new_state
                self.current_user = self.env.uid
                self.date_updated = datetime.today()
            else:
                message = _('Pasar de %s a %s no esta permitido') % (tool.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('available')

    def make_notavailable(self):
        self.change_state('notavailable')
        self.contar = self.contar + 1

    def make_lost(self):
        self.change_state('lost')

    def make_broken(self):
        self.change_state('broken')

    @api.multi
    def change_update_date(self):
        self.ensure_one()
        self.date_updated = fields.Datetime.now()

    @api.model
    def get_category(self, category):
        return category.mapped('tool_category.name')