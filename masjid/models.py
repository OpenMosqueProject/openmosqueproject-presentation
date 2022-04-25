from django.db import models
from django.urls import reverse
# Create your models here.

PRAYER_METHOD_CHOICES = [
    (1, 'University of Islamic Sciences, Karachi'),
    (2, 'Islamic Society of North America'),
    (3, 'Muslim World League'),
    (4, 'Umm Al-Qura University, Makkah'),
    (5, 'Egyptian General Authority of Survey'),
    (7, 'Institute of Geophysics, University of Tehran'),
    (8, 'Gulf Region'),
    (9, 'Kuwait'),
    (10, 'Qatar'),
    (11, 'Majlis Ugama Islam Singapura, Singapore'),
    (12, 'Union Organization islamic de France'),
    (13, 'Diyanet İşleri Başkanlığı, Turkey'),
    (14, 'Spiritual Administration of Muslims of Russia'),
    (15, 'Moonsighting Committee Worldwide (also requires shafaq paramteer)')
]


class Masjid(models.Model):

    masjid_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    method = models.IntegerField(choices=PRAYER_METHOD_CHOICES, default=3)
    masjidLogo = models.ImageField(upload_to='images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('masjid_detail', kwargs={'pk': self.pk})
