from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    edition = models.CharField(max_length=30)
    record = models.OneToOneField(Record,
                                    on_delete=models.CASCADE,
                                    primary_key=True,
                                )
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class User(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=20)
    member_type = models.CharField(max_length=30)
    contactNumber = models.CharField(max_length=20) 
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PhysicalCopy(models.Model):
    record_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class UserBooking(models.Model):
    member_id = models.ForeignKey(Record, on_delete=models.CASCADE)
    physical_copy_id = models.OneToOneField(UserBooking,
                                    on_delete=models.CASCADE,
                                    primary_key=True,
                                )
    booking_date = models.CharField(max_length=30)
    due_date = models.CharField(max_length=20)
    status = models.CharField(max_length = 30) 
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Record(models.Model):
    document_id = models.CharField(max_length=20)
    document_type = models.CharField(max_length=100)
    # document_id = models.CharField(max_length=20)
    quantity = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    # status = models.CharField(max_length = 30) 
    # created_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class JournalArticle(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    journal_id = models.CharField(max_length=30)
    # category = models.CharField(max_length=20)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Magazine(models.Model):
    title = models.CharField(max_length=100)
    # author = models.CharField(max_length=20)
    issue_id = models.CharField(max_length=30)
    # category = models.CharField(max_length=20)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Journal(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=20)
    issue_id = models.CharField(max_length=30)
    # category = models.CharField(max_length=20)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Magazine(models.Model):
    title = models.CharField(max_length=100)
    contributor = models.CharField(max_length=20)
    published_date = models.CharField(max_length = 30)
    editor = models.CharField(max_length=30)
    # category = models.CharField(max_length=20)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title