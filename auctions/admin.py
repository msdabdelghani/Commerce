from django.contrib import admin
from .models import Auction, Comment, Bid, User, Category

# Register your models here.

admin.site.register(Auction)

admin.site.register(Comment)

admin.site.register(Bid)

admin.site.register(User)

admin.site.register(Category)


