from django.urls import path
from managerapi import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("employee",views.EmployeesView,basename="employee")
router.register("teamlead",views.TeamleadView,basename="teamlead")
router.register("teams",views.TeamsView,basename="teams")
router.register("projects",views.ProjectView,basename="project-add")
router.register("assignedprojects",views.ProjectAssignView,basename="assignedprojects")
router.register("projectdetail",views.ProjectDetailView,basename="projectdetail")
router.register("taskchart",views.TaskChartView,basename="taskchart")
router.register("Performance",views.PerformancelistView,basename="Performance")
router.register("projectupdates",views.ProjectUpdatesView,basename="project-updates")
router.register("meeting",views.MeetingView,basename="meeting")






urlpatterns = [
    path("register/",views.ManagerCreateView.as_view(),name="signup"),
    path("empcreate/",views.EmployeeCreateView.as_view(),name="empsignup"),
    path('token/',views.CustomAuthToken.as_view(), name='token'),
    path("profile/",views.profileView.as_view(),name="profile"),

] +router.urls
