from django.shortcuts import render
from django.views.generic import TemplateView

import requests


class WeatherView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(WeatherView, self).get_context_data(**kwargs)
        city = self.request.GET.get('city', '')
        if city:
            api = 'ce9fa1660581155ce7a423dc1e357c45'
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
            data = requests.get(url).json()
            context['data'] = data
        return context