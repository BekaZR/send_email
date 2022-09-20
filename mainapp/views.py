
from mainapp.serializers import SendMailSerializer
from mainapp.models import SendMail
from rest_framework.generics import CreateAPIView


class SendMailView(CreateAPIView):
    queryset = SendMail.objects.all()
    serializer_class = SendMailSerializer


