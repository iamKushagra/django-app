from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.


# def index(request):
#     return HttpResponse("This works!")


# def feb(request):
#     return HttpResponse("This also works!")

monthly_challenges = {
    "January": "Eat no meat for entire month",
    "February": "Walk for atleast 20 minutes every day",
    "March": "Walk for atleast 30 minutes every day",
    "April": "Learn Django",
    "May": "Learn Django in May",
    "June": "Learn Django in June",
    "July": "Learn Django in July",
    "August": "Learn Django in August",
    "September": "Learn Django in September",
    "October": "Learn Django in October",
    "November": "Learn Django in November",
    "December": "Learn Django in December",
}

# def monthly_challenge_by_number(request, month):
#     return HttpResponse(month)


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capital_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capital_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # return HttpResponseRedirect("/challenge/" + redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")
