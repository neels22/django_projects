from django.shortcuts import render

# Create your views here.



def medication(req):
    return render(req,"medication.html")

def view_pat(req):
    return render(req,"view_patient.html")