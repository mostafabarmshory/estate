from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Types of a property"

    name = fields.Char(required=True)
    description = fields.Text()  # text                       
