from django.shortcuts import render
from company.models import ContactUs
from django.http import JsonResponse



def contact(request):
    return render(request, 'company/contact.html')



def ajax_contact_form(request):
    full_name = request.GET['full_name']
    email = request.GET['email']
    phone = request.GET['phone']
    subject = request.GET['subject']
    message = request.GET['message']

    contact = ContactUs.objects.create(
        full_name=full_name,
        email=email,
        phone=phone,
        subject=subject,
        message=message,
    )
    data = {
        'bool': True,
        'message': "Message sent successfully"
    }
    return JsonResponse({"data":data})






def about_us(request):
    return render(request, 'company/about_us.html')

def purchase_guide(request):
    return render(request, 'company/purchase_guide.html')


def privacy_policy(request):
    return render(request, 'company/privacy_policy.html')

def terms_of_services(request):
    return render(request, 'company/terms_of_services.html')
