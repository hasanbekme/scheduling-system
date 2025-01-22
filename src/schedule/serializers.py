from rest_framework import serializers
from .models import Subject, Student, Tutor, Availability
import pytz
from datetime import datetime

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    subjects = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), many=True, required=False)
    
    class Meta:
        model = Tutor
        fields = '__all__'
        
class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = [
            'tutor_id', 'is_recurring', 'day_of_week', 'date', 'start_time', 'end_time',
        ]

    def create(self, validated_data):
        tutor_id = validated_data.pop('tutor_id')
        day_of_weak = validated_data.get('day_of_week')
        date = validated_data.get('date')
        start_time = validated_data.get('start_time')
        end_time = validated_data.get('end_time')
        is_recuring = validated_data.get('is_recurring')
        
        # Fetch tutor object
        tutor = Tutor.objects.get(id=tutor_id)
        
        tutor_tz = pytz.timezone(tutor.time_zone)
        
        if not is_recuring:
            utc_start_time = datetime.combine(date, start_time, tzinfo=tutor_tz).astimezone(pytz.utc)
            utc_end_time = datetime.combine(date, end_time, tzinfo=tutor_tz).astimezone(pytz.utc)
        else:
            utc_start_time = datetime.combine(date, start_time, tzinfo=tutor_tz).astimezone(pytz.utc)
            utc_end_time = datetime.combine(date, end_time, tzinfo=tutor_tz).astimezone(pytz.utc)
            
            

        # Store availability with the local times and tutor's time zone
        availability = Availability(
            tutor=tutor,
            time_zone=tutor.time_zone,
            **validated_data
        )

        availability.save()
        return availability