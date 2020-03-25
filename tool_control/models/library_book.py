# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char('Titulo', required=True)
    date_updated = fields.Datetime('Ultima modificacion', copy=False)
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

    @api.multi
    def change_update_date(self):
        self.ensure_one()
        self.date_updated = fields.Datetime.now()

    @api.multi
    def find_book(self):
        domain = [
            '|',
                '&', ('name', 'ilike', 'Book Name'),
                     ('category_id.name', '=', 'Category Name'),
                '&', ('name', 'ilike', 'Book Name 2'),
                     ('category_id.name', '=', 'Category Name 2')
        ]
        books = self.search(domain)
        logger.info('Books found: %s', books)
        return True

    @api.model
    def get_all_library_members(self):
        library_member_model = self.env['library.member']  # This is an empty recordset of model library.member
        return library_member_model.search([])

    def filter_books(self):
        all_books = self.search([])
        filtered_books = self.books_with_multiple_authors(all_books)
        logger.info('Filtered Books: %s', filtered_books)

    def mapped_books(self):
        all_books = self.search([])
        books_authors = self.get_author_names(all_books)
        logger.info('Books Authors: %s', books_authors)

    def sort_books(self):
        all_books = self.search([])
        books_sorted = self.sort_books_by_date(all_books)
        logger.info('Books before sorting: %s', all_books)
        logger.info('Books after sorting: %s', books_sorted)

class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one('res.partner', ondelete='cascade')
    date_start = fields.Date('Member Since')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    date_of_birth = fields.Date('Date of birth')
