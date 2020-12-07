from django.shortcuts import render, Http404, HttpResponse
from django.http import JsonResponse
import json
from push_notification.models import Subscriber
import datetime
import logging
import os
from django_push_server.settings import (
    WEBPUSH_VAPID_PUBLIC_KEY,
    WEBPUSH_VAPID_PRIVATE_KEY,
    WEBPUSH_CLAIMS,
)
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return render(
        request,
        "push_notification/index.html",
        {
            "message": "the webapp is currently loading..."
        },
    )

@csrf_exempt
def subscription(request):
    """
        POST creates a subscription
        GET returns vapid public key which clients uses to send around push notification
    """
    method = request.method
    if "GET" == method:
        return HttpResponse(
            json.dumps({"public_key": WEBPUSH_VAPID_PUBLIC_KEY}),
            content_type="application/json",
            status=200,
        )
    elif "POST" == method:
        # TODO request body have to be json or return error
        payload = json.loads(request.body.decode('utf8'))
        subscription_info = payload['subscription_info']
        if None is subscription_info:
            return HttpResponse(
                "There is an error on you subscriber json data format"
            )

        # we assume subscription_info shall be the same
        subscriber = Subscriber.objects.filter(
            subscription_info = subscription_info
        ).first()
        if None is subscriber:
            subscriber = Subscriber()
            subscriber.subscription_info = subscription_info

        subscriber.modified = datetime.datetime.now(datetime.timezone.utc)
        subscriber.save()

        return JsonResponse(
            {'id': subscriber.id},
        )
    else:
        not_found_msg = "Page not found"
        logging.error(not_found_msg)
        return Http404(not_found_msg)


@csrf_exempt
def notify(request):
    message = (
        request.GET.get("message")
        if request.GET
        else "Updates \
        available"
    )
    howMany = Subscriber.objects.all().count()
    if howMany > 0:
        for subscriber in Subscriber.objects.all():
            try:
                send_push_notification(
                    json.loads(subscriber.subscription_info), message
                )
            except Exception as e:
                logging.error(e)
    else:
        return HttpResponse("there is no subscribers to notify")

    return HttpResponse("{} notification(s) sent".format(howMany))


@csrf_exempt
def send_push_notification(subscription_info, message):
    from pywebpush import webpush, WebPushException

    subscriber = Subscriber.objects.filter(
        Subscriber.subscription_info == subscription_info
    ).first()
    try:
        webpush(
            subscription_info=subscriber.subscription_info_json,
            data=message,
            vapid_private_key=WEBPUSH_VAPID_PRIVATE_KEY,
            vapid_claims=WEBPUSH_CLAIMS
        )
    except WebPushException as e:
        logging.exception("webpush fail {}".format(e))
