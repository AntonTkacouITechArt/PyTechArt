from django.urls import path

from testappdjango.views import IndexView, StudentDetailView, \
    TeacherDetailView, StudentUpdateView, TeacherUpdateView, StudentDeleteView, \
    TeacherDeleteView, StudentCreateView, TeacherCreateView, MarksMoreThan20, \
    TeacherAddMarkView, StudentAddMarkView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/update', StudentUpdateView.as_view(),
         name='student_update'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(),
         name='student_delete'),
    path('student/create', StudentCreateView.as_view(), name='student_create'),

    path('teacher/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/<int:pk>/update', TeacherUpdateView.as_view(),
         name='teacher_update'),
    path('teacher/<int:pk>/delete', TeacherDeleteView.as_view(),
         name='teacher_delete'),
    path('teacher/create', TeacherCreateView.as_view(), name='teacher_create'),

    path('overloaded', MarksMoreThan20.as_view(), name='MarksMoreThan20'),
    path('teacher/<int:pk>/add_mark', TeacherAddMarkView.as_view(), name='teacher_add_mark'),
    path('student/<int:pk>/add_mark', StudentAddMarkView.as_view(),
         name='student_add_mark'),

]