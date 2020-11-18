from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
def payment(request):
    if request.method=="GET":
        amount = request.GET.get("amount")
        email = request.GET.get("email")
        content = f"Payment recieved of {amount} recieved"
        send_mail("Payment Gateway Integration", content, "paymentnone8@gmail.com", [email])
        context = {
            "amount":amount
        }
    return render(request,"payment.html",context)
    