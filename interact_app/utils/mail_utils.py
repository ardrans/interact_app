from django.core.mail import send_mail
from .redis_utils import *
from django.core.mail import send_mail, BadHeaderError

#secret_code = key()

def send_verification_email():
    try:
        print('mail')
        secret_code = key()
        status = send_mail(
            'Confirmation link',
            f'http://localhost:8000/verify_email?key={secret_code}',
            'nsardra@gmail.com',
            ['nsardra@gmail.com'],
            fail_silently=True,
        )
        #print(status)
    except BadHeaderError as e:
        print(f"Error occurred while sending the email: {str(e)}")
