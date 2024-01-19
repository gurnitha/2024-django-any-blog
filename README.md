# 2024-django-any-blog
Membuat aplikasi Blog menggunakan Django versi 5
Github: https://github.com/gurnitha/2024-django-any-blog
Ytb: https://www.youtube.com/watch?v=HWg3zXWwre8


#### 1. Inisial setup

        modified:   .gitignore
        modified:   README.md

#### 2. Membuat virtual env dan install django

        E:\_WORKSPACE\2024\django\BLOG\2024-django-any-blog(main -> origin)
        λ python -m venv venv31250
        λ venv31250\Scripts\activate.bat
        (venv31250) λ pip install django

                (venv31250) λ pip list
        Package  Version
        -------- -------
        asgiref  3.7.2
        Django   5.0.1
        pip      23.2.1
        sqlparse 0.4.4
        tzdata   2023.4

#### 3. Membuat proyek django dengan nama 'config' di dalam folder src

        E:\_WORKSPACE\2024\django\BLOG\2024-django-any-blog(main -> origin)
        (venv31250) λ cd src\
        (venv31250) λ django-admin startproject config .
        (venv31250) λ ls
        config/  manage.py*  README.md

#### 4. Membuat apps django: apps/posts dan apps/marketing

        E:\_WORKSPACE\2024\django\BLOG\2024-django-any-blog\src(main -> origin)
        (venv31250) λ mkdir apps\posts
        (venv31250) λ django-admin startapp posts apps\posts
        (venv31250) λ mkdir apps\marketing
        (venv31250) λ django-admin startapp marketing apps\marketing

#### 5. Install posts dan marketing pada config/settings.py

        modified:   README.md
        new file:   apps/marketing/__init__.py
        new file:   apps/marketing/admin.py
        new file:   apps/marketing/apps.py
        new file:   apps/marketing/migrations/__init__.py
        new file:   apps/marketing/models.py
        new file:   apps/marketing/tests.py
        new file:   apps/marketing/views.py
        new file:   apps/posts/__init__.py
        new file:   apps/posts/admin.py
        new file:   apps/posts/apps.py
        new file:   apps/posts/migrations/__init__.py
        new file:   apps/posts/models.py
        new file:   apps/posts/tests.py
        new file:   apps/posts/views.py
        modified:   config/settings.py

#### 6. Menjalankan development server

        E:\_WORKSPACE\2024\django\BLOG\2024-django-any-blog\src(main -> origin)
        (venv31250) λ python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).

        You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
        Run 'python manage.py migrate' to apply them.
        January 20, 2024 - 05:51:10
        Django version 5.0.1, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

#### 7. Membuat Postgres db dan konek db dengan proyek

        modified:   README.md
        modified:   config/settings.py

        # DB: PostgreSQL
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': '2024-django-any-blog', 
                'USER': 'postgres', 
                'PASSWORD': 'pemogan148',
                'HOST': 'localhost', 
                'PORT': '5433',
            }
        }

        Testing: Restart server 

        :)

#### 8. Melindungi sensitif file dengan membuat .env file

        (venv31250) λ pip install django-environ
        (venv31250) λ pip install python-env
        (venv31250) λ pip install python-environ
        (venv31250) λ pip install python-dotenv

        new file:   .env.example
        modified:   README.md
        modified:   config/settings.py

        Tested :)

#### 9. Create home page: templates, views and urls

        modified:   README.md
        new file:   apps/posts/urls.py
        modified:   apps/posts/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   templates/index.html

        Note: Added bear html template

#### 10. Adding and loading static files
 
        modified:   README.md
        modified:   config/settings.py
        new file:   static_in_env/css/custom.css
        ..
        new file:   static_in_env/vendor/popper.js/umd/popper.min.js
        new file:   static_in_env/vendor/popper.js/umd/poppper.js.flow
        modified:   templates/index.html

        Tested :)

#### 11. Create and use base template

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/index.html 

        Tested :) 

#### 12. Refactor base templates

        modified:   templates/base.html
        new file:   templates/shared/footer.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header.html
        new file:   templates/shared/scripts.html

        Tested :)




























































































































































































