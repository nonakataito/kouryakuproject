from django.urls import path
from . import views

app_name = 'kouryaku'

urlpatterns = [
		path('',views.IndexView.as_view(), name='index'),

        path('post/', views.CreateKouryakuView.as_view(), name='post'),
        path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
		path('kouryakus/<int:category>',views.CategoryView.as_view(),
		name = 'kouryakus_cat'),
		path('user-list/<int:user>',views.UserView.as_view(),name = 'user_list'),
		path('kouryaku-detail/<int:pk>',views.DetailView.as_view(),name = 'kouryaku_detail'),
        path('kouryaku/<int:pk>/delete/',views.KouryakuDeleteView.as_view(),name = 'kouryaku_delete'),
        path('mypage/',views.MypageView.as_view(),name = 'mypage'),
		path('search/', views.search, name='search'),
] 