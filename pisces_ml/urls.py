from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),  # 기본 화면
    path('', views.predict_page, name='predict_page'),  # 입력 폼 페이지
    path('predict/', views.predict, name='predict'),   # 예측 API 엔드포인트
]
