from django.shortcuts import redirect, render

from .models import EventEnquiry



# Create your views here.

def event_enquiry(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        event_type = request.POST.get('event-type')
        venue = request.POST.get('venue')
        guests = request.POST.get('guests')
        message = request.POST.get('message')
        
        # Save form data to the database
        enquiry = EventEnquiry(
            contact_name=name,
            contact_email=email,
            contact_phone=phone,
            event_date=date,
            event_time=time,
            event_type=event_type,
            event_location=venue,
            number_of_guests=guests,
            additional_comments=message
        )
        enquiry.save()
        
    return render(request, 'customer/enquiry_form.html')
