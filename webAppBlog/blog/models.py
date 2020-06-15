from django.db import models


# Store the category of each Post
class PostCategory(models.Model):
    name = models.CharField(max_length=50)
    

    class Meta:
        verbose_name_plural = 'PostCategories'
    
    def __str__(self):
        return self.name



# Store the Post
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('PostCategory', null=True, blank=True, on_delete=models.DO_NOTHING)

    published = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title



# Store the comments
class Comment(models.Model):
    STATUS_VISIBLE = 'visible'
    STATUS_HIDDEN = 'hidden'
    STATUS_MODERATED = 'moderated'

    STATUS_CHOICES = (
        (STATUS_VISIBLE, 'Visible'),
        (STATUS_HIDDEN, 'Hidden'),
        (STATUS_MODERATED, 'Moderated')
    )
    
    
    
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    status = models.CharField(max_length=20, default=STATUS_VISIBLE, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    moderation_text = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Comments'
    
    def __str__(self):
        return '{} - {} (status={})'.format(self.author_name, self.text[:20], self.status) 


