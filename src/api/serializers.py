from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotAcceptable

from api.models import FullCard


class FullCardSerializer(serializers.ModelSerializer):

    card_number = serializers.SerializerMethodField()
  
    def get_card_number(self, obj):
        return obj.get_card_info()
    
    class Meta:
        model = FullCard
        fields = ["id", "card_number"]


class InsertSerializer(serializers.Serializer):
    insert_mode = serializers.CharField()
    card_number = serializers.CharField(required=False)
    file_uploaded = serializers.FileField(required=False)

    def validate_insert_mode(self, value):
        if not value.lower() in ["single", "multiple"]:
            raise ValidationError("Invalid value for this field.")
        return value.lower()
    
    def validate_file_uploaded(self, value):
        content_type = value.content_type

        if content_type != "text/plain":
            raise NotAcceptable("File content type is not acceptable.")
        content_file = value.readlines()
        if len(content_file) < 3:
            raise ValidationError({"detail": "File content type is invalid or currupted."})
        return content_file
    
    def validate(self, obj):
        if obj.get("insert_mode")=="single" and not obj.get("card_number"):
            raise ValidationError("card_number field is required for insert_mode=single.")
        if obj.get("insert_mode")=="multiple" and not obj.get("file_uploaded"):
            raise ValidationError("file_uploaded field is required for insert_mode=multiple.")
        return obj

    class Meta:
        fields = "__all__"