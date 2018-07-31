import osa
import os
from pprint import pprint


def get_path():
    source = "Homework"
    homework_source = os.path.abspath(source)

    return homework_source


def get_temperature():  # пункт номер 1
    list_temps = list()
    with open(os.path.join(get_path(), 'temps.txt'), encoding='utf8') as f:
        for temps in f:
            a = temps.strip().split(" F")
            b = int(a[0])
            list_temps.append(b)

    sum_temp = sum(list_temps) / len(list_temps)

    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(URL)
    response = client.service.ConvertTemp(
        Temperature=sum_temp,
        FromUnit='degreeFahrenheit',
        ToUnit='degreeCelsius')

    print("Средняя температура за неделю - {}".format(round(response, 2)))


def get_trace():  # пункт номер 2
    trace = dict()
    with open(os.path.join(get_path(), 'currencies.txt'), encoding='utf8') as f:
        for enum, temps in enumerate(f):
            trace_values = temps.strip().split(" ")
            trace_value = {"flyght": trace_values[0], "cost": trace_values[1], "currency": trace_values[2]}
            trace.update({enum: trace_value})

    URL = "http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL"
    client = osa.client.Client(URL)

    for values in trace.values():
        response = client.service.ConvertToNum(
            fromCurrency=values['currency'],
            toCurrency='RUB',
            amount=values['cost'],
            rounding=False)
        print("Полёт {} будет стоить {} рублей".format(values["flyght"], round(response, 0)))


def length_of_path():  # пункт номер 3
    trace = dict()
    with open(os.path.join(get_path(), 'travel.txt'), encoding='utf8') as f:
        for enum, temps in enumerate(f):
            trace_values = temps.strip().split(" ")
            length_value = trace_values[1].replace(",", "")
            trace_value = {"path": trace_values[0], "length": float(length_value)}
            trace.update({enum: trace_value})
            # int(float(trace_values[1]))
    # pprint(trace)
    URL = 'http://www.webservicex.net/length.asmx?WSDL'
    client = osa.client.Client(URL)

    for values in trace.values():
        response = client.service.ChangeLengthUnit(
            LengthValue=values["length"],
            fromLengthUnit='Miles',
            toLengthUnit='Kilometers')
        # print(response)
        print("Длина пути {} будет - {} км".format(values["path"], round(response, 2)))


def main():
    question = input("Подсчет средней температуры - нажмите 1\n"
                     "Подсчет стоимости перелёта - нажмите 2\n"
                     "Подсчет длины пути в километрах - нажмите 3")
    if question == "1":
        get_temperature()
    if question == "2":
        get_trace()
    if question == "3":
        length_of_path()

main()
