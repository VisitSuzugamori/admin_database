from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Series

# from django.urls import reverse_lazy
# from django.contrib import messages


class PageView(TemplateView):
    template_name = "index.html"
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

        ctx = super().get_context_data(**kwargs)  # type: ignore
        # ctx["site"] = site
        # print("%%gcd_9", kwargs.keys(), ctx.keys(), dir(ctx["view"]))
        return ctx


class IndexView(ListView):
    template_name = "index.html"
    model = Series
    context_object_name = "orderby_records"
    queryset = Series.objects.all()
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        get_context_data ctxコンテンツの

        Returns
        ------
        dict
            ctx
        """
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        return ctx
