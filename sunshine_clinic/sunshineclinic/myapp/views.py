from django.shortcuts import render,redirect
from .models import Review
from .models import Appointment
from django.core.mail import send_mail
from django.http import JsonResponse

def index(request):
    return render(request,'index.html')

def form(request):
    if request.method == 'GET':
        return render(request, 'form.html')

    return render(request, 'error.html')

def reg(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        phone = request.GET.get('phone')
        date = request.GET.get('date')
        time = request.GET.get('time')

        appointment = Appointment(name=name, email=email, phone=phone, date=date, time=time)
        appointment.save()

        # Perform any additional actions (e.g., send notifications)

        subject = 'New Appointment'
        message = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nDate: {date}\nTime: {time}'
        from_email = 'your-email@example.com'
        to_email = ['doctor@example.com']
        send_mail(subject, message, from_email, to_email, fail_silently=False)

        return JsonResponse({'success': True, 'message': 'Appointment submitted successfully'})

        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def review(request):
    return render(request,'review.html')

def rev(request):
    if request.method == 'GET':
        user = request.GET.get('user')
        rating = request.GET.get('rating')
        comment = request.GET.get('comment')
        if user and rating and comment:
            Review.objects.create(user=user, rating=rating, comment=comment)
            return redirect('reviews')
    reviews = Review.objects.all()[:4]  # Fetch limited reviews
    return render(request, 'index.html', {'reviews': reviews})
def index(request):
    reviews = Review.objects.all()[:4]  # Fetch limited reviews
    return render(request, 'index.html', {'reviews': reviews})
def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'all_reviews.html', {'reviews': reviews})