from account.forms import LoginUsernameForm
from django.conf import settings

def googleanalytics(request):
    return {
        'google_tracking_id' : settings.GOOGLE_TRACKING_ID,
    }

def add_login_form(request):
	return {
		'login_form': LoginUsernameForm(),
	}