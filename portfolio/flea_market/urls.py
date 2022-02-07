from django.urls import path

from .views import index, ProductsList, SearchList, Product, SignupView, Profile, AddProductView, CurrentUserProductsView,\
OtherUserProductsView, BookmarksView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy


app_name = 'flea_market'
urlpatterns = [
    path('', index, name='index'),
    path('add-product/', AddProductView.as_view(template_name='flea_market/add_product.html'), name='add_product'),
    path('product/<int:pk>/', Product.as_view(template_name='flea_market/product.html'), name='product'),
    path('products/c<int:id>/', ProductsList.as_view(template_name='flea_market/products.html'), name='products'),
    path('products/user<int:id>/', OtherUserProductsView.as_view(template_name='flea_market/other_user_products.html'),
         name='other_user_products'),
    path('search/', SearchList.as_view(), name='search'),
    path('login/', LoginView.as_view(template_name='flea_market/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(template_name='flea_market/signup.html'), name='signup'),
    path('profile/', Profile.as_view(template_name='flea_market/profile.html'), name='profile'),
    path('profile/bookmarks', BookmarksView.as_view(template_name='flea_market/bookmarks.html'), name='bookmarks'),
    path('profile/bookmark-create', BookmarksView.as_view(), name='bookmark_create'),
    path('profile/my-products', CurrentUserProductsView.as_view(template_name='flea_market/my_products.html'),
         name='my_products'),
    path('profile/password-change', PasswordChangeView.as_view(template_name='flea_market/password_change.html',
                                                               success_url=reverse_lazy('flea_market:profile')),
         name='password_change'),
]