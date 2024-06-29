from rest_framework import serializers
from adminapi.models import *



class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Manager
        fields="__all__"
        

class TeamleadSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamLead
        fields="__all__"

    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
        

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Meeting
        fields=["title","link","date","time"]
        

class MeetingListSerializer(serializers.ModelSerializer):
    organizer=serializers.CharField(read_only=True)
    class Meta:
        model=Meeting
        fields="__all__"
        

class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Technologies
        fields="__all__"
        
        
class TaskchartSerializer(serializers.ModelSerializer):
    project_detail=serializers.CharField(read_only=True)
    assigned_person=serializers.CharField(read_only=True)
    class Meta:
        model=TaskChart
        fields="__all__"
        
        
 