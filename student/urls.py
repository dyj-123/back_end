from django.urls import path

from student import personal_info,sign_in_out,select_course,stu_grade,password,classtable

urlpatterns = [
    path('PersonalInformation/', personal_info.list_info),
    path('student/sign/', sign_in_out.signin),
    path('student/select_course/', select_course.dispatcher),
    path('student/list_grade/', stu_grade.listgrade),
    path('student/list_grade/tendance',stu_grade.gradeTend),
    path('student/password/alter', password.alterpassword),
    path('student/password/verify', password.verify),
    path('student/password/', password.alterpassword),
    path('student/classtable/', classtable.classtable),
]