from rest_framework import serializers

from credit_terms.models import Credit_terms


class CredittermsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Credit_terms
        fields = ['id', 'title', 'description', 'file', 'created_at', 'updated_at']
