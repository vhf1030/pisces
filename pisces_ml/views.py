from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'pisces_ml/index.html')

# 임시 모델 예측 함수 (머신러닝 모델 로드 시 대체)
def mock_predict(market, item, date):
    # 예시: 시장 이름, 품목, 날짜를 기반으로 간단한 예측
    return f"${len(market) * 10 + len(item) * 5 + int(date.split('-')[2])}"

def predict_page(request):
    """입력 폼 및 결과 페이지"""
    return render(request, 'pisces_ml/predict.html')

def predict(request):
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
