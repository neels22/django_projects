from django.shortcuts import render

# Create your views here.



def schedule(req):
    return render(req,"appointments.html")


def notification(req):
    return render(req,"notifications.html")

def history(req):
    return render(req,"med_history.html")


