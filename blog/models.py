from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

POST_CHOICES = (
    ('Published' ,'Published' ),
    ( 'In Review', 'In Review'),
    ( 'Draft', 'Draft'),
)



class Post(models.Model): # db table
    title =  models.CharField(max_length=10 , error_messages={
        'invalid_choice': 'Value %r is not a valid choice.',
        'null': 'This field cannot be null.',
        'blank': 'This field cannot be blank.' ,
        'required': 'this field is required now ',
    } , help_text="A unique title for this thing")  # db column
    created_at = models.DateTimeField(default=timezone.now)  ## auto_now = True [last updated]  | auto_now_add = True = default
    last_updated = models.DateTimeField(auto_now = True)
    author  = models.ForeignKey(User , related_name='post_author' , on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    post_status = models.CharField(max_length=10 , choices=POST_CHOICES ,default='Draft')

    ## imagefield  slug 

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post , related_name='post_comment' , on_delete=models.CASCADE)
    user = models.ForeignKey(User , related_name='comment_author' , on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)

    # test = models.ManyToManyField()
    # test = models.OneToOneField()

    def __str__(self):
        return str(self.post) + ' - ' + str(self.user)