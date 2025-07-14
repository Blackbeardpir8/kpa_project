from django.urls import path
from forms.views import BogieFormView, WheelFormView

urlpatterns = [
    path('forms/bogie-checksheet', BogieFormView.as_view()),
    path('forms/wheel-specifications', WheelFormView.as_view()),
]