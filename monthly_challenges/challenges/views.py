from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
                     'december': None
}
def index(request):
    months = list(monthly_challenge.keys())
    return render(request, "challenges/index.html", {
        "months":months
    })

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
        return render(request, "challenges/challenge.html", {
            "text": message,
            "month":month
        })
    except:
        raise Http404()
