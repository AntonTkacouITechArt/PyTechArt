from django.db.models import Count, Q, Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, UpdateView, \
    DeleteView, CreateView

from testappdjango.models import Student, Teacher, Mark


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        return render(request, 'index.html',
                      {
                          'students': students,
                          'teachers': teachers,
                      },
                      )


class StudentDetailView(DetailView):
    model = Student

    def get(self, request, *args, **kwargs):
        return render(request, 'student_detail.html', context={
            'student': Student.objects.get(pk=kwargs['pk']),
            'marks': Mark.objects.raw(
                f"""
                SELECT
                "testappdjango_mark".id,
                "testappdjango_mark".date as date,
                "testappdjango_teacher".name as name ,
                "testappdjango_teacher".surname as surname,
                "testappdjango_mark".mark as mark
                FROM "testappdjango_mark"
                INNER JOIN "testappdjango_student" ON "testappdjango_student".id = "testappdjango_mark".student_id
                INNER JOIN "testappdjango_teacher" ON "testappdjango_teacher".id = "testappdjango_mark".teacher_id
                WHERE "testappdjango_mark".student_id = {kwargs['pk']};
                """
            ),
            'mark_count': Mark.objects.filter(
                student_id__exact=kwargs['pk']
            ).count()
            ,
            'avg_mark': Mark.objects.filter(
                student_id__exact=kwargs['pk'],
            ).aggregate(Avg('mark'))
        })


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_create.html'
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        new_item = Student.objects.create(
            name=request.POST.get('name'),
            surname=request.POST.get('surname'),
            b_day=request.POST.get('b_day')
        ).save()
        return HttpResponseRedirect('/index')


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_update.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('index')


class TeacherDetailView(DetailView):
    model = Teacher

    def get(self, request, *args, **kwargs):
        return render(request, 'teacher_detail.html',
                      context={
                        'teacher': Teacher.objects.get(pk=kwargs['pk']),
                        'marks': Mark.objects.raw(
                            f"""
                            SELECT
                            "testappdjango_mark".id,
                            "testappdjango_mark".date as date,
                            "testappdjango_student".name as name ,
                            "testappdjango_student".surname as surname,
                            "testappdjango_mark".mark as mark
                            FROM "testappdjango_mark"
                            INNER JOIN "testappdjango_student" ON "testappdjango_student".id = "testappdjango_mark".student_id
                            INNER JOIN "testappdjango_teacher" ON "testappdjango_teacher".id = "testappdjango_mark".teacher_id
                            WHERE "testappdjango_mark".teacher_id = {kwargs['pk']};
                            """
                        ),
                          'mark_count': Mark.objects.filter(
                              teacher_id__exact=kwargs['pk']
                          ).count()
                          ,
                          'avg_mark': Mark.objects.filter(
                              teacher_id__exact=kwargs['pk'],
                          ).aggregate(Avg('mark'))
                      }
      )


class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teacher_update.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'teacher_delete.html'
    success_url = reverse_lazy('index')


class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teacher_create.html'
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        new_item = Teacher.objects.create(
            name=request.POST.get('name'),
            surname=request.POST.get('surname'),
            rank=request.POST.get('rank')
        ).save()
        return HttpResponseRedirect('/index')


class MarksMoreThan20(TemplateView):
    template_name = 'marksmorethan.html'
