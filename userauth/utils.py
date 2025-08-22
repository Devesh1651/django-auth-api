import random
from django.core.mail import send_mail
from django.conf import settings
import redis


redis_client = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)


def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    subject = 'Your OTP for Account Verification'
    message = f'Your One-Time Password (OTP) is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    print(f"OTP for {email}: {otp}") 

    redis_client.setex(f"otp:{email}", 300, otp)
