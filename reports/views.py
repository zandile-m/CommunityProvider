from django.shortcuts import render
from .models import Issue

def report_issue(request):
    success = False
    if request.method == 'POST':
        Issue.objects.create(
            issue_type=request.POST['issue_type'],
            location=request.POST['location'],
            description=request.POST['description'],
            name=request.POST.get('name', ''),
        )
        success = True
    return render(request, 'reports/report_issue.html', {'success': success})