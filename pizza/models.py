from django.db import models

class Pizza(models.Model):
    """The name of different kinds of Pizzas"""
    name = models.CharField(max_length=200)
    #date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name
        
        
class Topping(models.Model):
    """Give a description of the Pizza"""
    pizza = models.ForeignKey(Pizza)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'toppings'
    
    def __str__(self):
        """Return a string representation of the model."""
        return self.name[:50] + "..."
