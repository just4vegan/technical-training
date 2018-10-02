# -*- coding: utf-8 -*-
from odoo import models, fields

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    authors_ids = fields.Many2many('library.partner', string="Authors")
    edition_date =  fields.Date(string='Edition date',)
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')

class Book_Copies(models.Model):
    _name = 'library.copies'
    _inherits = 'library.book'
    
    internal_
    
    
#With our application, Brussel's library can now manage the rentals of books by customers. However, the librarians are not happy with the solution. The library usually has several copies of a given book, which makes the list of books full of redundant data. Moreover, they want to identify each copy of a book with a unique reference, which is internal to the library. Rentals should relate to the actual book copy that is borrowed.

#Add a specific data model for book copies. All the copies of a book should share the same, unique, book data (title, authors, ISBN, etc.) Every book copy should have a unique internal reference. Rentals should relate to book copies instead of books.

#Hint: Use delegation inheritance for book copies.