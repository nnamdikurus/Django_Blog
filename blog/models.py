from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    body = models.TextField()



    def __str__(self):
        return self.title


    def my_url(self):
        return reverse('post_detail',args = [str(self.id)])


class Comment(models.Model):
    name = models.ForeignKey("auth.User", on_delete=models.CASCADE,)
    text_of_comment = models.TextField()
    post = models.ForeignKey('Post',on_delete=models.CASCADE, related_name = "Comments")

    def __str__(self):
        return "comment by: {}".format(self.name)