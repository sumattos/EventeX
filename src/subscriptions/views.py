# -*-coding: utf-8 -*-

from django.core.urlresolvers   import reverse
from django.shortcuts           import render, render_to_response, get_object_or_404
from django.template            import RequestContext
from forms                      import SubscriptionForms
from django.core.mail           import send_mail
from django.conf                import settings
from django.http                import HttpResponseRedirect


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    form = SubscriptionForms()
    context = RequestContext(request, {'form': form})
    return render_to_response('subscriptions/new.html', context)

def create(request):
    form = SubscriptionForms(request.POST)

    if not form.is_valid():
        context = RequestContext(request, {'form':form})
        return render_to_response('subscriptions/new.html', context)

    subscription = form.save()

    send_mail(subject = u'Cadastrado com Sucesso!!!',
              message = u'Obrigado pela sua mensagem ',
              from_email = settings.DEFAULT_FROM_EMAIL,
              recipient_list = [subscription.email])

    return render_to_response('subscriptions/success.html')

    #return HttpResponseRedirect(
    #   reverse('subscriptions:success', args=[subscription.pk]))

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscriptions': subscriptions})
    return render_to_response('subscriptions/succes.html', context)
