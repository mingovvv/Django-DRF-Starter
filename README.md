# Django & Django REST framework Starter

---

## Install

```commandline
pip install djangorestframework
```

| Package                   | Version |
|---------------------------|---------|
| asgiref                   | 3.8.1   |
| ***Django***              | 5.1     |
| ***djangorestframework*** | 3.15.2  |
| pip                       | 23.2.1  |
| setuptools                | 68.2.0  |
| sqlparse                  | 0.5.1   |
| tzdata                    | 2024.1  |
| wheel                     | 0.41.2  |

## Create Project

```commandline
django-admin startproject 'proejct-name'
```

or

```commandline
django-admin startproject config .
```

## Create App

```commandline
python manage.py startapp 'app-name'
```

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app' # add app_name
]
```
 - App 적용 

## Start Project

```commandline
python manage.py runserver
```

## Combine Django REST Framework
Open `{project-name}/settings.py` file.  
[settings.py](config%2Fsettings.py)
```python
INSTALLED_APPS = [
    # ...
    'rest_framework', # add DRF
    # ...
]
```

인증 및 권한 클래스, 페이지네이션 설정 등 다양한 설정을 추가하고 싶으면 `REST_FRAMEWORK`를 추가한다.
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

## Django Project & App Structure
```markdown
.    
├── manage.py - `관리 작업을 위한 명령 줄 유틸리티`    
├── project_name(config)    
│   ├── __init__.py  
│   ├── asgi.py  
│   ├── settings.py - `전체 Django 프로젝트의 구성`  
│   ├── urls.py - `URL을 기반으로 웹 요청 라우팅`   
│   └── wsgi.py  
├── app_name_1  
│   ├── __init__.py  
│   ├── admin.py - `Django 관리자 인터페이스를 구성`  
│   ├── apps.py  
│   ├── migrations  
│   │   └── ...  
│   ├── models.py - `데이터베이스 스키마`  
│   ├── tests.py - `단위 테스트`   
│   └── views.py - `비즈니스 로직 (like MVC Controller)`   
├── app_name_2  
│   ├── __init__.py  
│   ├── admin.py  
│   ├── apps.py  
│   ├── migrations  
│   │   └── ...  
│   ├── models.py  
│   ├── tests.py  
│   └── views.py  
└── app_name_3  
    ├── __init__.py    
    ├── admin.py  
    ├── apps.py  
    ├── migrations  
    │   └── ...  
    ├── models.py  
    ├── tests.py  
    └── views.py  
```

## Model
![img_1.png](img%2Fimg_1.png)
 - 1:1 관계: `OneToOneField`
 - 1:N 관계: `ForeignKey`
 - N:M 관계: `ManyToManyField`

### Database Connection
Django 5.1 requires mysqlclient 1.4.3 or later.

```commandline
pip install mysqlclient
```

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "{database_name}",
        "USER": "{user_name}",
        "PASSWORD": "{user_password}",
        "HOST": "{database_host}",
        "PORT": "{database_port}",
    }
}
```
- django.db.backends.postgresql
- django.db.backends.mysql
- django.db.backends.sqlite3
- django.db.backends.oracle

### Model migration과 데이터베이스 스키마 관리
migration은 Model의 필드 추가 또는 삭제 등... 변경 사항을 데이터베이스 스키마에 전파하는 Django의 방법을 의미한다.

```commandline
python manage.py makemigrations
```
 - Model 수정 이후, 변경 사항을 데이터베이스 스키마에 전파하기 위해 마이크레이션 파일을 생성한다.
 - `app_name/migrations/000n_initial.py` 경로에 파일 생성.
 - Model의 변경 사항을 추적하고 감시

```commandline
python manage.py migrate
```
 - 마이그레이션 파일을 데이터베이스에 적용한다.

### TODO
 - 환경 별 DB연결 설정

## View
Django의 뷰(Views)는 웹 요청을 받아 처리하고 웹 응답을 반환하는 Python 함수를 의미함.

### Function-Based Views, FBVs, 함수 기반의 Views
```python
from django.http import HttpResponse
def hello_world(request):
    return HttpResponse("Hello, World!")
```
 - 간단하고 직관적임.

### Class-Based Views, CBVs, 클래스 기반의 Views
```python
from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")
```
 - 유연하고 재사용에 용이함.
 - HTTP method는 클래스안에 정의된 메서드와 매핑됨.