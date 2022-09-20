from rest_framework.serializers import ModelSerializer
from mainapp.models import SendMail
from mainapp.send_email import send_mail_to_email


class SendMailSerializer(ModelSerializer):
    class Meta:
        model = SendMail
        fields = ('full_name', 'email', 'message', 'phone_number', )
        read_only_fields = ('date', )
        
    def create(self, validated_data):
        send_mail_to_email(
            validated_data['full_name'],
            validated_data['email'],
            validated_data['message'],
            validated_data['phone_number']
        )
        email = SendMail.objects.create(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            message=validated_data['message'],
            phone_number=validated_data['phone_number']
        )
        return email