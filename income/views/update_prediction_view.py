from django.contrib import messages
from django.core.management import call_command
from django.shortcuts import redirect
from django.views.generic.base import View


class UpdatePredictionView(View):

    def get(self, request, *args, **kwargs):
        call_command('calculate_income_prediction', uid=kwargs.get('pk'))
        messages.success(request, message='Successfully update prediction')
        return redirect('income:index')
