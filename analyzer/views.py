from django.shortcuts import render,get_object_or_404
from .models import LogEntry,Alert
from django.db.models import Count
def index(request):
    latest=LogEntry.objects.order_by('-created_at')[:50]
    alerts=Alert.objects.order_by('-created_at')[:20]
    stats={'total':LogEntry.objects.count(),
           'denies':LogEntry.objects.filter(action='DENY').count(),
           'allows':LogEntry.objects.filter(action='ALLOW').count(),
           'top_blocked':LogEntry.objects.filter(action='DENY').values('src_ip').annotate(c=Count('id')).order_by('-c')[:10]}
    return render(request,'analyzer/index.html',{'latest':latest,'alerts':alerts,'stats':stats})
def detail(request,pk):
    entry=get_object_or_404(LogEntry,pk=pk)
    return render(request,'analyzer/detail.html',{'entry':entry})
