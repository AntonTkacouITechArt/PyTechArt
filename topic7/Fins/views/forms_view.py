from django.db.models import Sum, Q, Count
from django.shortcuts import render
from django.views.generic import FormView
from Fins.models import Department
from Fins.forms import CompareForm


class CompareFormView(FormView):
    form_class = CompareForm
    template_name = 'forms/forms.html'
    success_url = 'forms/form_success.html'

    def get_form(self, *args, **kwargs):
        department = Department.objects.filter(
            shop__exact=self.kwargs['shop_pk']).all()
        data = [(dep.id, dep.sphere) for dep in department]
        form = super().get_form(*args, **kwargs)
        form.fields['department_1'].choices = data
        form.fields['department_2'].choices = data
        return form

    def post(self, request, *args, **kwargs):
        if request.POST.get('department_1') == request.POST.get(
                'department_2'):
            return render(request, 'forms/form_isnotvalid.html')
        else:
            data = {}
            dep1 = Department.objects.filter(
                id__exact=request.POST.get('department_1'))
            dep2 = Department.objects.filter(
                id__exact=request.POST.get('department_2'))

            # get data if POST have value
            if request.POST.get('staff_amount'):
                data.update(
                    {'staff_amount': [
                        dep1.get(
                            id=request.POST.get('department_1')
                        ).staff_amount,
                        dep2.get(
                            id=request.POST.get('department_2')
                        ).staff_amount,
                    ]}
                )
            if request.POST.get('total_sold_goods'):
                data.update(
                    {'total_sold_goods': [
                        dep1.filter(
                            item_filter__is_sold__exact=True,
                        ).aggregate(
                            sum=Sum('item_filter__price')).get('sum'),
                        dep2.filter(
                            item_filter__is_sold__exact=True,
                        ).aggregate(
                            sum=Sum('item_filter__price')).get('sum'), ]}
                )
            if request.POST.get('total_unsold_goods'):
                data.update({'total_unsold_goods': [
                    dep1.filter(
                        item_filter__is_sold__exact=False,
                    ).aggregate(
                        sum=Sum('item_filter__price')).get('sum'),
                    dep2.filter(
                        item_filter__is_sold__exact=False,
                    ).aggregate(
                        sum=Sum('item_filter__price')
                    ).get('sum'),
                ]})
            if request.POST.get('total_cost_goods'):
                data.update(
                    {'total_cost_goods': [
                        dep1.aggregate(
                            sum=Sum('item_filter__price')).get('sum'),
                        dep2.aggregate(
                            sum=Sum('item_filter__price')).get('sum'),
                    ]}
                )
            if request.POST.get('count_sold_goods'):
                data.update(
                    {'count_sold_goods': [
                        dep1.filter(
                            item_filter__is_sold__exact=True,
                        ).aggregate(
                            cnt=Count('item_filter__id')).get('cnt'),
                        dep2.filter(
                            item_filter__is_sold__exact=True,
                        ).aggregate(
                            cnt=Count('item_filter__id')).get('cnt'),
                    ]})
            if request.POST.get('count_unsold_goods'):
                data.update(
                    {'count_unsold_goods': [
                        dep1.filter(
                            item_filter__is_sold__exact=False,
                        ).aggregate(
                            cnt=Count('item_filter__id')).get('cnt'),
                        dep2.filter(
                            item_filter__is_sold__exact=False,
                        ).aggregate(
                            cnt=Count('item_filter__id')).get('cnt'),
                    ]})
            if request.POST.get('count_goods'):
                data.update({
                    'total_goods': [
                        dep1.aggregate(
                            cnt=Count('item_filter__id')
                        ).get('cnt'),
                        dep2.aggregate(
                            cnt=Count('item_filter__id')
                        ).get('cnt')
                    ]
                })
            return render(request, 'forms/form_success.html',
                          context={
                              'data': data,
                              'department_1': dep1[0].sphere,
                              'department_2': dep2[0].sphere,
                          })

    # def get(self,  request, *args, **kwargs):
    #     form = self.get_form()
    #     return render(request, 'forms/forms.html', {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     form = CompareForm(request.POST)
    #     print(form)
    # if form.is_valid():
    #     dep1 = form.cleaned_data['department_1']
    #     print(dep1)
    #     pass
    # else:
    #     print('not valid')
    #
    # return render(request, 'forms/forms.html', {'form':1})

    # def form_valid(self):
    #     print(self)
    #     pass

    # def get(self, request, *args, **kwargs):
    #     form = self.get_form(kwargs.get('shop_pk'))
    #     return render(request, 'forms/forms.html', {'form': form})

    # def get_form(self, shop_pk, *args, **kwargs):
    #     department = Department.objects.filter(
    #             shop__exact=shop_pk).all()
    #     data = [(dep.id, dep.sphere) for dep in department]
    #     form = super().get_form(*args, **kwargs)
    #     form.fields['department_1'].choices = data
    #     form.fields['department_2'].choices = data
    #     return form

    # def get(self, request, *args, **kwargs):
    #     # form = self.get_form(kwargs.get('shop_pk'))
    #     print(request.GET)
    #     deps = Department.objects.filter(
    #         shop__exact=kwargs['shop_pk'])
    #     form = CompareForm(initial={'department_1': deps})
    #     return render(request, 'forms/forms.html', {'form': form})

    # def get(self, request, *args, **kwargs):
    #     # form = self.get_form(kwargs.get('shop_pk'))
    #     form = CompareForm()
    #     return render(request, 'forms/forms.html', {'form': form})
    #

    # def get_initial(self):
    #     print(self.__dict__)
    #     print(self.kwargs.get('shop_pk'))
    #     initial = super().get_initial()
    #     deps = Department.objects.filter(
    #         shop__exact=self.kwargs['shop_pk']).all()
    #     print(deps)
    #     data = [(dep.id, dep.sphere) for dep in deps]
    #     print(data)
    #     initial['department_1'] = deps
    #     initial['department_2'] = data
    #     initial['total_sold_goods'] = True
    #
    #     return initial

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
