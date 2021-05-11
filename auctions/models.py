from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

from django.db.models.fields import BooleanField
from django.db.models.fields.related import ManyToManyField

class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length = 64)
    def __str__(self):
        return f"Category : {self.name}"


class Auction_listing(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    image =  models.CharField(max_length = 555, blank = True)
    categories = models.ManyToManyField(Category, blank=True, related_name="auction_categories")
    def __str__(self):
        return f"{self.name} ({self.description})"

class Bid(models.Model):
    value = models.DecimalField(max_digits=19, decimal_places=2)
    bid_auction = models.ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="bids")
    orderer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orderers")
    def __str__(self):
        return f"{self.orderer} gave : {self.value} for : {self.bid_auction}"

class Comment(models.Model):
    content = models.CharField(max_length = 555)
    auction_commented = models.ForeignKey(Auction_listing, on_delete=models.CASCADE, related_name="auctions")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    def __str__(self):
        return f"{self.auction_commented} : {self.content} by {self.author}"

class Watchlist(models.Model):
    added = models.BooleanField( default = False )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owners")
    items = models.ManyToManyField(Auction_listing, blank=True, related_name="auction_items")
    
    def __str__(self):
        if self.added:
            return f"The owner of this watchlist is {self.owner}"
