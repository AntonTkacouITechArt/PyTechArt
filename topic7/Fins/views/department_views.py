# Department
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from Fins.models import Department, Shop


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department/department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'department/department_new.html'
    fields = ['sphere', 'staff_amount']

    def post(self, request, *args, **kwargs):
        new_department = Department.objects.create(
            sphere=request.POST.get('sphere'),
            staff_amount=request.POST.get('staff_amount'),
            shop=Shop.objects.get(id=kwargs.get('shop_pk'))
        ).save()
        return HttpResponseRedirect(f"/fins/index/{kwargs['shop_pk']}/")


class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'department/department_update.html'
    fields = ['sphere', 'staff_amount', 'shop']


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'department/department_delete.html'
    fields = ['sphere', 'staff_amount', 'shop']
    context_object_name = 'department'
    success_url = reverse_lazy('index')
