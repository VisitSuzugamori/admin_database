# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import PasswordResetCompleteView
from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    """サインアップページのビュー"""

    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("accounts:signup_success")

    def form_valid(self, form):
        """CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録を行う

        parameters:
          form(django.forms.Form):
            form_classに格納されているCustomUserCreationFormオブジェクト
        Return:
          HttpResponseRedirectオブジェクト:
            スーパークラスのform_valid()の戻り値を返すことで、
            success_urlで設定されているURLにリダイレクトさせる
        """
        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "password_reset_complete.html"
