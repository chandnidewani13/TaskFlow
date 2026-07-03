from django.db import models

class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    deadline = models.DateField()

    priority = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title
class Task(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    status = models.CharField(max_length=50)

    priority = models.CharField(max_length=50)

    assigned_to = models.CharField(max_length=100)

    deadline = models.DateField()
class Team(models.Model):

    name = models.CharField(max_length=200)

    leader = models.CharField(max_length=200)

    email = models.EmailField()

    skill = models.CharField(max_length=100)

    role = models.CharField(max_length=50)

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name
    
class Meeting(models.Model):

    title = models.CharField(max_length=200)

    date = models.DateField()

    time = models.TimeField()

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title
class Upload(models.Model):
    title = models.CharField(max_length=200)

    file = models.FileField(upload_to='uploads/')

    uploaded_at = models.DateTimeField(
    auto_now_add=True
    )

    def __str__(self):
        return self.title