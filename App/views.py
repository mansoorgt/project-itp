from django.shortcuts import render

# Create your views here.
def viewRegistraionPge(request):
    return render(request,'registration.html')

class ReginstraionForms():
    def speakerForm(request):
        return render(request,'speaker-reg.html')