from django.shortcuts import render
from lab_5_app.models import IceCreamType
from lab_5_app.models import IceCream

def GetIcecreams(request):
    return render(request, 'icecreamType.html', {'data': {
        'icecreams': IceCreamType.objects.all()
    }})

def GetIcecreamInfo(request):
    return render(request, 'icecream.html', {'data': {
        'icecream_info': IceCream.objects.all()
    }})

def GetIcecreamType(request, pk):
    it = IceCreamType.objects.get(pk=pk)
    context = {
                  'pk': it.pk,
                  'title': it.title,
                  }
    return render(request, 'icecreamType.html', context)

def GetIcecream(request, pk):
    ic = IceCream.objects.get(idtype=pk)
    context = {
                  'pk': ic.pk,
                  'title': ic.title,
                  'ingridients': ic.ingridients,
                  'standart': ic.standart,
                  'price': ic.price,
                  }
    return render(request, 'icecream.html', context)

