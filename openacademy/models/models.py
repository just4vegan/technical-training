from odoo import api, fields, models

'''The citadel of the seven kingdoms, located in Oldtown would like to use Odoo to manage the training of its future maesters. In this system, the citadel wants to create and edit classes, with different levels. They would like to handle different sessions given by different maesters at different moments. It would be nice to register the attendees of those sessions. Maester Aemon thinks it would be a good idea to differentiate the sessions in preparation from the ones that will actually be given, as well as having a way to archive the sessions, so they can find what they need as quickly as you can find a book in the Citadel's Library, which is the largest in Westeros.'''


class Citadel(models.Model):
    _description = 'Citadel'
    _name = 'openacademy.citadel' #pick not too much of an easy name
    _order = 'name'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.partner', string = 'Responsible')
    level = fields.Selection([(0, "Beginner"), (1, "Intermediate")])
#    session_ids = fields.One2many('openacademy.session', string= 'Session')
#    my_master = fields.Char()
    #my_moment = fields.Many2one('res.country.state', 'Fed. State', domain="[('country_id', '=', country)]")
#   if you use the .One2many command, you need you reference the table you are pointing too as the 2nd argument

class Session(models.Model):
    _description = 'Citadel'
    _name = 'openacademy.session' #pick not too much of an easy name
    _order = 'name'
    name = fields.Char(string='Name')
    
    
    