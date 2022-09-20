from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def send_mail_to_email(full_name, email, message, phone_number):
    data = {
        'full_name': full_name,
        "email": email,
        'message': message,
        'phone_number': phone_number
    }
    html_body = render_to_string('mail.html', data)
    msg = EmailMultiAlternatives(subject='Здравствуйте', to=[email])
    msg.attach_alternative(html_body, 'text/html')
    msg.send()