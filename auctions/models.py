from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm


class Comment(models.Model):
    content = models.CharField(max_length = 555)

class Bid(models.Model):
    price =  models.DecimalField(max_digits=19, decimal_places=10)
    STATUS = (
        ('Y', 'Your bid is the current bid'),
        ('N', ''),
    )

    status = models.CharField(max_length=1, choices=STATUS)

class Auction(models.Model):
    title = models.CharField(max_length = 255)
    subtitle = models.CharField(max_length = 555)
    initialprice = models.DecimalField(max_digits=19, decimal_places=10)
    comments = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE, related_name="related_comments")
    bids = models.ForeignKey(Bid, null=True, blank=True, on_delete=models.CASCADE, related_name="offers")
    image = models.ImageField(upload_to='auctions/img/', null=True, blank=True)

class Category(models.Model):
    label = models.CharField(max_length = 255)
    auctions = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="auction_listing")

class User(AbstractUser):
    user_bids = models.ForeignKey(Bid, null=True, blank=True, on_delete=models.CASCADE, related_name="user_bids")
    user_auctions = models.ForeignKey(Auction, null=True, blank=True, on_delete=models.CASCADE, related_name="user_auctions")
    user_comments = models.ForeignKey(Comment,null=True, blank=True, on_delete=models.CASCADE, related_name="user_comments")
    pass
 
class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = ['title', 'subtitle', 'initialprice', 'image']