# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    authors_ids = fields.Many2many('library.partner', string="Authors")
    edition_date =  fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')
    total = fields.Float(default = 1.0)
    qty = fields.Float(default = 1.0)
    total = fields.Float()
    cost = fields.Float(default = 1.0)
    
    all_info = fields.Char(compute='_compute_all_info', string='All info')
    
    @api.depends('name', 'isbn')
    def _compute_all_info(self):
        for line in self:
            line.all_info = "%s, (%s)" % (line.name, line.isbn)

    @api.onchange('cost', 'qty')
    def _onchange_costqty(self):
        self.total = self.cost * self.qty
        
    @api.constrains('qty') 
    def _check_money_(self):
        for cash in self:
            if cash.qty > 5:
                raise ValidationError("Your Number is too high!")
                
                

        

        