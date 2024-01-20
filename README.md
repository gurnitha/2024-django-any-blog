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

#### 13. Refactor index template

        modified:   README.md
        new file:   templates/home/divider.html
        new file:   templates/home/featured-posts.html
        new file:   templates/home/gallery.html
        new file:   templates/home/hero.html
        new file:   templates/home/intro.html
        new file:   templates/home/latest-posts.html
        new file:   templates/home/newsletter.html
        modified:   templates/index.html

        Tested :)

#### 14. Adding page title

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/index.html 

#### 15. Creating blog page: template, views, urls

        modified:   README.md
        modified:   apps/posts/urls.py
        modified:   apps/posts/views.py
        new file:   static_in_env/favicon.ico
        new file:   templates/blog.html
        modified:   templates/shared/head.html
        modified:   templates/shared/header.html

        Tested :)

#### 16. Refactor blog template

        modified:   README.md
        modified:   templates/blog.html
        new file:   templates/blog/categories.html
        new file:   templates/blog/latest-posts.html
        new file:   templates/blog/pagination.html
        new file:   templates/blog/posts.html
        new file:   templates/blog/search.html
        new file:   templates/blog/tags.html

        Tested :)

#### 17. Moving aside files from blog folder to shared folder

        modified:   README.md
        modified:   templates/blog.html
        new file:   templates/shared/aside-categories.html
        renamed:    templates/blog/latest-posts.html -> templates/shared/aside-latest-posts.html
        renamed:    templates/blog/search.html -> templates/shared/aside-search.html
        renamed:    templates/blog/tags.html -> templates/shared/aside-tags.html

        Tested :)


#### 18. Moving aside files from blog folder to shared folder

        modified:   apps/posts/urls.py
        modified:   apps/posts/views.py
        renamed:    templates/blog.html -> templates/posts-list.html
        renamed:    templates/blog/categories.html -> templates/posts/categories.html
        renamed:    templates/blog/pagination.html -> templates/posts/pagination.html
        renamed:    templates/blog/posts.html -> templates/posts/posts.html
        modified:   templates/shared/header.html

        Note: 

        In navbar there are Blog and Post menus.
        They are similar, should be only one, either Blog or Post

        Tested :)

#### 19. Create single post page: template, views, urls and links

        modified:   README.md
        modified:   apps/posts/urls.py
        modified:   apps/posts/views.py
        modified:   templates/home/featured-posts.html
        new file:   templates/post-single.html
        modified:   templates/posts/posts.html
        modified:   templates/shared/header.html

        Tested :)

#### 20. Re-setting up STATIC and MEDIA files

        modified:   apps/posts/admin.py
        modified:   apps/posts/models.py
        renamed:    static_in_env/css/custom.css -> config/static/css/custom.css
        renamed:    static_in_env/css/fontastic.css -> config/static/css/fontastic.css
        ...
        renamed:    static_in_env/vendor/popper.js/umd/poppper.js.flow -> config/static/vendor/popper.js/umd/poppper.js.flow
        modified:   config/urls.py

        Note:

        1. Rename static_in_env to static
        2. Moved it to config folder
        3. Re-define path for static and media files

        Tested :)

#### 21. Create Author, Category, Tag and Post models

        modified:   apps/posts/admin.py
        new file:   apps/posts/migrations/0001_initial.py
        new file:   apps/posts/migrations/0002_alter_author_profile_picture_alter_post_thumbnail.py
        modified:   apps/posts/models.py
        modified:   config/settings.py
        new file:   media/uploads/profiles/ing.jpeg
        new file:   media/uploads/thumbnail/featured-pic-1.jpeg
        new file:   media/uploads/thumbnail/featured-pic-2.jpeg
        new file:   media/uploads/thumbnail/featured-pic-3.jpeg

        Note:

        1. Register models to admin.py
        2. Run migrations
        3. Create superuser
        4. Add some categories, tags, and posts

        Tested :)

#### 22. Making the slug field in post table prepopulated_fields

        modified:   README.md
        modified:   apps/posts/admin.py
        new file:   media/uploads/thumbnail/blog-1.jpg
        new file:   media/uploads/thumbnail/blog-2.jpg
        new file:   media/uploads/thumbnail/blog-3.jpg
        new file:   media/uploads/thumbnail/blog-post-1.jpeg
        new file:   media/uploads/thumbnail/blog-post-2.jpg
        new file:   media/uploads/thumbnail/blog-post-3.jpeg
        new file:   media/uploads/thumbnail/blog-post-4.jpeg

        Note: Added some more posts

        Tested :)

#### 23. Load and display featured posts

        modified:   README.md
        modified:   apps/posts/views.py
        modified:   templates/home/featured-posts.html

        Tested :)

#### 24. Load and display latest posts

        modified:   README.md
        modified:   apps/posts/views.py
        modified:   templates/home/latest-posts.html

        # Grab 3 latest posts and render them based on LIFO
        latest_posts = Post.objects.order_by('-timestamp')[0:3]

        Tested :)

#### 25. Create Singup model, and add functionality to Subscribe Newsletter and testing

        modified:   README.md
        #1 create Signup model
        modified:   apps/marketing/models.py 

        #2 register the Signup model
        modified:   apps/marketing/admin.py 

        #3 migrations
        new file:   apps/marketing/migrations/0001_initial.py 

        #4 define signup logic
        modified:   apps/posts/views.py 

        #5 define the form
        modified:   templates/home/newsletter.html 

        Tested :)

#### 26. Image Gallery: Create Gallery model, run migration, load on view method and display

        modified:   README.md
        modified:   apps/posts/admin.py
        modified:   apps/posts/models.py
        modified:   apps/posts/views.py
        new file:   media/gallery/2024/01/20/gallery-1.jpg
        new file:   media/gallery/2024/01/20/gallery-2.jpeg
        new file:   media/gallery/2024/01/20/gallery-3.jpg
        new file:   media/gallery/2024/01/20/gallery-4.jpg
        modified:   templates/home/gallery.html

        Tested :)

#### 27. Load and display all posts to posts-list page

        modified:   apps/posts/views.py
        modified:   templates/home/featured-posts.html
        renamed:    templates/posts/categories.html -> templates/posts/inc/categories.html
        renamed:    templates/posts/pagination.html -> templates/posts/inc/pagination.html
        new file:   templates/posts/inc/posts.html
        new file:   templates/posts/post-single.html
        new file:   templates/posts/posts-list.html
        deleted:    templates/posts/posts.html

        Tested :)

#### 28. Load and display latest posts on aside of the posts-list page

        modified:   README.md
        modified:   apps/posts/views.py
        modified:   templates/shared/aside-latest-posts.html 

        Tested :) 


#### 29. Create get_category_count view, Load, Count and display them

        modified:   README.md
        modified:   apps/posts/views.py
        modified:   templates/shared/aside-categories.html

        Tested :)

#### 30. Create get_tag_count view, Load, Count and display them

        modified:   README.md
        modified:   apps/posts/views.py
        modified:   templates/shared/aside-categories.html
        modified:   templates/shared/aside-tags.html

        Tested :)





























































































































































































