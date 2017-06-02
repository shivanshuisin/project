from django.shortcuts import render

def Redirect(request):
    return render(request,'final/Index.html')
def Login(request):
    return render(request,'final/Login.html')