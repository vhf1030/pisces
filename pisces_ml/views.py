from django.shortcuts import render  # type: ignore
from django.http import JsonResponse  # type: ignore
import os
import json
from datetime import datetime
# Create your views here.


def market_overview(request):
    # !TODO!
    # 예시 데이터 로드 (JSON 파일 또는 DB에서 가져오기)
    data_path = os.path.join('static', 'data', 'market_prices.json')
    with open(data_path, 'r') as file:
        market_data = json.load(file)
    
    context = {'market_data': market_data}
    return render(request, 'pisces_ml/market_overview.html', context)



# def predict_seafood_price(request):
#     if request.method == 'POST':
#         seafood = request.POST.get('seafood')
#         date = request.POST.get('date')

#         # 예측 로직 (머신러닝 모델 사용)
#         # 여기에 모델 호출 코드를 작성하세요.
#         prediction = {
#             "Market 1": 1234.56,
#             "Market 2": 2345.67,
#             "Market 3": 3456.78,
#         }

#         return render(request, 'pisces_ml/seafood_prediction.html', {
#             'seafood': seafood,
#             'date': date,
#             'prediction': prediction
#         })
#     return render(request, 'pisces_ml/seafood_input.html')


# def predict_market_prices(request):
#     if request.method == 'POST':
#         market = request.POST.get('market')
#         date = request.POST.get('date')

#         # 예측 로직 (머신러닝 모델 사용)
#         # 여기에 모델 호출 코드를 작성하세요.
#         prediction = {
#             "Seafood 1": 1234.56,
#             "Seafood 2": 2345.67,
#             "Seafood 3": 3456.78,
#         }

#         return render(request, 'pisces_ml/market_prediction.html', {
#             'market': market,
#             'date': date,
#             'prediction': prediction
#         })
#     return render(request, 'pisces_ml/market_input.html')


def predict_market(request):
    if request.method == 'POST':
        market = request.POST.get('market')
        date = request.POST.get('date')

        # 예측 로직
        prediction = {
            "농어": 12345,
            "광어": 67890,
        }

        return render(request, 'pisces_ml/market_template.html', {
            'prediction': prediction,
            'market': market,
            'date': date
        })

    return render(request, 'pisces_ml/market_template.html', {'market': None, 'date': None})



def predict_seafood(request):
    if request.method == 'POST':
        seafood = request.POST.get('seafood')
        date = request.POST.get('date')

        # 예측 로직
        prediction = {
            "가락시장": 12345,
            "구리농수산물시장": 67890,
        }

        return render(request, 'pisces_ml/seafood_template.html', {
            'prediction': prediction,
            'seafood': seafood,
            'date': date
        })

    return render(request, 'pisces_ml/seafood_template.html', {'seafood': None, 'date': None})


# def index(request):
#     return render(request, 'pisces_ml/index.html')

# 임시 모델 예측 함수 (머신러닝 모델 로드 시 대체)
def mock_predict(market, item, date):
    # 예시: 시장 이름, 품목, 날짜를 기반으로 간단한 예측
    return f"{hash(market) % 100 * 10 + hash(item) % 1000 * 100 + hash(date.split('-')[2]) % 100 * 10}원"

def predict_page(request):
    """입력 폼 및 결과 페이지"""
    return render(request, 'pisces_ml/predict.html')

def predict(request):  # to be deprecated
    """예측 요청 처리"""
    if request.method == 'POST':
        market = request.POST.get('market')
        item = request.POST.get('item')
        date = request.POST.get('date')
        try:
            if not market or not item or not date:
                raise ValueError("All fields are required.")

            # 임시 예측 로직 (머신러닝 모델 로드 후 대체)
            prediction = mock_predict(market, item, date)
            return JsonResponse({'prediction': prediction})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
