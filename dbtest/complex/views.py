from django.views.generic.base import TemplateView

from .models import Series

# from django.views.generic import ListView, DetailView, FormView
# from django.urls import reverse_lazy
# from django.contrib import messages

# from .forms import ContactForm


class ComplexMixin:
    model = Series

    def get_context_data(self, **kwargs):
        """
        get_context_data ctxコンテンツの

        urlから、トップ階層の各htmlページの名前を特定する仕組みを追加
        また、サイト全体で共通の定数定義をテンプレートへ渡す

        Returns
        ------
        dict
            ctx
        """
        ctx = super().get_context_data(**kwargs)
        # ctx["site"] = site
        # print("%%gcd_9", kwargs.keys(), ctx.keys(), dir(ctx["view"]))
        return ctx


class PageView(ComplexMixin, TemplateView):
    template_name = "index.html"


class IndexView(ComplexMixin, TemplateView):
    template_name = "index.html"
    context_object_name = "orderby_records"
    queryset = Series.objects
    paginate_by = 1
