from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login, get_user_model
from account.forms import UserForm
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.hashers import check_password


# SMTP 관련 인증
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token


# Create your views here.
def account_main(request):
    return render(request, "account/index.html")

def logout_view(request):
    logout(request)
    return redirect('/')


def signup(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 비밀번호 확인도 같다면
        if request.POST['nickname'] is not None:
            if request.POST['password1'] == request.POST['password2']:

                
                # 유저 만들기
                user = User.objects.create_user(
                                    username=request.POST['username'],
                                    password=request.POST['password1'],
                                    email=request.POST['email'],
                                    first_name=request.POST['nickname'])
                user.is_active = False # 유저 비활성화
                user.save()


                current_site = get_current_site(request) 
                message = render_to_string('account/activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })

                mail_title = "계정 활성화 확인 이메일"
                mail_to = request.POST["email"]
                email = EmailMessage(mail_title, message, to=[mail_to])
                email.send()
                return redirect("account:signup_done")

    # 포스트 방식 아니면 페이지 띄우기
    return render(request, 'account/signup.html')



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExsit):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("/")
    else:
        return render(request, 'base.html', {'error' : '계정 활성화 오류'})
    return 


def signup_done(request):
    return render(request, 'account/signup_succfully.html')


# def change_password(request):
#   if request.method == "POST":
#     user = request.user
#     origin_password = request.POST["origin_password"]
#     if check_password(origin_password, user.password):
#       new_password = request.POST["new_password"]
#       confirm_password = request.POST["confirm_password"]
#       if new_password == confirm_password:
#         user.set_password(new_password)
#         user.save()
#         auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#         return redirect('profile')
#       else:
#         messages.error(request, 'Password not same')
#     else:
#       messages.error(request, 'Password not correct')
#     return render(request, 'change_password.html')
#   else:
#     return render(request, 'change_password.html')
  

# def detail(request, pk):
#     User = get_user_model()
#     user = get_object_or_404(User, pk=pk)
#     context = {
#         'user': user
#     }
#     return render(request, 'account/accounts.html', context)