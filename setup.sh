#!/bin/bash
# =============================================
# سكريبت إعداد وتشغيل مشروع مندوبية الانتخابات
# =============================================

echo "====================================="
echo "  إعداد مشروع مندوبية سلطة الانتخابات"
echo "====================================="

# 1. تثبيت المكتبات
echo ""
echo "[1/4] تثبيت المكتبات المطلوبة..."
pip install -r requirements.txt

# 2. إنشاء قاعدة البيانات
echo ""
echo "[2/4] إنشاء قاعدة البيانات..."
python manage.py makemigrations
python manage.py migrate

# 3. إنشاء حساب المدير
echo ""
echo "[3/4] إنشاء حساب المدير الرئيسي..."
echo "from django.contrib.auth import get_user_model; \
U = get_user_model(); \
U.objects.filter(username='admin').exists() or \
U.objects.create_superuser('admin', 'admin@mandobia.dz', 'admin123')" \
| python manage.py shell

echo ""
echo "[4/4] الإعداد اكتمل!"
echo ""
echo "====================================="
echo "  بيانات الدخول الافتراضية:"
echo "  المستخدم : admin"
echo "  كلمة المرور: admin123"
echo "====================================="
echo ""
echo "لتشغيل الخادم:"
echo "  python manage.py runserver"
echo ""
echo "ثم افتح المتصفح على:"
echo "  http://127.0.0.1:8000"
echo "====================================="
