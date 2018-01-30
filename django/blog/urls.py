from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('detail/', views.post_detail),
    re_path(r'(?P<pk>\d+)/$', views.post_detail)
    # 숫자가 1개 이상 반복도니느 경우를 정규표현식ㅇ르ㅗ 하되
    # 해당반복구간을 그룹으로 묶고 그룹이름을 pk로 지정

]
