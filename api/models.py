from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ApiData(models.Model):
    title = models.CharField(_("Title"), max_length=255, blank=True)                            
    body = models.CharField(blank=True, max_length=1023)
    q = models.CharField(_("q"), max_length=1023, blank=True)
    SORT_OPTIONS = (
        ('activity', 'Activity'),
        ('votes', 'Votes'),
        ('creation', 'Creation'),
        ('relevance', 'Relevance')
    )
    sort = models.CharField(_("Sort"), max_length=20, default='activity', choices=SORT_OPTIONS)
    DESCENDING = 'desc'
    Ascending = 'asc'
    ORDER_OPTIONS = (
        (DESCENDING, 'Descending'),
        (Ascending, 'Ascending')
    )
    order = models.CharField(_("Order"), max_length=20, default=DESCENDING, choices=ORDER_OPTIONS)
    BOOLEAN_FIELD_CHOICES = (
        (None, ''),
        (True, 'True'),
        (False, 'False')
    )
    closed = models.BooleanField(_("closed"), null=True, choices=BOOLEAN_FIELD_CHOICES)
    accepted = models.BooleanField(_("accepted"), null=True, choices=BOOLEAN_FIELD_CHOICES)
    fromdate = models.DateField(_("From Date"), null=True, blank=True)                        
    views = models.PositiveIntegerField(_("views"), blank=True, null=True)
    answers = models.PositiveIntegerField(_("Number of answers"), blank=True, null=True)
    todate = models.DateField(_("To Date"), null=True, blank=True)    
    notagged = models.CharField(_("Not tagged"), max_length=253, blank=True)
    tagged = models.CharField(_("Tagged"), max_length=255, blank=True)
    min_date = models.DateField(_("min"), null=True, blank=True)
    max_date = models.DateField(_("max"), null=True, blank=True)
    migrated = models.BooleanField(_("migrated"), null=True, choices=BOOLEAN_FIELD_CHOICES)
    notice = models.BooleanField(_("Notice"), null=True, choices=BOOLEAN_FIELD_CHOICES)
    user = models.PositiveIntegerField(_("Id of user"), null=True, blank=True)    
    url = models.CharField(_("url"), max_length=255, blank=True)
    wiki = models.BooleanField(_("wiki"), null=True, choices=BOOLEAN_FIELD_CHOICES)
    page =  models.PositiveIntegerField(_("Page number"), null=True, blank=True)
    pagesize = models.PositiveIntegerField(_("Page Size"), null=True, blank=True)
    class Meta:
        verbose_name = _("ApiData")
        verbose_name_plural = _("ApiDatas")

    def __str__(self):
        return self.title