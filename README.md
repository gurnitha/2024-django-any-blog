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










































































































































































































