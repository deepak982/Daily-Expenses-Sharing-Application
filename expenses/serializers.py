from rest_framework import serializers
from .models import User, Expense

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

    def validate_participants(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Participants should be a dictionary with user_id as key and amount or percentage as value.")
        return value
