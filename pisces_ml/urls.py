from django.urls import path  # type: ignore
from . import views

urlpatterns = [
    # path('', views.index, name='index'),  # 기본 화면
    path('', views.predict_page, name='predict_page'),  # 입력 폼 페이지
    path('predict/', views.predict, name='predict'),   # 예측 API 엔드포인트
    # path('', views.market_overview, name='market_overview'),  # TODO
    path('predict/seafood/', views.predict_seafood_price, name='predict_seafood_price'),  # TODO
    path('predict/market/', views.predict_market_prices, name='predict_market_prices'),  # TODO
]

