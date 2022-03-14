from odoo import fields, api, models

class Lot(models.Model):
    _name = "iliasnico.lot"
    _description = "lot"

    name = fields.Char(string="Nom")
    auction_id = fields.Many2one(string="vente",comodel_name="iliasnico.auction")
