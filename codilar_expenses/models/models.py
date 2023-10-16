from odoo import api, models, fields
import datetime
from odoo.exceptions import ValidationError


class ExpenseTypes(models.Model):
    _name = 'expense.type'

    name = fields.Char(string="Expense Type")


class AddingField(models.Model):
    _inherit = 'hr.expense'

    expense_type = fields.Many2one('expense.type', string="Expense Type")
    due_date = fields.Date(string="Due date")
    forcast = fields.Float(string="Forcast")
    paid = fields.Float(string="Paid")
    unpaid = fields.Float(string="Carry forward", compute='_compute_unpaid_amount')
    boolean = fields.Boolean(string="Pending", default=False)

    def name_get(self):
        res = []
        for expense in self:
            expense_type_name = expense.expense_type.name if expense.expense_type else ''
            display_name = f"{expense_type_name} - {expense.name}" if expense_type_name else expense.name
            res.append((expense.id, display_name))
        return res

    @api.depends('paid', 'forcast')
    def _compute_unpaid_amount(self):
        for rec in self:
            rec.unpaid = rec.forcast - rec.paid

    @api.constrains('paid', 'forcast')
    def _check_paid_less_than_forcast(self):
        for rec in self:
            if rec.forcast < rec.paid:
                raise ValidationError("Paid amount should not greater than forcast")
