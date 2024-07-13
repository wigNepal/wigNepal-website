from django.db import models

# Create your models here.
class submission(models.Model):
    education_level_choices = [
        ('diploma','Diploma'),
        ('bachelor','Bachelors'),
        ('master','Masters'),
        ('phd','PHD'),
        ('other','Other'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    education_level = models.CharField(max_length=50, blank=True, null=True, choices = education_level_choices)
    faculty = models.CharField(max_length=100, blank=True, null=True)
    institution_name = models.CharField(max_length=100, blank=True, null=True)
    graduation_year = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    organization_name = models.CharField(max_length=100, blank=True, null=True)
    organization_website = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    mentorship_participation = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')], blank=True, null=True)
    mentor_mentee = models.CharField(max_length=6, choices=[('mentor', 'Mentor'), ('mentee', 'Mentee')], blank=True, null=True)
    expectations = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    #profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)


    def __str__(self):
        return self.full_name