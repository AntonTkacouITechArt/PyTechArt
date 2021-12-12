from django.db.models import Count, Q
from django.shortcuts import redirect
from django.urls import reverse_lazy

from testappdjango.models import Mark


class MarksMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        mark = Mark.objects.aggregate(
            cnt=Count(
                'id',
            )
        )
        if 'admin' not in request.path and mark.get('cnt') > 20 and 'overloaded' not in request.path:
            return redirect(reverse_lazy('MarksMoreThan20'))
        response = self._get_response(request)
        return response