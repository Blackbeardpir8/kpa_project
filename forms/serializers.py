from rest_framework import serializers
from forms.models import *


# Bogie Serializers 
class BogieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieDetails
        exclude = ['form']

class BogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheet
        exclude = ['form']

class BMBCChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BMBCChecksheet
        exclude = ['form']

class BogieFormSerializer(serializers.ModelSerializer):
    bogieDetails = BogieDetailsSerializer()
    bogieChecksheet = BogieChecksheetSerializer()
    bmbcChecksheet = BMBCChecksheetSerializer()

    class Meta:
        model = BogieForm
        fields = ['formNumber', 'inspection_by', 'inspection_date',
                'bogieDetails', 'bogieChecksheet', 'bmbcChecksheet']

    def create(self, validated_data):
        bogie_details_data = validated_data.pop('bogieDetails')
        bogie_checksheet_data = validated_data.pop('bogieChecksheet')
        bmbc_checksheet_data = validated_data.pop('bmbcChecksheet')

        form = BogieForm.objects.create(**validated_data)

        BogieDetails.objects.create(form=form, **bogie_details_data)
        BogieChecksheet.objects.create(form=form, **bogie_checksheet_data)
        BMBCChecksheet.objects.create(form=form, **bmbc_checksheet_data)

        return form
    
    def validate_inspection_by(self, value):
        if not value.strip():
            raise serializers.ValidationError("inspection_by cannot be empty.")
        return value


# Wheel Serializers
class WheelFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelFields
        exclude = ['form']

class WheelFormSerializer(serializers.ModelSerializer):
    fields = WheelFieldsSerializer()

    class Meta:
        model = WheelForm
        fields = ['formNumber', 'submittedBy', 'submittedDate', 'fields']

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        form = WheelForm.objects.create(**validated_data)
        WheelFields.objects.create(form=form, **fields_data)
        return form

    def validate_formNumber(self, value):
        if not value.startswith('WHEEL-'):
            raise serializers.ValidationError("Form number must start with 'WHEEL-'")
        return value

    