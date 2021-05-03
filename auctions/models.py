from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    pass

class Auction_listing(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    image =  models.ImageField(blank = True)
    def __str__(self):
        return f"{self.name} ({self.description})"

class Bid(models.Model):
    value = models.DecimalField(max_digits=19, decimal_places=2)
    bid_auction = models.ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="bids")
    orderer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orderers")
    def __str__(self):
        return f"{self.value}"

class Comment(models.Model):
    content = models.CharField(max_length = 555)
    auction_commented = models.ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="auctions")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    def __str__(self):
        return f"{self.value}"

class Category(models.Model):
    name = models.CharField(max_length = 64)
    auction_categories = models.ManyToManyField(Auction_listing, blank=True, related_name="categories")
    

