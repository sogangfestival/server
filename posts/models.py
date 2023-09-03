from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    password = models.IntegerField(null = True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)

    #True는 분실물, False는 습득물
    flag = models.BooleanField(default=True) 

    PLACES_CHOICES = (
        (0, "J관"),
        (1, "R관"),
        (2, "K관"),
        (3, "GA관"),
        (4, "MA관"),
        (5, "AS관"),
        (6, "다산관"),
        (7, "체육관"),
        (8, "경제관"),
        (9, "우정관"),
        (10, "청년광장"),
        (11, "대운동장"),
        (12, "엠마오관"),
        (13, "로욜라 도서관"),
        (14, "곤자가플라자"),
    )

    TYPE_CHOICES = (
        (0, "전자기기"),
        (1, "화장품"),
        (2, "지갑"),
        (3, "의류/액세서리"),
        (4, "카드/신분증"),
        (5, "기타"),
    )

    COLOR_CHOICES = (
        (0, "레드"),
        (1, "오렌지"),
        (2, "옐로우"),
        (3, "그린"),
        (4, "블루"),
        (5, "네이비"),
        (6, "퍼플"),
        (7, "브라운"),
        (8, "화이트"),
        (9, "블랙"),
        (10, "골드"),
        (11, "실버"),
        (12, "베이지"),
        (13, "핑크"),
        (14, "패턴"),
        (15, "기타"),
    )

    place = MultiSelectField(max_length=100, choices=PLACES_CHOICES)
    type = MultiSelectField(max_length=100, choices=TYPE_CHOICES)
    color = MultiSelectField(max_length=100, choices=COLOR_CHOICES)