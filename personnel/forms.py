from django import forms
from .models import Personne, CATEGORIE_CHOICES


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        exclude = ['cree_le', 'modifie_le']
        widgets = {
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اللقب'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu_naissance': forms.TextInput(attrs={'class': 'form-control'}),
            'nin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXXXXXXXXXXXXXXX XX'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0XXXXXXXXX'}),
            'telephone2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0XXXXXXXXX'}),
            'fax': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '034XXXXXXX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'commune': forms.Select(attrs={'class': 'form-control'}),
            'wilaya': forms.Select(attrs={'class': 'form-select'}),
            'rib': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XX XXX XXXXXXXXXXXXXXXX XX'}),
            'banque': forms.TextInput(attrs={'class': 'form-control'}),
            'poste': forms.TextInput(attrs={'class': 'form-control'}),
            'mission': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'role_systeme': forms.Select(attrs={'class': 'form-select'}),
            'actif': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'categorie': 'الفئة',
            'nom': 'اللقب',
            'prenom': 'الاسم',
            'sexe': 'الجنس',
            'date_naissance': 'تاريخ الميلاد',
            'lieu_naissance': 'مكان الميلاد',
            'nin': 'رقم التعريف الوطني (NIN)',
            'telephone': 'رقم الهاتف',
            'telephone2': 'رقم هاتف ثانوي',
            'fax': 'فاكس',
            'email': 'البريد الإلكتروني',
            'adresse': 'العنوان الكامل',
            'commune': 'البلدية',
            'wilaya': 'الولاية',
            'rib': 'رقم الحساب البنكي (RIB)',
            'banque': 'اسم البنك / CCP',
            'poste': 'المنصب',
            'mission': 'المهمة',
            'date_debut': 'تاريخ بداية العمل',
            'date_fin': 'تاريخ نهاية العمل',
            'photo': 'الصورة الشخصية',
            'role_systeme': 'صلاحية النظام',
            'actif': 'نشط',
        }


class FiltreForm(forms.Form):
    categorie = forms.ChoiceField(
        choices=[('', 'كل الفئات')] + list(CATEGORIE_CHOICES),
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    wilaya = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ابحث بالولاية...'})
    )
    recherche = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ابحث بالاسم أو NIN...'})
    )
    actif = forms.ChoiceField(
        choices=[('', 'الكل'), ('1', 'نشط'), ('0', 'غير نشط')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
