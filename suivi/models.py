from django.db import models
from django.contrib.auth.models import User


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

STATUT_CHOICES = [
    ('en_attente', 'في الانتظار'),
    ('contacte',   'تم الاتصال'),
    ('en_cours',   'جارٍ العمل'),
    ('termine',    'تمت العملية'),
    ('probleme',   'يوجد مشكل'),
]


class Tache(models.Model):
    nom         = models.CharField('اسم المهمة', max_length=200, unique=True)
    description = models.TextField('الوصف', blank=True)
    ordre       = models.PositiveIntegerField('الترتيب', default=0)
    actif       = models.BooleanField('نشط', default=True)
    cree_le     = models.DateTimeField('تاريخ الإنشاء', auto_now_add=True)

    class Meta:
        verbose_name        = 'مهمة'
        verbose_name_plural = 'المهام'
        ordering            = ['ordre', 'nom']

    def __str__(self):
        return self.nom


class SuiviTache(models.Model):
    baldiya     = models.ForeignKey('SuiviBaldiya', on_delete=models.CASCADE, verbose_name='البلدية', related_name='taches_suivi')
    tache       = models.ForeignKey(Tache, on_delete=models.CASCADE, verbose_name='المهمة')
    statut      = models.CharField('الحالة', max_length=20, choices=STATUT_CHOICES, default='en_attente')
    attribue_a  = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='مسند إلى', related_name='taches_suivi'
    )
    remarque    = models.TextField('الملاحظة', blank=True)
    date_debut  = models.DateField('تاريخ البداية', null=True, blank=True)
    date_fin    = models.DateField('تاريخ الانتهاء', null=True, blank=True)
    modifie_par = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='modifications_taches', verbose_name='آخر تعديل بواسطة'
    )
    modifie_le  = models.DateTimeField('تاريخ آخر تعديل', auto_now=True)
    cree_le     = models.DateTimeField('تاريخ الإنشاء', auto_now_add=True)

    class Meta:
        verbose_name        = 'متابعة مهمة'
        verbose_name_plural = 'متابعة المهام'
        ordering            = ['tache__ordre', 'cree_le']
        unique_together     = ['baldiya', 'tache']

    def __str__(self):
        return f"{self.baldiya.get_commune_display()} — {self.tache.nom}"

    def statut_color(self):
        return {
            'en_attente': 'secondary',
            'contacte':   'info',
            'en_cours':   'warning',
            'termine':    'success',
            'probleme':   'danger',
        }.get(self.statut, 'secondary')

    def statut_icon(self):
        return {
            'en_attente': 'hourglass',
            'contacte':   'telephone-fill',
            'en_cours':   'arrow-repeat',
            'termine':    'check-circle-fill',
            'probleme':   'exclamation-triangle-fill',
        }.get(self.statut, 'circle')


class SuiviBaldiya(models.Model):
    commune      = models.CharField('البلدية', max_length=4, choices=COMMUNE_CHOICES, unique=True)
    statut       = models.CharField('الحالة', max_length=20, choices=STATUT_CHOICES, default='en_attente')
    attribue_a   = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='مسند إلى', related_name='baldiyas'
    )
    remarque     = models.TextField('الملاحظة', blank=True)
    date_contact = models.DateField('تاريخ الاتصال', null=True, blank=True)
    modifie_par  = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='modifications', verbose_name='آخر تعديل بواسطة'
    )
    modifie_le   = models.DateTimeField('تاريخ آخر تعديل', auto_now=True)
    cree_le      = models.DateTimeField('تاريخ الإنشاء', auto_now_add=True)

    class Meta:
        verbose_name        = 'متابعة بلدية'
        verbose_name_plural = 'متابعة البلديات'
        ordering            = ['commune']

    def __str__(self):
        return f"{self.get_commune_display()} — {self.get_statut_display()}"

    def statut_color(self):
        return {
            'en_attente': 'secondary',
            'contacte':   'info',
            'en_cours':   'warning',
            'termine':    'success',
            'probleme':   'danger',
        }.get(self.statut, 'secondary')

    def statut_icon(self):
        return {
            'en_attente': 'hourglass',
            'contacte':   'telephone-fill',
            'en_cours':   'arrow-repeat',
            'termine':    'check-circle-fill',
            'probleme':   'exclamation-triangle-fill',
        }.get(self.statut, 'circle')
