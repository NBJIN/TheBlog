from django.db import models
from django.contrib.auth.models import User, timezone
from cloudinary.models import CloudinaryField
# from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# added tupple status to show wheather our post is draft or published
STATUS = (
    (0, "Draft"),
    (1, "Published")
    )

# models below
# Create a post model


class Post(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    post_contributor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blogap_posts')
    date_of_post = models.DateTimeField(auto_created=True)
    update_post = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    content = RichTextField(max_length=7000, blank=True, null=True)
    no_of_likes = models.ManyToManyField(
        User, related_name="blogap_no_of_likes")
    excerpt = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)


   # def save(self):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #         super(Post, self).save(*args, **kwa
    # def save(self, *args, **kwargs):
        # self.slug = slugify(self.Post_name)
        # super(Post, self).save(*args, **kwargs)

# added show descending order of posts
    class Meta:
        ordering = ['-date_of_post']

# On admin page allow user to see name and author
    def __str__(self):
        return self.name + ' | ' + slef.post_contributor

# added show total no of likes on a post
    def no_of_likes(self):
        return self.no_of_likes.count()

# added Comment on a post model


class Comment(models.Model):
    contributor_comment = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')
    email = models.EmailField()
    date_of_comment = models.DateTimeField(auto_created=True)
    image = CloudinaryField('image', default='placeholder')
    content = RichTextField(max_length=7000, blank=True, null=True)
    # content = models.TextField()
    no_of_comments = models.ManyToManyField(User, related_name="blog_comment")
    approved = models.BooleanField('Approved', default='False')


# added show descending order of comments
class Meta:
    ordering = ['-date_of_comment']

# added on admin page allow auther to see contributor
    def __str__(self):
        return self.contributor_comment()

# added show total number of comments
    def no_of_comments(self):
        return self.no_of_comments.count()

    def __str__(self):
        return f"comment {self.body} by {self.contributor_comment}"
