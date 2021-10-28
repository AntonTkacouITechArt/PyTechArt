# Department
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from Fins.models import Department


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department/department_new.html'
    fields = ['sphere', 'staff_amount', 'shop']


class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'department/department_update.html'
    fields = ['sphere', 'staff_amount', 'shop']


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department/department_delete.html'
    fields = ['sphere', 'staff_amount', 'shop']
    context_object_name = 'department'
