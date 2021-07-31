from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "This is a simple module to test odoo"

    name = fields.Char(required=True)
    description = fields.Text()  # text                       
    postcode = fields.Char()  # character varying          
    date_availability = fields.Date()  # date                       
    expected_price = fields.Float(required=True)  # double precision           
    selling_price = fields.Float()  # double precision           
    bedrooms = fields.Integer()  # integer                    
    living_area = fields.Integer()  # integer                    
    facades = fields.Integer()  # integer                    
    garage = fields.Boolean()  # boolean                    
    garden = fields.Boolean()  # boolean                    
    garden_area = fields.Integer()  # integer                    
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])  # character varying          
    active = fields.Boolean()  # boolean       
    state = fields.Selection([
        ('new', 'New'), 
        ('received', 'Offer Received'), 
        ('accepted', 'Offer Accepted'), 
        ('sold', 'Sold'), 
        ('canceled', 'Canceled')], 
        required=True, default='new')
    
    property_type_id = fields.Many2one("estate.property.typ", string="Type")
