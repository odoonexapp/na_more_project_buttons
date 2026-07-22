from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    dropship_picking_count = fields.Integer(
        related="sale_order_id.dropship_picking_count",
        string="Dropship Picking Count",
    )

    def action_view_dropship(self):
        return self.sale_order_id.action_view_dropship()

    def action_view_purchase_orders(self):
        return self.sale_order_id.action_view_purchase_orders()

    def _get_stat_buttons(self):
        buttons = super()._get_stat_buttons()
        sale_order = self.sudo().sale_order_id
        if self.env.user.has_group('stock.group_stock_user'):
            buttons.append({
                'icon': 'truck',
                'text': self.env._('Dropshipping'),
                'number': sale_order.dropship_picking_count,
                'action_type': 'object',
                'action': 'action_view_dropship',
                'show': sale_order.dropship_picking_count > 0,
                'sequence': 2,
            })
        if self.env.user.has_group('purchase.group_purchase_user'):
            buttons.append({
                'icon': 'credit-card',
                'text': self.env._('Purchase'),
                'number': sale_order.purchase_order_count,
                'action_type': 'object',
                'action': 'action_view_purchase_orders',
                'show': sale_order.purchase_order_count > 0,
                'sequence': 2,
            })
        return buttons
