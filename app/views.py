from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
from app.models import Address

#공식 !! 리스트에
def list(request):
    address = Address.objects.all()
    return HttpResponse(address)


def index(request):
    address = ''
    try:
        address = request.GET['address']

        #디비에 삽입
        add = Address(address=address)
        add.save()
    except MultiValueDictKeyError:
        pass
    return HttpResponse(
    '{"Hello":"'+address+'"}')