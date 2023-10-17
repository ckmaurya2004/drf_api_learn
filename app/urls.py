from  . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter 
from rest_framework.routers import DefaultRouter 
from .views import CourseListView,InsctructureListView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'courses',CourseListView,basename="courses")
router.register(r'insctructure',InsctructureListView,basename="insctructure")



urlpatterns = [
  
     path('courses/<int:pk>',views.CourseDetailView.as_view(), name= "course_deatal"),
    path('', include(router.urls)),
    path(' ',obtain_auth_token, name= "create-token")

]
