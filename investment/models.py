#-*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

class Objective(models.Model):
    text = models.CharField(max_length=400)
    post_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.post_date = datetime.now()
        self.save

    def __str__(self):
        return self.text

class Blog(models.Model):
    INVESTMENT = 'INVESTMENT'
    COMPANY = 'COMPANY'
    HOME = 'HOME'
    OTHER = 'OTHER'
    CATEGORY_CHOICES = (
        (INVESTMENT, '투자'),
        (COMPANY, '회사'),
        (HOME, '가정'),
        (OTHER, '기타'),
    )

    post_date = models.DateTimeField(default=datetime.now())
    edit_date = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=200, choices = CATEGORY_CHOICES, default=INVESTMENT)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.post_date = datetime.now()
        self.save()

    def __str__(self):
        return self.title

class Phase(models.Model):
    startdate = models.DateTimeField()
    enddate = models.DateTimeField(blank=True,null=True)
    no = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.no)

class RESegment(models.Model):
    APARTMENT = 'AP'
    OFFICETEL = 'OF'
    TYPE_CHOICES = (
        (APARTMENT, 'Apartment'),
        (OFFICETEL, 'Officetel'),
    )
    segment_type = models.CharField(
        max_length = 2,
        choices = TYPE_CHOICES,
        default = APARTMENT,
    )

    def __str__(self):
        return self.segment_type

class SMSegment(models.Model):
    KOREA = 'KOR'
    USA = 'USA'
    EUROPE = 'EUR'
    CHINA = 'CHN'
    COUNTRY_CHOICES = (
        (KOREA, 'Korea'),
        (USA, 'United States'),
        (EUROPE, 'Europe'),
        (CHINA, 'China'),
    )
    segment_country = models.CharField(
        max_length = 3,
        choices = COUNTRY_CHOICES,
        default = KOREA,
    )

    def __str__(self):
        return self.segment_country

class StockMarketItem(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    investment_segment = models.ForeignKey(SMSegment, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profit = models.PositiveIntegerField(blank=True, null=True)
    portion = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.CharField(max_length=450)
    comment_before = models.TextField(blank=True)
    comment_during = models.TextField(blank=True, null=True)
    comment_after = models.TextField(blank=True, null=True)
    chosen = models.BooleanField(blank=True)

    def __str__(self):
        return self.name

class RealEstateItem(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    investment_segment = models.ForeignKey(RESegment, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    portion = models.DecimalField(max_digits=3, decimal_places=0)
    description = models.CharField(max_length=450)
    comment = models.TextField()
    chosen = models.BooleanField()

    def __str__(self):
        return self.name
