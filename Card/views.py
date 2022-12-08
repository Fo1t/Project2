from django.shortcuts import render, redirect
from Card.models import Card
from datetime import timedelta, datetime
from uuid import uuid4
from Card.forms import SearchForm, CreateCardForm


def MainPage(request):
    data = {}
    data['cards'] = Card.objects.all()
    if request.method == 'GET':
        data['form'] = SearchForm()
    else:
        form = SearchForm(request.POST)
        data['form'] = form
        if form.is_valid():
            data['search_cards'] = ''
            if form.cleaned_data['identity'] != '':
                data['card_identity'] = Card.objects.filter(identity__icontains=form.cleaned_data['identity'])
            if form.cleaned_data['status'] != '':
                data['card_status'] = Card.objects.filter(status__icontains=form.cleaned_data['status'])
            if form.cleaned_data['series'] != '':
                data['card_series'] = Card.objects.filter(series__icontains=form.cleaned_data['series'])
            if form.cleaned_data['date_of_issue'] is not None:
                data['card_date_of_issue'] = Card.objects.filter(date_of_issue__icontains=form.cleaned_data['date_of_issue'])
            if form.cleaned_data['valid_thru'] is not None:
                data['card_valid_thru'] = Card.objects.filter(valid_thru__icontains=form.cleaned_data['valid_thru'])
    return render(request, 'index.html', data)


def tools(request, identity, key):
    if key == 'delete':
        Card.objects.filter(identity=identity).delete()
    elif key == 'activate':
        card = Card.objects.filter(identity=identity)[0]
        card.status='а'
        card.save()
    elif key == 'deactivate':
        card = Card.objects.filter(identity=identity)[0]
        card.status='н'
        card.save()
    return redirect('/')

def CreatePage(request):
    data = {'error_msg': ''}
    print(f'{request.method=}')
    if request.method == 'GET':
        data['form'] = CreateCardForm()
    else:
        print(f'{request.POST=}')
        form = CreateCardForm(request.POST)
        if form.is_valid():
            delta = {
                '1': timedelta(days=30),
                '6': timedelta(days=180),
                '12': timedelta(days=365),
            }            
            print(f'{form.cleaned_data=}')
            for card in range(form.cleaned_data['count']):
                Card(
                    identity=uuid4(),
                    status='н',
                    series=form.cleaned_data['series'],
                    date_of_issue=datetime.now(),
                    valid_thru=datetime.now() + delta[form.cleaned_data['valid_thru']]
                ).save()
            return redirect('/')
        else:
            print(f'{form.errors=}')
            data['error_msg'] = form.errors
    return render(request, 'create.html', data)
    