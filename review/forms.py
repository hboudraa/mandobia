from django import forms
from .models import ReviewPeriod, electoralReview, VotersByAgeGroup


class ReviewPeriodForm(forms.ModelForm):
    class Meta:
        model = ReviewPeriod
        fields = ['year', 'start_date', 'end_date', 'is_active']
        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'السنة'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ElectoralReviewForm(forms.ModelForm):
    class Meta:
        model = electoralReview
        fields = [
            'review_period', 'municipality_code', 'municipality_name', 'wilaya',
            'voters_before_review',
            'new_by_age_reason', 'new_by_residence_change', 'new_by_omission', 'new_by_transfer',
            'new_males', 'new_females', 'new_registered_total',
            'removed_by_death', 'removed_by_duplication', 'removed_by_residence_change', 'removed_by_transfer', 'removed_by_loss_rights',
            'removed_males', 'removed_females', 'removed_total',
            'data_updated',
            'voters_after_review_males', 'voters_after_review_females',
            'created_by'
        ]
        widgets = {
            'review_period': forms.Select(attrs={'class': 'form-select'}),
            'municipality_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رمز البلدية'}),
            'municipality_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم البلدية'}),
            'wilaya': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الولاية'}),
            'voters_before_review': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_by_age_reason': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_by_residence_change': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_by_omission': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_by_transfer': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_males': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_females': forms.NumberInput(attrs={'class': 'form-control'}),
            'new_registered_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_by_death': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_by_duplication': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_by_residence_change': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_by_transfer': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_by_loss_rights': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_males': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_females': forms.NumberInput(attrs={'class': 'form-control'}),
            'removed_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'data_updated': forms.NumberInput(attrs={'class': 'form-control'}),
            'voters_after_review_males': forms.NumberInput(attrs={'class': 'form-control'}),
            'voters_after_review_females': forms.NumberInput(attrs={'class': 'form-control'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أنشأه'}),
        }


class VotersByAgeGroupForm(forms.ModelForm):
    class Meta:
        model = VotersByAgeGroup
        fields = ['age_group', 'males', 'females']
        widgets = {
            'age_group': forms.Select(attrs={'class': 'form-select'}),
            'males': forms.NumberInput(attrs={'class': 'form-control'}),
            'females': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ReviewFilterForm(forms.Form):
    """Form for filtering reviews"""
    review_period = forms.ModelChoiceField(
        queryset=ReviewPeriod.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='فترة المراجعة'
    )
    wilaya = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الولاية'}),
        label='الولاية'
    )
    municipality_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم البلدية'}),
        label='البلدية'
    )

