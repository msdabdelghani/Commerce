from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django import forms
from django.forms import BaseModelFormSet

from .models import User, Auction_listing, Bid, Comment, Category

class NewAuctionForm(forms.Form):
    title = forms.CharField(label="New Title")
    description = forms.CharField(label="New Description", widget=forms.Textarea)
    startingBid = forms.DecimalField(label="Starting Bid", max_digits=19, decimal_places=2)
    image = forms.CharField(label="Image", required=False)
    categories = forms.CharField(label="Category", required=False)

def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction_listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("auctions:index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("auctions:index"))
    else:
        return render(request, "auctions/register.html")

def add(request):   
    if request.method == "POST":
        a1 = Auction_listing()
        c1 = Category()
        form = NewAuctionForm(request.POST)
        if form.is_valid():
            a1.name = form.cleaned_data["title"]
            a1.description = form.cleaned_data["description"]
            a1.price = form.cleaned_data["startingBid"]
            a1.image = form.cleaned_data["image"]
            a1.save()
            c1.name = form.cleaned_data["categories"]
            c1.save()
            a1.categories.add(c1)

            return HttpResponseRedirect(reverse("auctions:index"))
        else:
            return render(request, "auctions/add.html", {
                "form": form
            })
    
    return render(request, "auctions/add.html", {
            "form": NewAuctionForm()
        })

def auction(request, auction_id):
    auction = Auction_listing.objects.get(pk = auction_id)
    return render(request, "auctions/auction.html", {
        "auction": auction
    })