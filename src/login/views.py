from django.shortcuts import render_to_response


def login(request):
    return render_to_response('login.html')


def registration(request):
    return render_to_response('settings.html')
