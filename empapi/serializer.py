from rest_framework import serializers
from adminapi.models import *



class ProfileEditSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    
    class Meta:
        model=Employee
        fields=["id","name","email_address","phoneno","home_address","job_title","department","linkedin_profile","resume"]

   
    
class TeamSerializer(serializers.ModelSerializer):
    teamlead=serializers.CharField(read_only=True)
    members=serializers.SerializerMethodField()

    def get_members(self, obj):
        return [member.employee.name for member in obj.members.all()]    

    class Meta:
        model=Teams
        fields="__all__"
        

class ProjectAssignSerializer(serializers.ModelSerializer):
    teamlead=serializers.CharField(source='teamlead.name', read_only=True)
    project=serializers.CharField(source='project.topic', read_only=True)
    team=serializers.CharField(source='team.name', read_only=True)
    class Meta:
        model=Project_assign
        fields="__all__"
        
        
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    projectassigned=serializers.CharField(source='projectassigned.topic', read_only=True)
    teamlead=serializers.CharField(source='teamlead.name', read_only=True)
    assigned_person=serializers.CharField(source='assigned_person.name', read_only=True)
    class Meta:
        model=ProjectDetail
        fields="__all__"    
         
        
        
class ProjectUpdatesSerializer(serializers.ModelSerializer):
    project=serializers.CharField(read_only=True)
    class Meta:
        model=ProjectUpdates
        fields="__all__"     
        


class TaskChartSerializer(serializers.ModelSerializer):
    project_detail=serializers.CharField(read_only=True)
    assigned_person=serializers.CharField(read_only=True)
    start_date=serializers.CharField(read_only=True)
    end_date=serializers.CharField(read_only=True)
    total_days=serializers.CharField(read_only=True)
    class Meta:
        model=TaskChart
        fields="__all__"

        
class TaskUpdateChartSerializer(serializers.ModelSerializer):
    task=serializers.CharField(read_only=True)
    updated_by=serializers.CharField(read_only=True)    
    date_updated=serializers.CharField(read_only=True)
    class Meta:
        model=TaskUpdateChart
        fields="__all__"
        

class MeetingListSerializer(serializers.ModelSerializer):
    organizer=serializers.CharField(read_only=True)
    class Meta:
        model=Meeting
        fields="__all__"
        

class TechnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Technologies
        fields="__all__"
        
        
class DailyTaskSerializer(serializers.ModelSerializer):
    teamlead=serializers.CharField(read_only=True)
    emp=serializers.CharField(read_only=True)
    class Meta:
        model=DailyTask
        fields="__all__"
        

class RatingSerializer(serializers.ModelSerializer):
    teamlead=serializers.CharField(read_only=True)
    class Meta:
        model=Rating
        fields="__all__"