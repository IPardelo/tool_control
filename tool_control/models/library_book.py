# -*- coding: utf-8 -*-
import logging
from sqlite3.dbapi2 import Date

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Titulo', required=True)
    date_updated = fields.Datetime('Ultima modificacion', default=lambda self: fields.datetime.now(), readonly=True)
    current_user = fields.Many2one('res.users', 'Ultimo usuario editor', default=lambda self: self.env.user)
    category_id = fields.Many2one('library.book.category', string='Categoria')
    state = fields.Selection([
        ('available', 'Disponible'),
        ('notavailable', 'Usandose'),
        ('lost', 'Perdida'),
        ('broken', 'Rota')],
        'State', default="available")

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
        for book in self:
            if book.is_allowed_transition(book.state, new_state):
                book.state = new_state
                self.current_user = lambda self: self.env.user
                self.date_updated = lambda self: fields.datetime.now()
            else:
                message = _('Pasar de %s a %s no esta permitido') % (book.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('available')

    def make_notavailable(self):
        self.change_state('notavailable')

    def make_lost(self):
        self.change_state('lost')

    def make_broken(self):
        self.change_state('broken')

    @api.onchange('name')
    def change_field_value(self):
        self.current_user = lambda self: self.env.user

    @api.multi
    def change_update_date(self):
        self.ensure_one()
        self.date_updated = fields.Datetime.now()