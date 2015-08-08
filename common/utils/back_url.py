'''
Created on Aug 23, 2013

@author: antipro
'''
from django.utils.http import is_safe_url
from django.shortcuts import resolve_url
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse


def is_url_can_not_go_back(request, url):
    return url == reverse('accounts:logout') or not is_safe_url(url=url, host=request.get_host())


def get_go_back_url(request, redirect_fieldname=REDIRECT_FIELD_NAME, default='/'):
    redirect_to = request.REQUEST.get(redirect_fieldname)
    if is_url_can_not_go_back(request, redirect_to):
        redirect_to = request.META.get('HTTP_REFERER')
        if is_url_can_not_go_back(request, redirect_to):
            redirect_to = resolve_url(default) if default else None
    return redirect_to
