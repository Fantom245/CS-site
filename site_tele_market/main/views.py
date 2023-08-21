from django.shortcuts import render


def main(request):
    return render(request, "main/main_page.html")


def buy_filter(request):
    return render(request, "main/buy_filter.html")


def sell(request):
    return render(request, "main/sell_.html")


def buy_filter_2(request):
    return render(request, "main/buy_filter_2.html")




