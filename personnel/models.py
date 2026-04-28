from django.db import models


WILAYA_CHOICES = [
    ('01', 'أدرار'), ('02', 'الشلف'), ('03', 'الأغواط'), ('04', 'أم البواقي'),
    ('05', 'باتنة'), ('06', 'بجاية'), ('07', 'بسكرة'), ('08', 'بشار'),
    ('09', 'البليدة'), ('10', 'البويرة'), ('11', 'تمنراست'), ('12', 'تبسة'),
    ('13', 'تلمسان'), ('14', 'تيارت'), ('15', 'تيزي وزو'), ('16', 'الجزائر'),
    ('17', 'الجلفة'), ('18', 'جيجل'), ('19', 'سطيف'), ('20', 'سعيدة'),
    ('21', 'سكيكدة'), ('22', 'سيدي بلعباس'), ('23', 'عنابة'), ('24', 'قالمة'),
    ('25', 'قسنطينة'), ('26', 'المدية'), ('27', 'مستغانم'), ('28', 'المسيلة'),
    ('29', 'معسكر'), ('30', 'ورقلة'), ('31', 'وهران'), ('32', 'البيض'),
    ('33', 'إليزي'), ('34', 'برج بوعريريج'), ('35', 'بومرداس'), ('36', 'الطارف'),
    ('37', 'تندوف'), ('38', 'تيسمسيلت'), ('39', 'الوادي'), ('40', 'خنشلة'),
    ('41', 'سوق أهراس'), ('42', 'تيبازة'), ('43', 'ميلة'), ('44', 'عين الدفلى'),
    ('45', 'النعامة'), ('46', 'عين تيموشنت'), ('47', 'غرداية'), ('48', 'غليزان'),
    ('49', 'تيميمون'), ('50', 'برج باجي مختار'), ('51', 'أولاد جلال'),
    ('52', 'بني عباس'), ('53', 'عين صالح'), ('54', 'عين قزام'), ('55', 'تقرت'),
    ('56', 'جانت'), ('57', 'المغير'), ('58', 'المنيعة'),
]

COMMUNE_CHOICES = [
    ('0601', 'بجاية'), ('0602', 'أميزور'), ('0603', 'فرعون'), ('0604', 'تأوريرت اغيل'),
    ('0605', 'شلاطة'), ('0606', 'تامقرة'), ('0607', 'تيمزريت'), ('0608', 'سوق الاثنين'),
    ('0609', 'مسيسنة'), ('0610', 'تينبذار'), ('0611', 'تيشي'), ('0612', 'سمعون'),
    ('0613', 'كنديرة'), ('0614', 'تيفرة'), ('0615', 'إغرم'), ('0616', 'أمالو'),
    ('0617', 'إغيل على'), ('0618', 'فلاين الماثن'), ('0619', 'توجة'), ('0620', 'درقينة'),
    ('0621', 'سيدي عياد'), ('0622', 'أوقاس'), ('0623', 'بني جليل'), ('0624', 'أدكار'),
    ('0625', 'أقبو'), ('0626', 'صدوق'), ('0627', 'تازمالت'), ('0628', 'آيت رزين'),
    ('0629', 'شميني'), ('0630', 'السوق أوفلة'), ('0631', 'تاسكريوت'), ('0632', 'طيبان'),
    ('0633', 'تالة حمزة'), ('0634', 'برباشة'), ('0635', 'بني كسيلة'), ('0636', 'أوزلاقن'),
    ('0637', 'بوحمزة'), ('0638', 'بنى مليكش'), ('0639', 'سيدي عيش'), ('0640', 'القصر'),
    ('0641', 'ملبو'), ('0642', 'أكفادو'), ('0643', 'لفلاي'), ('0644', 'خراطة'),
    ('0645', 'ذراع القايد'), ('0646', 'تامريجت'), ('0647', 'أيت سماعيل'), ('0648', 'بوخليفة'),
    ('0649', 'تيزى نبربر'), ('0650', 'بنى معوش'), ('0651', 'وادي غير'), ('0652', 'بوجليل'),
]

SEXE_CHOICES = [
    ('M', 'ذكر'),
    ('F', 'أنثى'),
]

CATEGORIE_CHOICES = [
    ('mandoub', 'مندوب'),
    ('ouvrier', 'عامل مندوبية'),
    ('charge_application', 'مكلف بالتطبيقة'),
    ('SG','أمين عام'),
    ('responsable', 'مسؤول / إداري'),
    ('a_disposition','تحت التصرف'),
]

ROLE_CHOICES = [
    ('admin', 'مدير النظام'),
    ('editeur', 'محرر'),
    ('lecteur', 'قارئ'),
]


class Personne(models.Model):
    """Modèle de base pour toutes les catégories de personnel"""

    # Catégorie
    categorie = models.CharField('الفئة', max_length=30, choices=CATEGORIE_CHOICES)

    # Informations personnelles
    nom = models.CharField('اللقب', max_length=100)
    prenom = models.CharField('الاسم', max_length=100)
    sexe = models.CharField('الجنس', max_length=1, choices=SEXE_CHOICES)
    date_naissance = models.DateField('تاريخ الميلاد')
    lieu_naissance = models.CharField('مكان الميلاد', max_length=150)

    # Numéro d'identification nationale
    nin = models.CharField('رقم التعريف الوطني (NIN)', max_length=18, unique=True)

    # Contact
    telephone = models.CharField('رقم الهاتف', max_length=10)
    telephone2 = models.CharField('رقم هاتف ثانوي', max_length=10, blank=True, null=True)
    fax = models.CharField('فاكس', max_length=10, blank=True, null=True)
    email = models.EmailField('البريد الإلكتروني', blank=True, null=True)

    # Adresse
    adresse = models.TextField('العنوان')
    commune = models.CharField('البلدية', max_length=4, choices=COMMUNE_CHOICES)
    wilaya = models.CharField('الولاية', max_length=2, choices=WILAYA_CHOICES)

    # Compte bancaire
    rib = models.CharField('رقم الحساب البنكي (RIB)', max_length=23, blank=True, null=True)
    banque = models.CharField('البنك', max_length=100, blank=True, null=True)

    # Poste et mission
    poste = models.CharField('المنصب', max_length=150)
    mission = models.TextField('المهمة', blank=True, null=True)

    # Période de travail
    date_debut = models.DateField('تاريخ بداية العمل')
    date_fin = models.DateField('تاريخ نهاية العمل', blank=True, null=True)

    # Photo
    photo = models.ImageField('الصورة الشخصية', upload_to='photos/', blank=True, null=True)

    # Rôle système
    role_systeme = models.CharField('صلاحية النظام', max_length=20, choices=ROLE_CHOICES, default='lecteur')

    # Métadonnées
    cree_le = models.DateTimeField('تاريخ الإنشاء', auto_now_add=True)
    modifie_le = models.DateTimeField('تاريخ التعديل', auto_now=True)
    actif = models.BooleanField('نشط', default=True)

    class Meta:
        verbose_name = 'شخص'
        verbose_name_plural = 'الأشخاص'
        ordering = ['nom', 'prenom']

    def __str__(self):
        return f"{self.nom} {self.prenom} — {self.get_categorie_display()}"

    def get_full_name(self):
        return f"{self.nom} {self.prenom}"
