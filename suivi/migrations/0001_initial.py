from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuiviBaldiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(
                    choices=[
                        ('0601', 'بجاية'), ('0602', 'أميزور'), ('0603', 'فرعون'),
                        ('0604', 'تأوريرت اغيل'), ('0605', 'شلاطة'), ('0606', 'تامقرة'),
                        ('0607', 'تيمزريت'), ('0608', 'سوق الاثنين'), ('0609', 'مسيسنة'),
                        ('0610', 'تينبذار'), ('0611', 'تيشي'), ('0612', 'سمعون'),
                        ('0613', 'كنديرة'), ('0614', 'تيفرة'), ('0615', 'إغرم'),
                        ('0616', 'أمالو'), ('0617', 'إغيل على'), ('0618', 'فلاين الماثن'),
                        ('0619', 'توجة'), ('0620', 'درقينة'), ('0621', 'سيدي عياد'),
                        ('0622', 'أوقاس'), ('0623', 'بني جليل'), ('0624', 'أدكار'),
                        ('0625', 'أقبو'), ('0626', 'صدوق'), ('0627', 'تازمالت'),
                        ('0628', 'آيت رزين'), ('0629', 'شميني'), ('0630', 'السوق أوفلة'),
                        ('0631', 'تاسكريوت'), ('0632', 'طيبان'), ('0633', 'تالة حمزة'),
                        ('0634', 'برباشة'), ('0635', 'بني كسيلة'), ('0636', 'أوزلاقن'),
                        ('0637', 'بوحمزة'), ('0638', 'بنى مليكش'), ('0639', 'سيدي عيش'),
                        ('0640', 'القصر'), ('0641', 'ملبو'), ('0642', 'أكفادو'),
                        ('0643', 'لفلاي'), ('0644', 'خراطة'), ('0645', 'ذراع القايد'),
                        ('0646', 'تامريجت'), ('0647', 'أيت سماعيل'), ('0648', 'بوخليفة'),
                        ('0649', 'تيزى نبربر'), ('0650', 'بنى معوش'), ('0651', 'وادي غير'),
                        ('0652', 'بوجليل'),
                    ],
                    max_length=4, unique=True, verbose_name='البلدية'
                )),
                ('statut', models.CharField(
                    choices=[
                        ('en_attente', 'في الانتظار'), ('contacte', 'تم الاتصال'),
                        ('en_cours', 'جارٍ العمل'), ('termine', 'تمت العملية'),
                        ('probleme', 'يوجد مشكل'),
                    ],
                    default='en_attente', max_length=20, verbose_name='الحالة'
                )),
                ('remarque', models.TextField(blank=True, verbose_name='الملاحظة')),
                ('date_contact', models.DateField(blank=True, null=True, verbose_name='تاريخ الاتصال')),
                ('modifie_le', models.DateTimeField(auto_now=True, verbose_name='تاريخ آخر تعديل')),
                ('cree_le', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('attribue_a', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='baldiyas',
                    to='auth.user', verbose_name='مسند إلى'
                )),
                ('modifie_par', models.ForeignKey(
                    blank=True, null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='modifications',
                    to='auth.user', verbose_name='آخر تعديل بواسطة'
                )),
            ],
            options={
                'verbose_name': 'متابعة بلدية',
                'verbose_name_plural': 'متابعة البلديات',
                'ordering': ['commune'],
            },
        ),
    ]
