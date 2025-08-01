from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_price_in_cents(self):
        """
        Convert price to cents for Stripe
        """
        return int(self.price * 100)

    class Meta:
        ordering = ['-created_at']
