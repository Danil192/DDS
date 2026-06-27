from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import CashFlow
from .forms import CashFlowForm
from .filters import CashFlowFilter

class CashFlowListView(ListView):
    model = CashFlow
    template_name = 'core/cashflow_home.html'
    context_object_name = 'cashflows'
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        self.filterset = CashFlowFilter(self.request.GET, queryset=qs)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'core/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'core/cashflow_form.html'
    success_url = reverse_lazy('cashflow_list')

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'core/cashflow_confirm_delete.html'
    success_url = reverse_lazy('cashflow_list')