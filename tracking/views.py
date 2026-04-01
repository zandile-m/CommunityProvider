from django.shortcuts import render
from reports.models import Issue

def track_issues(request):
    filter_type = request.GET.get('filter', 'All')
    if filter_type == 'All':
        issues = Issue.objects.all().order_by('-date_reported')
    else:
        issues = Issue.objects.filter(issue_type=filter_type).order_by('-date_reported')
    
    pending_count = Issue.objects.filter(status='Pending').count()
    resolved_count = Issue.objects.filter(status='Resolved').count()
    
    return render(request, 'tracking/track_issues.html', {
        'issues': issues,
        'pending_count': pending_count,
        'resolved_count': resolved_count,
        'filter_type': filter_type,
    })