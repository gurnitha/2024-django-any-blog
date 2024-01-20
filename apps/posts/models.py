# apps/posts/models.py

# Django modules
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Define User
User = get_user_model()


# Author model
class Author(models.Model):
	# Author has OneToOne relationship with the User model
	# An author is belong to a user
	user 			= models.OneToOneField(User,on_delete=models.CASCADE)
	profile_picture = models.ImageField()

	class Meta:
		verbose_name = 'Author'
		verbose_name_plural = 'Authors'

	def __str__(self):
		return self.user.username


# Category model
class Category(models.Model):
	title = models.CharField(max_length=50)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title


# Tag model
class Tag(models.Model):
	title 		= models.CharField(max_length=50)
	# Tag has ManyToOne relationship with Category.
	# Many tags can belong to a category. 
	category 	= models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	def __str__(self):
		return self.title


# Post model
class Post(models.Model):
	title 			= models.CharField(max_length=100)
	slug 			= models.SlugField(max_length=250)
	overview 		= models.TextField()
	timestamp 		= models.DateTimeField(auto_now_add=True)
	comment_count 	= models.IntegerField(default=0)
	view_count 		= models.IntegerField(default=0)
	# Post has ManyToOne relationship with Author.
	# Many posts can belong to an author. 	
	author 			= models.ForeignKey(Author, on_delete=models.CASCADE)
	thumbnail 		= models.ImageField()
	# Post has ManyToMany relationship with Category.
	# A post can have many categories.
	categories 		= models.ManyToManyField(Category)
	# Post has ManyToMany relationship with Tag.
	# A post can have many tags.
	tags 			= models.ManyToManyField(Tag)
	featured 		= models.BooleanField()

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:post_single', kwargs={
			'id':self.id 
		})


# Gallery images
class Gallery(models.Model):
	title = models.CharField(max_length=100, blank=True, null=True)
	image = models.ImageField(upload_to='gallery/%Y/%m/%d')
	timestamp 		= models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Gallery'
		verbose_name_plural = 'Galleries'

	def __str__(self):
		return self.title