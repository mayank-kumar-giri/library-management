from django.conf import settings
from django.db import models
from django.utils import timezone

class Record(models.Model):
    document_id = models.CharField(max_length=20)
    document_type = models.CharField(max_length=100)
    quantity = models.CharField(max_length=30)
    category = models.CharField(max_length=20) 

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

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    edition = models.CharField(max_length=30, default='1')
    record = models.OneToOneField(Record,
                                    on_delete=models.CASCADE,
                                    primary_key=True,
                                    default=1,
                                )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Journal(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=20)
    issue_id = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class JournalArticle(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)
    record = models.OneToOneField(Record,
                                    on_delete=models.CASCADE,
                                    primary_key=True,
                                    default=1,
                                )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Magazine(models.Model):
    record = models.OneToOneField(Record,
                                    on_delete=models.CASCADE,
                                    primary_key=True,
                                    default=1,
                                )
    title = models.CharField(max_length=100)
    issue_id = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Issue(models.Model):
    title = models.CharField(max_length=100)
    contributor = models.CharField(max_length=20)
    published_date = models.CharField(max_length = 30)
    editor = models.CharField(max_length=30)
    journal_id = models.ForeignKey(Journal, on_delete=models.CASCADE)
    magazine_id = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=20)
    member_type = models.CharField(max_length=30)
    contactNumber = models.CharField(max_length=20) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class UserBooking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    physical_copy = models.OneToOneField(PhysicalCopy,
                                    on_delete=models.CASCADE,
                                    primary_key=True,
                                )
    booking_date = models.CharField(max_length=30)
    due_date = models.CharField(max_length=20)
    status = models.CharField(max_length = 30) 

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title