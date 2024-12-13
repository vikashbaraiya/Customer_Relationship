from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Order, Customer, Employee, Supplier
from django.contrib.auth.models import User
from django.conf import settings



@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created:
        customer = instance.customer
        subject = 'Order Confirmation'
        message = render_to_string('order_confirmation_email.html', {
            'customer': customer,
            'order': instance,
        })
        send_mail(subject, message, 'your-email@example.com', [customer.email], fail_silently=False)


@receiver(post_save, sender=Order)
def send_order_delivery_email(sender, instance, **kwargs):
    if instance.status == 'Delivered':
        customer = instance.customer
        subject = 'Order Delivered'
        message = render_to_string('delivery_confirmation_email.html', {
            'customer': customer,
            'order': instance,
        })
        send_mail(subject, message, 'your-email@example.com', [customer.email], fail_silently=False)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Platform!'
        message = render_to_string('user_registration_email.html', {
            'user': instance,
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email], fail_silently=False)



@receiver(post_save, sender=Customer)
def send_customer_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Customer Registration Confirmation'
        message = render_to_string('customer_registration_email.html', {
            'customer': instance,
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email], fail_silently=False)



@receiver(post_save, sender=Employee)
def send_employee_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Company'
        message = render_to_string('employee_registration_email.html', {
            'employee': instance,
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email], fail_silently=False)


@receiver(post_save, sender=Supplier)
def send_supplier_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Supplier Registration Confirmation'
        message = render_to_string('supplier_registration_email.html', {
            'supplier': instance,
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email], fail_silently=False)