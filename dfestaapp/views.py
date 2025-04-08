from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from . models import studentDetails
from . models import paymentDetails
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def events(request):
    return render(request,'events.html')

def registrations(request):
    return render(request,'registration.html')

def info(request):
    return render(request,'info.html')

def event(request):
    event_name = request.GET.get('event')
    event = {}
    if event_name == "bughunt":
        event = {"name": "Bug Hunt", "description": "A fun event to find bugs in the code!", "img":"bughunt.jpeg"}
    if event_name == "cinelens":
        event = {"name": "Cine Lens", "description": "A film-making competition!", "img":"cinelens.jpeg"}
    if event_name == "datapirates":
        event = {"name": "Data Pirates", "description": "A data analysis competition!", "img":"datapirates.jpeg"}
    if event_name == "E-Sports":
        event = {"name": "E-Sports", "description": "A gaming competition!", "img":"esports.jpeg"}
    if event_name == "f2":
        event = {"name": "F2", "description": "A Formula 2 racing event!", "img":"f2.jpeg"}
    if event_name == "Fun-Activities":
        event = {"name": "Fun Factory", "description": "A fun event with games and activities!", "img":"funfactory.jpeg"}
    if event_name == "mindmaze":
        event = {"name": "Mind Maze", "description": "A puzzle-solving competition!", "img":"mindmaze.jpeg"}
    if event_name == "paperpresentation":
        event = {"name": "Paper Presentation", "description": "A competition to present research papers!", "img":"paperpresentation.jpeg"}
    if event_name == "projectexpo":
        event = {"name": "Project Expo", "description": "An exhibition of innovative projects!", "img":"projectexpo.jpeg"}
    if event_name == "squidgame":
        event = {"name": "Squid Game", "description": "A fun game event!", "img":"squidgame.jpeg"}
    if event_name == "Quiz":
        event = {"name": "Tech Quiz", "description": "A quiz competition on technology!", "img":"techquiz.jpeg"}
        event = {"name": "Tech Quiz", "description": "A quiz competition on technology!", "img":"techquiz.jpeg"}
    if event_name == "visionverse":
        event = {"name": "Vision Verse", "description": "A competition to showcase your vision!", "img":"visionverse.jpeg"}
    if event_name == "web":
        event = {"name": "Web Xpress", "description": "A web development competition!", "img":"webxpress.jpeg"}

    return render(request,'event_detail.html', {'event':event})


def register(request):
    eventname = request.GET.get('event')
    if request.method == "POST":
        fullname = request.POST.get('name')
        emailid = request.POST.get('email')
        phonenumber = request.POST.get('phone')
        department = request.POST.get('department')
        year = request.POST.get('year')
        event = request.POST.get('event')

        obj = studentDetails(fullname = fullname , email = emailid , phone = phonenumber , dept = department , year = year , event = event)
        obj.save()
        
        request.session['registration_id'] = obj.id

        if obj:
            messages.success(request, f'Student Details Saved Successfully')
        else:
            messages.error(request, 'Failed')

        return redirect('payment')
        
    return render(request ,'register.html' , {'eventname':eventname,'message':'Saved Successfully'})


def payment(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        utr = request.POST.get('utr')

        if not image or not utr:
            messages.error(request, "All fields are required!")
            return redirect('payment') 
        
        try:
            payobj = paymentDetails(image = image , utr = utr)
            payobj.save()
        
            id = request.session['registration_id']
            if id:
                s = studentDetails.objects.get(id=id)
                s.payment_verified = True
                s.save()
                messages.success(request, "Payment uploaded successfully.")

            else:
                messages.error(request, "Session expired. Please try again.")

        except IntegrityError:
            messages.error(request, 'Payment Failed')

        return redirect('payment')

    return render(request,'payment.html')

def registrationDetails(request):

    data = studentDetails.objects.filter(payment_verified = True)

    return render(request,'regDet.html',{'data':data})

def technical_events(request):
    return render(request, 'technical.html')

def non_technical_events(request):
    return render(request, 'non_technical.html')

def sports_events(request):
    return render(request, 'sports.html')

def e_sports_events(request):
    return render(request, 'e_sports.html')
