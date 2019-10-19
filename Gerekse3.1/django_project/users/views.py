from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.views.generic import (
    DetailView,
)

def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data.get('email')
            email = form.cleaned_data.get('email')
            if email:
                if User.objects.filter(email=email).exists():
                    return HttpResponse("Bu Mail Zaten Kayıtlı")
                    return email
                kontrol=""
                for i in reversed(to_email):
                    kontrol += i
                if kontrol[:11]=="rt.ude.utem":
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Hesabınız Oluşturuldu, Giriş Yapabilirsiniz')
                    user = form.save(commit=False)
                    user.is_active = False
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Hesabınızı Onaylayın'
                    message = render_to_string('users/acc_active_email.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                            'token':account_activation_token.make_token(user),
                            })
    
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    return render(request, 'users/kayit_basarili.html')
                else:
                    return render(request, 'users/kayit_basarisiz.html')
                
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('blog-new')
    else:
        return HttpResponse('Aktivasyon Kodu Geçersiz')


@login_required
def profile(request,*args, **kwargs):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
          u_form.save()  
          p_form.save()
          messages.success(request, f'Hesabınız Güncellendi')
          return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)       
    
    context = {
            'u_form': u_form,
            'p_form': p_form
            }
    
    return render(request, 'users/profile.html', context)

class ProfileDetailView(DetailView):
    model = User   
    template_name = "users/user_detail.html"  