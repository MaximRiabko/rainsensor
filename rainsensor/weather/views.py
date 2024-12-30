from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=59fc0a9d626249a1156f49224447acea').read()
        list_data = json.loads(source)

        data = {
            "country_code": str(list_data['sys']['country']),
            "city": str(list_data['name']),
            "coordinate": str(list_data['coord']['lon']) + ', '
                          + str(list_data['coord']['lat']),

            "temp": str(list_data['main']['temp']) + ' °C',
            "pressure": str(list_data['main']['pressure']),
            "humidity": str(list_data['main']['humidity']),
            'main': str(list_data['weather'][0]['main']),
            'description': str(list_data['weather'][0]['description']),
            'icon': list_data['weather'][0]['icon'],
        }

        print(data)
    else:
        data = {}

    return render(request, 'weather/index.html', data)

