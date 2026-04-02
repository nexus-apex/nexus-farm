import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Crop, FarmField, Harvest


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['crop_count'] = Crop.objects.count()
    ctx['crop_planted'] = Crop.objects.filter(status='planted').count()
    ctx['crop_growing'] = Crop.objects.filter(status='growing').count()
    ctx['crop_ready'] = Crop.objects.filter(status='ready').count()
    ctx['crop_total_area_acres'] = Crop.objects.aggregate(t=Sum('area_acres'))['t'] or 0
    ctx['farmfield_count'] = FarmField.objects.count()
    ctx['farmfield_clay'] = FarmField.objects.filter(soil_type='clay').count()
    ctx['farmfield_sandy'] = FarmField.objects.filter(soil_type='sandy').count()
    ctx['farmfield_loam'] = FarmField.objects.filter(soil_type='loam').count()
    ctx['farmfield_total_area_acres'] = FarmField.objects.aggregate(t=Sum('area_acres'))['t'] or 0
    ctx['harvest_count'] = Harvest.objects.count()
    ctx['harvest_a'] = Harvest.objects.filter(quality_grade='a').count()
    ctx['harvest_b'] = Harvest.objects.filter(quality_grade='b').count()
    ctx['harvest_c'] = Harvest.objects.filter(quality_grade='c').count()
    ctx['harvest_total_quantity_kg'] = Harvest.objects.aggregate(t=Sum('quantity_kg'))['t'] or 0
    ctx['recent'] = Crop.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def crop_list(request):
    qs = Crop.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'crop_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def crop_create(request):
    if request.method == 'POST':
        obj = Crop()
        obj.name = request.POST.get('name', '')
        obj.variety = request.POST.get('variety', '')
        obj.field_name = request.POST.get('field_name', '')
        obj.area_acres = request.POST.get('area_acres') or 0
        obj.planted_date = request.POST.get('planted_date') or None
        obj.expected_harvest = request.POST.get('expected_harvest') or None
        obj.status = request.POST.get('status', '')
        obj.estimated_yield = request.POST.get('estimated_yield') or 0
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/crops/')
    return render(request, 'crop_form.html', {'editing': False})


@login_required
def crop_edit(request, pk):
    obj = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.variety = request.POST.get('variety', '')
        obj.field_name = request.POST.get('field_name', '')
        obj.area_acres = request.POST.get('area_acres') or 0
        obj.planted_date = request.POST.get('planted_date') or None
        obj.expected_harvest = request.POST.get('expected_harvest') or None
        obj.status = request.POST.get('status', '')
        obj.estimated_yield = request.POST.get('estimated_yield') or 0
        obj.notes = request.POST.get('notes', '')
        obj.save()
        return redirect('/crops/')
    return render(request, 'crop_form.html', {'record': obj, 'editing': True})


@login_required
def crop_delete(request, pk):
    obj = get_object_or_404(Crop, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/crops/')


@login_required
def farmfield_list(request):
    qs = FarmField.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(soil_type=status_filter)
    return render(request, 'farmfield_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def farmfield_create(request):
    if request.method == 'POST':
        obj = FarmField()
        obj.name = request.POST.get('name', '')
        obj.location = request.POST.get('location', '')
        obj.area_acres = request.POST.get('area_acres') or 0
        obj.soil_type = request.POST.get('soil_type', '')
        obj.irrigation = request.POST.get('irrigation', '')
        obj.status = request.POST.get('status', '')
        obj.current_crop = request.POST.get('current_crop', '')
        obj.save()
        return redirect('/farmfields/')
    return render(request, 'farmfield_form.html', {'editing': False})


@login_required
def farmfield_edit(request, pk):
    obj = get_object_or_404(FarmField, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.location = request.POST.get('location', '')
        obj.area_acres = request.POST.get('area_acres') or 0
        obj.soil_type = request.POST.get('soil_type', '')
        obj.irrigation = request.POST.get('irrigation', '')
        obj.status = request.POST.get('status', '')
        obj.current_crop = request.POST.get('current_crop', '')
        obj.save()
        return redirect('/farmfields/')
    return render(request, 'farmfield_form.html', {'record': obj, 'editing': True})


@login_required
def farmfield_delete(request, pk):
    obj = get_object_or_404(FarmField, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/farmfields/')


@login_required
def harvest_list(request):
    qs = Harvest.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(crop_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(quality_grade=status_filter)
    return render(request, 'harvest_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def harvest_create(request):
    if request.method == 'POST':
        obj = Harvest()
        obj.crop_name = request.POST.get('crop_name', '')
        obj.field_name = request.POST.get('field_name', '')
        obj.quantity_kg = request.POST.get('quantity_kg') or 0
        obj.quality_grade = request.POST.get('quality_grade', '')
        obj.harvest_date = request.POST.get('harvest_date') or None
        obj.sold_price = request.POST.get('sold_price') or 0
        obj.buyer = request.POST.get('buyer', '')
        obj.revenue = request.POST.get('revenue') or 0
        obj.save()
        return redirect('/harvests/')
    return render(request, 'harvest_form.html', {'editing': False})


@login_required
def harvest_edit(request, pk):
    obj = get_object_or_404(Harvest, pk=pk)
    if request.method == 'POST':
        obj.crop_name = request.POST.get('crop_name', '')
        obj.field_name = request.POST.get('field_name', '')
        obj.quantity_kg = request.POST.get('quantity_kg') or 0
        obj.quality_grade = request.POST.get('quality_grade', '')
        obj.harvest_date = request.POST.get('harvest_date') or None
        obj.sold_price = request.POST.get('sold_price') or 0
        obj.buyer = request.POST.get('buyer', '')
        obj.revenue = request.POST.get('revenue') or 0
        obj.save()
        return redirect('/harvests/')
    return render(request, 'harvest_form.html', {'record': obj, 'editing': True})


@login_required
def harvest_delete(request, pk):
    obj = get_object_or_404(Harvest, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/harvests/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['crop_count'] = Crop.objects.count()
    data['farmfield_count'] = FarmField.objects.count()
    data['harvest_count'] = Harvest.objects.count()
    return JsonResponse(data)
