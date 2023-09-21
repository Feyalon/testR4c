# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from robots.models import Robot

@receiver(post_save, sender=Robot)
def notify_robot_availability(sender, instance, **kwargs): # сразу тут пишу что я не SMTP не настраивал.
    if instance.avaible:
        subject = "Ваш робот доступен в наличии"
        message = f"Добрый день!\n\nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.\nЭтот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
        send_mail(subject, message, "test1@example.com", ["test2@example.com"])
    else:
        pass
