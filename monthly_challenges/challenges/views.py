from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthly_challenge = {
                     'january':"This in month of January",
                     'February':"This is month of February",
                     'march':"This is month of March",
                     'april':"This is month of April",
                     'may':"This is month of May",
                     'june':"This is month of June",
                     'july':"This is month of July",
                     'august':"This is month of August",
                     'september':"This is month of September",
                     'october':"This is month of October",
                     'november':'This is month of November',
                     'december':"This is month of December"
}
def index(request):
    res = ""
    for month in list(monthly_challenge.keys()):
        link = reverse('month-challenge',args =[month])
        res+= f"<li><u><a href=\"{link}\">{month.capitalize()}</a></u></li>"
    response_data = f"<ul>{res}<ul>"
    return HttpResponse(response_data)

def month_by_number(request, month):
    try:
        month_redirect = list(monthly_challenge.keys())[month-1]
        redirect_path = reverse('month-challenge', args =[month_redirect])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("This month is not supported")
def multiple_months(request, month):
    try:
        message = monthly_challenge[month.lower()]
        response_message = f"<h1>{message}</h1>"
        return HttpResponse(response_message)
    except:
        return HttpResponseNotFound("This month is not supported")
