from django.shortcuts import render
from django.views.generic import FormView

from Fins.models import Department
from Fins.views.forms import CompareForm


class CompareFormView(FormView):
    template_name = 'forms/forms.html'
    context_object_name = 'form'

    def get(self, request, *args, **kwargs):
        form_class = CompareForm(request, kwargs)
        return render(request, 'forms/forms.html')

    def post(self, request, *args, **kwargs):
        department1 = Department.objects.get(
            id=kwargs.get('select_department_1')
        )
        department2 = Department.objects.get(
            id=kwargs.get('select_department_2')
        )

        context = {}
        if request.POST.get('staff_amount') == 'on':
            context.update(
                {
                    'staff_amount1': department1.staff_amount,
                    'staff_amount2': department2.staff_amount,
                }
            )
        if request.POST.get('total_sold_goods') == 'on':
            pass
        # context =
