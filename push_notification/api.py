from tastypie.resources import ModelResource
from push_notification.models import Subscriber


class SubscriberResource(ModelResource):
    class Meta:
        queryset = Subscriber.objects.all()
        resource_name = 'subscriber'