import os
import django
from datetime import date, timedelta

# إعداد Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mandobia.settings')
django.setup()

from inventory.models import CategorieProduit, Fournisseur, Produit, Lot
from django.contrib.auth.models import User

def create_sample_data():
    # إنشاء مستخدم إذا لم يكن موجوداً
    user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        user.set_password('admin123')
        user.save()

    # إنشاء فئات المنتجات
    categories_data = [
        {'nom': 'أدوية', 'couleur': '#dc3545'},
        {'nom': 'معدات طبية', 'couleur': '#28a745'},
        {'nom': 'مستلزمات', 'couleur': '#007bff'},
        {'nom': 'مواد كيميائية', 'couleur': '#ffc107'},
    ]

    categories = {}
    for cat_data in categories_data:
        cat, created = CategorieProduit.objects.get_or_create(
            nom=cat_data['nom'],
            defaults={'couleur': cat_data['couleur']}
        )
        categories[cat_data['nom']] = cat

    # إنشاء موردين
    fournisseurs_data = [
        {'nom': 'شركة الأدوية الجزائرية', 'contact': 'أحمد محمد', 'telephone': '021234567'},
        {'nom': 'مستودعات الطبية المركزية', 'contact': 'فاطمة علي', 'telephone': '021234568'},
        {'nom': 'شركة المعدات الطبية', 'contact': 'محمد أحمد', 'telephone': '021234569'},
    ]

    fournisseurs = {}
    for four_data in fournisseurs_data:
        four, created = Fournisseur.objects.get_or_create(
            nom=four_data['nom'],
            defaults={
                'contact': four_data['contact'],
                'telephone': four_data['telephone']
            }
        )
        fournisseurs[four_data['nom']] = four

    # إنشاء منتجات
    produits_data = [
        {
            'nom': 'أموكسيسيلين 500mg',
            'categorie': categories['أدوية'],
            'unite_mesure': 'piece',
            'quantite_stock': 150,
            'seuil_alerte': 20,
            'prix_achat': 25.50,
            'prix_vente': 35.00,
            'a_date_expiration': True,
            'duree_validite_jours': 365,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
            'emplacement': 'رف 1 - درج 2',
        },
        {
            'nom': 'إنسولين سريع المفعول',
            'categorie': categories['أدوية'],
            'unite_mesure': 'piece',
            'quantite_stock': 75,
            'seuil_alerte': 15,
            'prix_achat': 120.00,
            'prix_vente': 180.00,
            'a_date_expiration': True,
            'duree_validite_jours': 180,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
            'emplacement': 'ثلاجة الأدوية',
        },
        {
            'nom': 'قفازات طبية',
            'categorie': categories['مستلزمات'],
            'unite_mesure': 'piece',
            'quantite_stock': 500,
            'seuil_alerte': 50,
            'prix_achat': 2.50,
            'prix_vente': 4.00,
            'a_date_expiration': False,
            'fournisseur': fournisseurs['مستودعات الطبية المركزية'],
            'emplacement': 'رف 3 - درج 1',
        },
        {
            'nom': 'مطهر كحولي 70%',
            'categorie': categories['مواد كيميائية'],
            'unite_mesure': 'litre',
            'quantite_stock': 25,
            'seuil_alerte': 5,
            'prix_achat': 15.00,
            'prix_vente': 25.00,
            'a_date_expiration': True,
            'duree_validite_jours': 730,
            'fournisseur': fournisseurs['مستودعات الطبية المركزية'],
            'emplacement': 'مخزن المواد الكيميائية',
        },
        {
            'nom': 'مقياس ضغط دم إلكتروني',
            'categorie': categories['معدات طبية'],
            'unite_mesure': 'piece',
            'quantite_stock': 12,
            'seuil_alerte': 3,
            'prix_achat': 850.00,
            'prix_vente': 1200.00,
            'a_date_expiration': False,
            'fournisseur': fournisseurs['شركة المعدات الطبية'],
            'emplacement': 'رف المعدات - درج 1',
        },
    ]

    produits = {}
    for prod_data in produits_data:
        prod, created = Produit.objects.get_or_create(
            nom=prod_data['nom'],
            categorie=prod_data['categorie'],
            defaults={
                'unite_mesure': prod_data['unite_mesure'],
                'quantite_stock': prod_data['quantite_stock'],
                'seuil_alerte': prod_data['seuil_alerte'],
                'prix_achat': prod_data['prix_achat'],
                'prix_vente': prod_data['prix_vente'],
                'a_date_expiration': prod_data['a_date_expiration'],
                'duree_validite_jours': prod_data.get('duree_validite_jours'),
                'fournisseur': prod_data.get('fournisseur'),
                'emplacement': prod_data.get('emplacement'),
                'cree_par': user,
            }
        )
        produits[prod_data['nom']] = prod

    # إنشاء دفعات للمنتجات ذات الصلاحية
    today = date.today()

    lots_data = [
        {
            'produit': produits['أموكسيسيلين 500mg'],
            'numero_lot': 'AMOX2024001',
            'date_fabrication': today - timedelta(days=30),
            'date_expiration': today + timedelta(days=335),  # 11 شهر من الآن
            'quantite_initiale': 200,
            'quantite_restante': 150,
            'prix_achat_unitaire': 25.50,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
        },
        {
            'produit': produits['أموكسيسيلين 500mg'],
            'numero_lot': 'AMOX2024002',
            'date_fabrication': today - timedelta(days=15),
            'date_expiration': today + timedelta(days=350),  # سنة من الآن
            'quantite_initiale': 100,
            'quantite_restante': 100,
            'prix_achat_unitaire': 26.00,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
        },
        {
            'produit': produits['إنسولين سريع المفعول'],
            'numero_lot': 'INSU2024001',
            'date_fabrication': today - timedelta(days=45),
            'date_expiration': today + timedelta(days=135),  # 4.5 أشهر من الآن
            'quantite_initiale': 100,
            'quantite_restante': 75,
            'prix_achat_unitaire': 120.00,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
        },
        {
            'produit': produits['إنسولين سريع المفعول'],
            'numero_lot': 'INSU2024002',
            'date_fabrication': today - timedelta(days=10),
            'date_expiration': today + timedelta(days=170),  # 5.5 أشهر من الآن
            'quantite_initiale': 50,
            'quantite_restante': 50,
            'prix_achat_unitaire': 125.00,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
        },
        {
            'produit': produits['مطهر كحولي 70%'],
            'numero_lot': 'ALCO2024001',
            'date_fabrication': today - timedelta(days=60),
            'date_expiration': today + timedelta(days=670),  # 22 شهر من الآن
            'quantite_initiale': 30,
            'quantite_restante': 25,
            'prix_achat_unitaire': 15.00,
            'fournisseur': fournisseurs['مستودعات الطبية المركزية'],
        },
        # منتج منتهي الصلاحية (للاختبار)
        {
            'produit': produits['أموكسيسيلين 500mg'],
            'numero_lot': 'AMOX2023001',
            'date_fabrication': today - timedelta(days=400),
            'date_expiration': today - timedelta(days=30),  # انتهت منذ شهر
            'quantite_initiale': 100,
            'quantite_restante': 15,
            'prix_achat_unitaire': 24.00,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
        },
        # منتج سينتهي قريباً (للاختبار)
        {
            'produit': produits['إنسولين سريع المفعول'],
            'numero_lot': 'INSU2024003',
            'date_fabrication': today - timedelta(days=160),
            'date_expiration': today + timedelta(days=5),  # سينتهي خلال 5 أيام
            'quantite_initiale': 20,
            'quantite_restante': 18,
            'prix_achat_unitaire': 118.00,
            'fournisseur': fournisseurs['شركة الأدوية الجزائرية'],
        },
    ]

    for lot_data in lots_data:
        lot, created = Lot.objects.get_or_create(
            produit=lot_data['produit'],
            numero_lot=lot_data['numero_lot'],
            defaults={
                'date_fabrication': lot_data.get('date_fabrication'),
                'date_expiration': lot_data['date_expiration'],
                'quantite_initiale': lot_data['quantite_initiale'],
                'quantite_restante': lot_data['quantite_restante'],
                'prix_achat_unitaire': lot_data['prix_achat_unitaire'],
                'fournisseur': lot_data.get('fournisseur'),
                'cree_par': user,
            }
        )

    print("تم إنشاء البيانات التجريبية بنجاح!")
    print(f"- {len(categories)} فئة منتج")
    print(f"- {len(fournisseurs)} مورد")
    print(f"- {len(produits)} منتج")
    print(f"- {len(lots_data)} دفعة")

if __name__ == '__main__':
    create_sample_data()
