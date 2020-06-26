##################################################################
# This program will work only with postal codes from Romania !!! #
##################################################################

import requests


def get_weather(postal_code):
    api_key = ''  # This api_key is from https://home.openweathermap.org/api_keys
    country_code = 'RO'

    response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}'
                            .format(postal_code, country_code, api_key))

    if response.status_code != 200:
        print("The postal code is wrong, try again")
        main()
        return

    data = response.json()
    temperature = round(float(data['main']['temp']) - 273.15)

    city = data['name']
    humidity = data['main']['humidity']

    print('{}°C Humidity: {}% - City: {}'.format(temperature, humidity, city))
    main()


def main():
    print("Enter a postal code to see the weather or nothing to exit")
    postal_code = input('Please enter a postal code: ')
    if postal_code == '':
        return 0
    get_weather(postal_code)


main()