from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from custom.models import SiteSetting, EmailVerificationToken
from custom.forms import SiteSettingForm
from django.contrib import messages
from allauth.account.forms import LoginForm
from django.utils import timezone
from datetime import timedelta
from custom.emails import send_verification_email
from django.contrib.auth import login
from django.http import JsonResponse
User = get_user_model()

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "home.html"


class UserProfileView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.UpdateView
):
    model = User
    fields = [
        'first_name', 'last_name', 'email', 'phone_number',
        'image', 'gender', 
    ]
    success_message = "Profile Has been Updated!"
    success_url = reverse_lazy("home")
    template_name = "account/profile.html"

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)
    

class SiteSettingView(
    LoginRequiredMixin,
    generic.View):
    

    def get(self, request, *args, **kwargs):
        
        if not request.user.is_superuser:
            messages.error(request, 'Only Super user can access this page')
            return redirect('/')
        
        context = {
            'instance': SiteSetting.objects.last(),
        }
        return render(request, "site_setting.html", context)
    
    def post(self, request, *args, **kwargs):
        instance = SiteSetting.objects.last()
        if instance:
            form = SiteSettingForm(request.POST, request.FILES, instance=instance)
        else:
            form = SiteSettingForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Site setting has been updated")
        else:
            messages.error(request, 'Please correct the error below.')

        return redirect('/site-setting/')

class CustomLoginView(generic.View):

    def get(self, request, *args, **kwargss):
        form = LoginForm()
        return render(request, "account/login.html", {'form': form})
    

    def post(self, request, *args, **kwargss):
        try:
            email = request.POST.get('login')
            password = request.POST.get('password')
            user = User.objects.filter(email=email).last()
            
            if user is not None:
                if user.check_password(password):
                    if user.is_active:
                        send_verification_email(user)
                        messages.info(request, f'Confirmation e-mail sent to {email}')
                        return redirect('/')
                    else:
                        messages.error(request, "User not activated")
                else:
                    messages.error(request, "Password is incorrect")
            else:
                messages.error(request, 'User with this email not exist')

            return redirect('.')
        except Exception as e:
            messages.error(request, str(e))
        return redirect('.')


class VerifyLoginEmailView(
    generic.View
):
    def get(self, request, *args, **kwargss):
        token = request.GET.get('token')
        try:
            token_obj = EmailVerificationToken.objects.get(token=token, is_used=False)
            # Optional: check if the token is expired (e.g., 1 hour)
            if timezone.now() > token_obj.created_at + timedelta(hours=1):
                messages.error(request, f'Token expired')
                return redirect('/login')
            
            user = token_obj.user
            user.backend = 'allauth.account.auth_backends.AuthenticationBackend'
            login(request, user)
            token_obj.is_used = True
            token_obj.save()
            messages.success(request, f'Successfully signed in as {user.email}.')
            return redirect('/')
        except EmailVerificationToken.DoesNotExist:
            messages.error(request, f'Invalid token')
            return redirect('/login')
        

class UserTimeZoneView(
    LoginRequiredMixin,
    generic.View
):
    def post(self, request, *args, **kwargss):
        user = request.user
        time_zone = request.POST.get('time_zone', 'UTC')
        user.time_zone = time_zone
        user.save()
        return JsonResponse({'code': 1, 'msg': 'Time zone has been changed'})