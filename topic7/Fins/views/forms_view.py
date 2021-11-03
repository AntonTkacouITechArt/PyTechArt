from django.shortcuts import render
from django.views.generic import FormView

from Fins.models import Department
from Fins.forms import CompareForm


class CompareFormView(FormView):
    def get(self, request, *args, **kwargs):
#         print(kwargs.get('shop_pk'))
        department = Department.objects.filter(
            shop__exact=kwargs.get('shop_pk')).all()
        data = [dep.id for dep in department]
        print(data)
        print(department)
        form = CompareForm()
        form['department_1'].__choices = department
        return render(request, 'forms/forms.html', {'form': form})
#
    # def post(self, request, *args, **kwargs):
    #     department1 = Department.objects.get(
    #         id=kwargs.get('select_department_1')
    #     )
    #     department2 = Department.objects.get(
    #         id=kwargs.get('select_department_2')
    #     )
    #
    #     context = {}
    #     if request.POST.get('staff_amount') == 'on':
    #         context.update(
    #             {
    #                 'staff_amount1': department1.staff_amount,
    #                 'staff_amount2': department2.staff_amount,
    #             }
    #         )
    #     if request.POST.get('total_sold_goods') == 'on':
    #         pass
    #     # context =
