"""
سكريبت إنشاء المستخدمين العشرة
شغّله بـ: python manage.py shell < create_users.py
"""
from django.contrib.auth.models import User

users = [
    {'username': 'user01', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '01'},
    {'username': 'user02', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '02'},
    {'username': 'user03', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '03'},
    {'username': 'user04', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '04'},
    {'username': 'user05', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '05'},
    {'username': 'user06', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '06'},
    {'username': 'user07', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '07'},
    {'username': 'user08', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '08'},
    {'username': 'user09', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '09'},
    {'username': 'user10', 'password': 'mandobia2024', 'first_name': 'مستخدم', 'last_name': '10'},
]

created = 0
for u in users:
    if not User.objects.filter(username=u['username']).exists():
        User.objects.create_user(
            username=u['username'],
            password=u['password'],
            first_name=u['first_name'],
            last_name=u['last_name'],
        )
        print(f"✓ تم إنشاء: {u['username']}")
        created += 1
    else:
        print(f"⚠ موجود مسبقاً: {u['username']}")

print(f"\nتم إنشاء {created} مستخدم جديد.")
print("كلمة المرور الافتراضية لكل مستخدم: mandobia2024")
