from django.shortcuts import render

def GetIcecreams(request):
    return render(request, 'master.html', {'data': {'icecreamss':
        [
            {'title': 'Пломбир', 'id': 1},
            {'title': 'Шоколадное мороженное', 'id': 2},
            {'title': 'Клубничное мороженное', 'id': 3},
        ]
    }})

def GetIcecream(request, id):
    return render(request, 'detail.html', {'data': {
        'id': id,
        'icecream_info':
            [
                {'title': 'Пломбир',
                    'ingridients': 'Сливки 33%, Молоко, Яичный желток, Сахарная пудра, Ванилин',
                    'standart': 'ГОСТ 119-41',
                    'price': '72 р.',
                    'id': 1},
                {'title': 'Шоколадное мороженное',
                    'ingridients': 'Сливки 33%, Молоко, Яичный желток, Сахарная пудра, Какао',
                    'standart': 'ГОСТ 31457-2012',
                    'price': '68 р.',
                    'id': 2},
                {'title': 'Клубничное мороженное',
                     'ingridients': 'Сливки 33%, Молоко, Яичный желток, Сахарная пудра, Клубника',
                     'standart': 'ГОСТ 31457-2012',
                     'price': '62 р.',
                     'id': 3},
            ]
    }})