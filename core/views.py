
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import admin
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
@login_required
def inicio(request):
    return render(request, 'core/inicio.html')
