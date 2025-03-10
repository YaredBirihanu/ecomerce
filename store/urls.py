from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('about/', views.about, name='about'),
    path('product/<int:pk>',views.product,name='product'),
    path('category/<str:foo>',views.category,name='category'),
]











# path('register/', views.register, name='register'),
#     path('profile/', views.profile, name='profile'),
#     path('cart/', views.cart, name='cart'),
#     path('checkout/', views.checkout, name='checkout'),
#     path('product/<int:id>/', views.product, name='product'),
#     path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
#     path('update_cart/<int:id>/<int:quantity>/', views.update_cart, name='update_cart'),
#     path('order_history/', views.order_history, name='order_history'),
#     path('order_detail/<int:id>/', views.order_detail, name='order_detail'),
#     path('search/', views.search, name='search'),
#     path('contact/', views.contact, name='contact'),
#     path('faq/', views.faq, name='faq'),
#     path('terms/', views.terms, name='terms'),
#     path('privacy/', views.privacy, name='privacy'),
#     path('returns/', views.returns, name='returns'),
#     path('shipping/', views.shipping, name='shipping'),
#     path('faq/', views.faq, name='faq'),
#     path('blog/', views.blog, name='blog'),
#     path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
#     path('news/', views.news, name='news'),
#     path('news_detail/<int:id>/', views.news_detail, name='news_detail'),
#     path('special_offers/', views.special_offers, name='special_offers'),
#     path('blog_category/<int:id>/', views.blog_category, name='blog_category'),
#     path('news_category/<int:id>/', views.news_category, name='news_category'),
#     path('contact_us/', views.contact_us, name='contact_us'),
#     path('subscribe/', views.subscribe, name='subscribe')
#     path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
#     path('password_reset/', views.password_reset, name='password_reset'),
#     path('password_reset_done/', views.password_reset_done, name='password_reset_done'),
#     path('password_reset_confirm/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm')
#     path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
#     path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
#     path('shipping_returns/', views.shipping_returns, name='shipping_returns'),
#     path('returns_policy/', views.returns_policy, name='returns_policy'),
#     path('refund_policy/', views.refund_policy, name='refund_policy')
#     path('delivery_policy/', views.delivery_policy, name='delivery_policy'),
#     path('returns_and_refunds/', views.returns_and_refunds, name='returns_and_refunds'),
#     path('returns_and_exchanges/', views.returns_and_exchanges, name='returns_and_exchanges'),
#     path('returns_and_returns/', views.returns_and_returns, name='returns_and_returns'),
#     path('returns_and_returns_policy/', views.returns_and_returns_policy, name='returns_and_returns_policy'),
#     path('returns_and_returns_faq/', views.returns_and_returns_faq, name='returns_and_returns_faq'),
#     path('returns_and_returns_terms/', views.returns_and_returns_terms, name='returns_and_returns_terms'),
#     path('returns_and_returns_faq/', views.returns_and_returns_faq, name='returns_and_returns_faq'),
#     path('returns_and_returns_terms/', views.returns_and_returns_terms, name='returns_and_returns_terms'),
#     path('returns_and_returns_shipping/', views.returns_and_returns_shipping, name='returns_and_returns_shipping'),
#     path('returns_and_returns_returns/', views.returns_and_returns_returns, name='returns_and_returns_returns'),
#     path('returns_and_returns_returns_policy/', views.returns_and_returns_returns_policy, name='returns_and_returns_returns_policy'),
#     path('returns_and_returns_returns_faq/', views.returns_and_returns_returns_faq, name='returns_and_returns_returns_faq'),
#     path('returns_and_returns_returns_terms/', views.returns_and_returns_returns_terms, name='returns_and_returns_returns_terms'),
#     path('returns_and_returns_returns_shipping/', views.returns_and_returns_returns_shipping, name='returns_and_returns_returns_shipping'),
#     path('returns_and_returns_returns/', views.returns_and_returns_returns, name='returns_and_returns_returns'),
