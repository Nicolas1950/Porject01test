from odoo import fields, api, models

class Lot(models.Model): 
    _name = "moduletest.lot"
    _description = "Un petit test"

    name = fields.Char(string="Nom du Lot")
    auction_id = fields.Many2one(string="Vente", comodel_name="moduletest.auction")