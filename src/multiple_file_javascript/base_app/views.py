import json
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import MultipleFieldJavascript


@method_decorator(csrf_exempt, name='dispatch')
class MultipleFieldView(View):
    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        for d in data:
            MultipleFieldJavascript.objects.get_or_create(data=d)
        response = {
            "response": "ok"
        }
        return JsonResponse(response, safe=False)

    def get(self, *args, **kwargs):
        data = MultipleFieldJavascript.objects.order_by('-id')
        return render(self.request, 'multiple_field.html', {"data": data})
