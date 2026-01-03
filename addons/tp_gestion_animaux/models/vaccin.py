from odoo import models, fields

class Vaccin(models.Model):
    _name = "tp.vaccin"
    _description = "Vaccin"

    name = fields.Char(string="Nom du vaccin", required=True)
    date_vaccination = fields.Date(string="Date de vaccination")
    veterinaire = fields.Char(string="Vétérinaire")

    animal_id = fields.Many2one(
        "tp.animal",
        string="Animal"
    )
