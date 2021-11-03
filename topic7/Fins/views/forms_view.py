from django.shortcuts import render
from django.views.generic import FormView
from Fins.models import Department
from Fins.forms import CompareForm


class CompareFormView(FormView):
    form_class = CompareForm
    template_name = 'forms/forms.html'

    def get(self, request, *args, **kwargs):
        form = self.get_form(kwargs.get('shop_pk'))
        return render(request, 'forms/forms.html', {'form': form})

    def get_form(self, shop_pk, *args, **kwargs):
        department = Department.objects.filter(
                shop__exact=shop_pk).all()
        data = [(dep.id, dep.sphere) for dep in department]
        form = super().get_form(*args, **kwargs)
        form.fields['department_1'].choices = data
        form.fields['department_2'].choices = data
        return form

    # def get(self, request, *args, **kwargs):
    #     initial = self.get_initial(kwargs.get('shop_pk'))
    #     form = CompareForm(initial=initial)
    #     return render(request, 'forms/forms.html', {'form': form})

    #
    # def get_initial(self, shop_id):
    #     initial = super(CompareFormView, self).get_initial()
    #     department = Department.objects.filter(
    #         shop__exact=shop_id).all()
    #     data = [dep.sphere for dep in department]
    # data = [(dep.id, dep.sphere) for dep in department]
    #
    # initial['department_1'] = Department.models.query(
    #     ~Q(department_shop=1))
    # initial['department_2'] = Department.models.query(
    #     ~Q(department_shop=2))
    # print(data)
    # initial['department_1'] = data
    # initial['department_2'] = data
    # initial['total_cost_goods'] = True
    # return initial
#
