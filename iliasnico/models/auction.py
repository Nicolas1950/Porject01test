from odoo import fields, api, models

class Auction(models.Model):
    _name = "iliasnico.auction"
    _description = "vente"

    name = fields.Char(string="Nom")
    lot_ids= fields.One2many(string="lots", comodel_name="iliasnico.lot", inverse_name="auction_id")