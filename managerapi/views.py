from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from rest_framework.decorators import action
from django.db.models import Count, Sum, F, ExpressionWrapper, FloatField

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


from adminapi.models import *
from managerapi.serializer import *



class ManagerCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_type="manager")
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

class EmployeeCreateView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def post(self,request,*args,**kwargs):
        serializer=EmpRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            manager_id=request.user.username
            serializer.save(user_type="employee",manager_name=manager_id)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        
        
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_obj=Manager.objects.get(id=user.id)
        if user_obj:
            token, created = Token.objects.get_or_create(user=user)
            user_type = user.user_type
            return Response({
                'token': token.key,
                'user_type': user_type,
            })
        else:
            return Response(data={"msg": "You are not approved by admin"}, status=status.HTTP_403_FORBIDDEN)
        
        

class EmployeesView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
    def list(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        manager_id=request.user.username
        print(manager_id)
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)
    
    

class TeamleadView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
    def list(self,request,*args,**kwargs):
        qs=TeamLead.objects.all()
        serializer=TeamleadSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=TeamLead.objects.get(id=id)
        serializer=TeamleadSerializer(qs)
        return Response(data=serializer.data)
    
    
    
class TeamsView(ViewSet):    
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    
    def list(self,request,*args,**kwargs):
        qs=Teams.objects.all()
        serializer=TeamsSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Teams.objects.get(id=id)
        serializer=TeamsSerializer(qs)
        return Response(data=serializer.data)
    
    
    @action(detail=True, methods=["post"])
    def team_approval(self, request, *args, **kwargs):
        team_id = kwargs.get("pk")
        team_obj = Teams.objects.get(id=team_id)
        team_obj.is_approved = True
        team_obj.save()
        serializer = TeamsSerializer(team_obj)
        return Response(serializer.data)
    
    

class ProjectView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request,*args,**kwargs):
        qs=Projects.objects.all()
        serializer=ProjectSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Projects.objects.get(id=id)
        serializer=ProjectSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance =Projects.objects.get(id=id)
            instance.delete()
            return Response({"msg": "Projects removed"})
        except Employee.DoesNotExist:
            return Response({"msg": "Projects not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
    @action(detail=True, methods=["post"])
    def create_updates(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Projects.objects.get(id=id)
        serializer=ProjectUpdatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project=qs)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
class ProjectUpdatesView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
       
       
    def list(self,request,*args,**kwargs):
        qs=ProjectUpdates.objects.all()
        serializer=ProjectUpdatesSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=ProjectUpdates.objects.get(id=id)
        serializer=ProjectUpdatesSerializer(qs)
        return Response(data=serializer.data)
    
    
    
class ProjectAssignView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=Project_assign.objects.all()
        serializer=ProjectAssignSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Project_assign.objects.get(id=id)
        serializer=ProjectAssignSerializer(qs)
        return Response(data=serializer.data)
    
    
    
class ProjectDetailView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=ProjectDetail.objects.all()
        serializer=ProjectDetailSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=ProjectDetail.objects.get(id=id)
        serializer=ProjectDetailSerializer(qs)
        return Response(data=serializer.data)
    
    
    
class TaskChartView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=TaskChart.objects.all()
        serializer=TaskChartSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    
    
    def retrieve(self, request, *args, **kwargs):
        try:
            task_chart = TaskChart.objects.prefetch_related('taskupdatechart_set').get(id=kwargs.get("pk"))
        except TaskChart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskChartSerializer(task_chart)
        data = serializer.data
        task_updates_chart_list = task_chart.taskupdatechart_set.all()
        task_updates_chart_serializer = TaskUpdatesChartSerializer(task_updates_chart_list, many=True)
        data['task_updates_chart_list'] = task_updates_chart_serializer.data
        return Response(data)
    
    
    
class PerformancelistView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=Performance_assign.objects.all()
        serializer=PerformanceTrackViewSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance =Performance_assign.objects.get(id=id)
            instance.delete()
            return Response({"msg": "performance removed"})
        except Employee.DoesNotExist:
            return Response({"msg": "performance not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
            
class MeetingView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=MeetingSerializer(data=request.data)
        user_id=request.user.username
        if serializer.is_valid():
            serializer.save(organizer=user_id)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request,*args,**kwargs):
        qs=Meeting.objects.all()
        serializer=MeetingListSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Meeting.objects.get(id=id)
        serializer=MeetingListSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance =Meeting.objects.get(id=id)
            instance.delete()
            return Response({"msg": "Meeting removed"})
        except Employee.DoesNotExist:
            return Response({"msg": "Meeting not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
   
class profileView(APIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        Manager_id=request.user.id
        qs=Manager.objects.get(id=Manager_id)
        serializer=RegistrationSerializer(qs)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs): 
        Manager_id = request.user.id
        try:
            Manager = Manager.objects.get(id=Manager_id)
        except Manager.DoesNotExist:
            return Response({"error": "Manager does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileEditSerializer(instance=Manager, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
