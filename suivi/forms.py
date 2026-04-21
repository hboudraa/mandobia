from django import forms
from .models import SuiviBaldiya, STATUT_CHOICES
from django.contrib.auth.models import User


class SuiviBaldiyaForm(forms.ModelForm):
    class Meta:
        model  = SuiviBaldiya
        fields = ['commune', 'statut', 'attribue_a', 'remarque', 'date_contact']
        widgets = {
            'commune':      forms.Select(attrs={'class': 'form-select'}),
            'statut':       forms.Select(attrs={'class': 'form-select'}),
            'attribue_a':   forms.Select(attrs={'class': 'form-select'}),
            'remarque':     forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
                                                  'placeholder': 'أضف ملاحظة...'}),
            'date_contact': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'commune':      'البلدية',
            'statut':       'الحالة',
            'attribue_a':   'مسند إلى',
            'remarque':     'الملاحظة',
            'date_contact': 'تاريخ الاتصال',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['attribue_a'].queryset = User.objects.filter(is_active=True).order_by('username')
        self.fields['attribue_a'].empty_label = '— غير مسند —'
