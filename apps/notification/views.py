from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Notification

@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notifaction_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)

    if goto !='':
        notification = Notification.objects.get(pk=notifaction_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('view_application', application_id=notification.extra_id)
        elif notification.notification_type == Notification.APPLICATION:
            return redirect('view_application', application_id=notification.extra_id)
    
    return render(request, 'notification/notification.html')
