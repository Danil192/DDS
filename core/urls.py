from django.urls import path
from . import views

urlpatterns = [
    path('', views.CashFlowListView.as_view(), name='cashflow_list'),
    path('create/', views.CashFlowCreateView.as_view(), name='cashflow_create'),
    path('<int:pk>/update/', views.CashFlowUpdateView.as_view(), name='cashflow_update'),
    path('<int:pk>/delete/', views.CashFlowDeleteView.as_view(), name='cashflow_delete'),
]