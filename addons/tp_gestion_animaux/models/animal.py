from odoo import models, fields

class Animal(models.Model):
    _name = "tp.animal"
    _description = "Animal de compagnie"

    name = fields.Char(string="Nom de l'animal", required=True)
    espece = fields.Selection([
        ('chien', 'Chien'),
        ('chat', 'Chat'),
        ('autre', 'Autre'),
    ], string="Espèce")

    race = fields.Char(string="Race")
    date_naissance = fields.Date(string="Date de naissance")
    proprietaire = fields.Char(string="Propriétaire")

    # Relation One2many vers les vaccins
    vaccin_ids = fields.One2many(
        'tp.vaccin',     # modèle Vaccin
        'animal_id',     # champ Many2one de vaccin
        string='Vaccins'
    )
