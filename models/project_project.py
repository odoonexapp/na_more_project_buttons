from odoo import _, api, fields, models, _lt

class ProjectProject(models.Model):
    _inherit = "project.project"
    
    dropship_picking_count = fields.Integer(
        related="sale_order_id.dropship_picking_count",
        store=True,
        string="Dropship Picking Count"
    )
    
    def action_view_dropship(self):
        return self.sale_order_id.action_view_dropship()
    
    def action_view_purchase_orders(self):
        return self.sale_order_id.action_view_purchase_orders()
    
    def _get_stat_buttons(self):
        buttons = super(ProjectProject, self)._get_stat_buttons()
        if self.user_has_groups('stock.group_stock_user'):
            buttons.append({
                    'icon': 'truck',
                    'text': _lt('Dropshipping'),
                    'number': self.sale_order_id.dropship_picking_count,
                    'action_type': 'object',
                    'action': 'action_view_dropship',
                    'show': self.sale_order_id.dropship_picking_count>0,
                    'sequence': 2,
                })
        if  self.user_has_groups('purchase.group_purchase_user'):
            buttons.append({
                        'icon': 'credit-card',
                        'text': _lt('Purchase'),
                        'number': self.sale_order_id.purchase_order_count,
                        'action_type': 'object',
                        'action': 'action_view_purchase_orders',
                        'show': self.sale_order_id.purchase_order_count>0,
                        'sequence': 2,
                    })
        return buttons
