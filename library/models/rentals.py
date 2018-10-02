# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')
    rental_date = fields.Date(string='Rental date')
    return_date = fields.Date(string='Return date')
    

    
#    def _compute_total(self):
 #       """
  #      get and sum the order lines' price
   #     """
    #    self.total = sum(
     #       orderline.price for orderline in self.order_line_ids)

        
        
'''In the first module, we created a basic library module with information on the book, publisher and customer. When renting a book, we would like to display as much information as possible on the renting form (about both the customer and the book) but without having to set this information all over again. Find ways to be informative and avoids adding workload to the librarians.'''

# price_subtotal = fields.Float(compute='_compute_amount_line_all', digits=0, string='Subtotal w/o Tax')