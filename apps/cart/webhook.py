import json
import stripe 

from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import EmailMultiAlternatives

from .cart import Cart
from apps.order.views import render_to_pdf
from apps.order.models import Order

@csrf_exempt
def webhook(request):
    payload = request.body
    event = None

    stripe.api_key = settings.STRIPE_API_KEY_HIDDEN

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        return HttpResponse(status=400)

    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object
        order = Order.objects.get(payment_intent=payment_intent.id)
        order.paid = True
        order.save()
        
        for item in order.items.all():
            product=item.product
            product.num_available-=item.quantity
            product.save()
            
        subject="Order Confirmation"
        from_email ='noreply@shop.com'
        to=['mail@shop.com', order.email]
        text_content='Your Order is successfull'
        html_content=render_to_string('email_confirmation.html',{'order':order})
        pdf=render_to_pdf('order_pdf.html',{'order':order})
        
        msg=EmailMultiAlternatives(subject,text_content,from_email,to)
        msg.attach_alternative(html_content,"text/html")
        
        if pdf:
            name="order_%s.pdf" % order.id
            msg.attach(name,pdf,'application/pdf')
        msg.send()
        #html=render_to_string('email_confirmation.html',{'order':order})
        #send_mail('Order confirmation','Your Order is successfull','noreply@shop.com',['mail@shop.com', order.email], fail_silently=False,html_message=html)

    return HttpResponse(status=200)