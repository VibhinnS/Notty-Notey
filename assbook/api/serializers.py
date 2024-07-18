from rest_framework.serializers import ModelSerializer
from .models import Note
class Note_Serializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'