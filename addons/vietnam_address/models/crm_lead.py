from odoo import models, fields, api

class Lead(models.Model):
    _inherit = 'crm.lead'

    province_id = fields.Many2one(
        'res.country.province',
        string='Province/City'
    )

    ward_id = fields.Many2one(
        'res.country.ward',
        string='Ward',
        # domain="[('district_id', '=', district_id)]"
    )


    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.province_id = self.partner_id.province_id.id
            self.ward_id = self.partner_id.ward_id.id
            self.street = self.partner_id.street
        else:
            self.province_id = False
            self.ward_id = False
            self.street = False





