from django.db import models
from django.urls import reverse




class IncomesCategory(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='incomes_category')

    def __str__(self):
        return self.name

    def get_incomes_category_url(self):
        return reverse("delete-incomes-category", args=[self.id])




class Incomes(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='incomes')
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.ForeignKey(IncomesCategory, on_delete=models.CASCADE, related_name='incomes')
    narration = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.amount} {self.user.currency}  {self.date}'




class ExpensesCategory(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='expenses_category')

    def __str__(self):
        return self.name

    def get_expenses_category_url(self):
        return reverse("delete-expenses-category", args=[self.id])


class Expenses(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name='expenses')
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=15)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE, related_name='expenses')
    narration = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.amount} {self.user.currency}  {self.date}'

