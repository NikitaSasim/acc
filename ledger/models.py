from django.db import models

# import international.models
# choices = international.models.currencies
#
# class Currency(models.Model):
#       currency_code = models.CharField(max_length=100, choices=choices)


class IncomeCategory(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='income_category')

    def __str__(self):
        return self.name


class Income(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='incomes')
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE, related_name='incomes')
    narration = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.amount} {self.user.currency}  {self.date}'


class ExpensesCategory(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='expenses_category')

    def __str__(self):
        return self.name


class Expenses(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE, related_name='expenses')
    narration = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.amount} {self.user.currency}  {self.date}'
