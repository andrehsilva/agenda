from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

class tenantListView(ListView):
    model = Tenant