from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Region, Image, Ad, Bookmark
from .forms import AdFormSet, ImageForm, FilterFormSet, SignupForm
from django.views.generic import ListView, DetailView, View, FormView, CreateView, UpdateView
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def index(request):
    six_categories = [i.category_set.first().category_set.first() for i in Category.objects.filter(parent_category=None).order_by('id')[: 8]]
    data = {
        'classifier': Category.objects.filter(parent_category=None).order_by('id'),
        'six_categories': six_categories,
        # 'count_my_products': Ad.objects.filter(user=request.user).count()
    }
    print(request.user)
    return render(request, 'flea_market/index.html', context=data)


class SearchList(ListView):
    def get(self, request, *args, **kwagrs):
        search = self.request.GET['title']
        return JsonResponse({
            'html': render_to_string('flea_market/search_list.html', {'search_list': Ad.objects.filter(title__icontains=search)[:10]}),
        })


class BaseProductsView(ListView):
    paginate_by = 2
    extra_context = {
        'classifier': Category.objects.filter(parent_category=None).order_by('id'),
        'form': FilterFormSet,
    }

    def get_queryset(self):
        q = Q(is_active=True)
        for key in self.request.GET:
            print(f'{key}: {self.request.GET[key]}')
            if key == 'price_from':
                q &= Q(price__gte=int(self.request.GET[key]))
            elif key == 'price_to':
                q &= Q(price__lte=int(self.request.GET[key]))
            elif key == 'type_ad':
                q &= Q(type_ad__in=self.request.GET.getlist(key))
            elif key == 'bargain':
                q &= Q(bargain=True)
            elif key == 'city':
                try:
                    self.city = Region.objects.get(title=self.request.GET[key].capitalize())
                    q &= Q(city=self.city)
                except:
                    print('City name not correct')
        self.queryset = Ad.objects.filter(q)
        if self.request.GET.get('order'):
            order_key, order_value = self.request.GET['order'].split(':')
            self.queryset = self.queryset.order_by(('' if order_value == 'desc' else '-') + order_key)
        else:
            self.queryset = self.queryset.order_by('-date_creation')
        return self.queryset

    def get(self, request, *args, **kwagrs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        print(self.object_list)
        self.paginator = Paginator(self.object_list, self.paginate_by)
        self.num_page = self.request.GET.get('page')
        self.page_obj = self.paginator.get_page(self.num_page)

        html = render_to_string('flea_market/products_list.html', {'page_obj': self.page_obj}, self.request)
        context['html'] = html
        print(self.request.GET)
        if self.request.is_ajax():
            print('Ajax')
            return JsonResponse({'html': html})
        else:
            print('Not Ajax')
            context['object_list'] = self.page_obj
            if self.request.user.is_authenticated:
                context['count_my_products'] = Ad.objects.filter(user=self.request.user).count()
            return self.render_to_response(context)

class ProductsList(BaseProductsView):
    def get_queryset(self):
        return (super().get_queryset()).filter(category=get_object_or_404(Category, id=self.kwargs['id']))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = Category.objects.get(id=self.kwargs['id'])
        return context

class Product(DetailView):
    model = Ad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classifier'] = Category.objects.filter(parent_category=None).order_by('id')
        return context


class CurrentUserProductsView(LoginRequiredMixin, BaseProductsView):
    def get_queryset(self):
        return (super().get_queryset()).filter(user=self.request.user)


class OtherUserProductsView(BaseProductsView):
    def get_queryset(self):
        return (super().get_queryset()).filter(user=get_object_or_404(User, id=self.kwargs['id']))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['owner_products'] = get_object_or_404(User, id=self.kwargs['id']) #todo ask Sasha it is normal?
        return context


class BookmarksView(LoginRequiredMixin, ListView):
    paginate_by = 2
    extra_context = {
        'classifier': Category.objects.filter(parent_category=None).order_by('id'),
    }

    def get_queryset(self):
        self.queryset = Bookmark.objects.filter(user=self.request.user)
        print(self.queryset)
        return self.queryset


class CreateMixin:


class BookmarkCreateView(LoginRequiredMixin, DetailView):
    model = Bookmark

    def post(self, request, *args, **kwargs):
        print(request)
        print(args)
        print(kwargs)

        return super().post(request, *args, **kwargs)


def ads_participate(request):
    pass


class AddProductView(LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdFormSet
    success_url = reverse_lazy('flea_market:my_products')# todo redirect to user ads
    extra_context = {
        'image_form': ImageForm,
        'categories': [i for i in Category.objects.exclude(parent_category=None) if i.category_set.count() != 0],
    }

    def form_valid(self, form):
        new_product = form.save(commit=False)
        new_product.category = Category.objects.get(id=self.request.POST['category'])
        new_product.city = Region.objects.get(title=self.request.POST['city'])
        new_product.user = self.request.user
        new_product.save()
        for i in range(len(self.request.FILES.getlist('photo'))):
            instance = Image(photo=self.request.FILES.getlist('photo')[i], order_display=i, ad=new_product)
            instance.save()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            search_city = [i.title + ', ' + i.parent_region.title for i in
                           Region.objects.exclude(parent_region=None).filter(title__istartswith=request.GET['city'])]
            return JsonResponse(search_city, safe=False)
        return super().get(request, *args, **kwargs)


class SignupView(CreateView):
    model = User
    form_class = SignupForm
    redirect_authenticated_user = True
    success_url = reverse_lazy(viewname='flea_market:login')

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.success_url
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.META['QUERY_STRING']:
            self.success_url += '?' + self.request.META['QUERY_STRING']
        return super().form_valid(form)


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'email']
    success_url = reverse_lazy('flea_market:profile')

    def get_queryset(self):
        self.kwargs['pk'] = self.request.user.id
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        context['password_change_form'] = PasswordChangeForm(user=self.request.user)
        return context