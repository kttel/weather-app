from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from decouple import config

import requests


class WeatherView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(WeatherView, self).get_context_data(**kwargs)
        city = self.request.GET.get('city', '')
        if city:
            api = config('API_KEY')
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
            data = requests.get(url).json()
            if data.get('message', None) is None:
                context['data'] = data
            else:
                messages.error(self.request, "Incorrect city!")
        return context