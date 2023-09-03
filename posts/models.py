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
    content = models.TextField()

    #True는 분실물, False는 습득물
    flag = models.BooleanField(default=True) 

    PLACES_CHOICES = (
        ("J", "J"),
        ("R", "R"),
        ("K", "K"),
        ("GA", "GA"),
        ("MA", "MA"),
        ("AS", "AS"),
        ("다산관", "다산관"),
        ("체육관", "체육관"),
        ("경제관", "경제관"),
        ("우정관", "우정관"),
        ("청년광장", "청년광장"),
        ("대운동장", "대운동장"),
        ("엠마오관", "엠마오관"),
        ("로욜라 도서관", "로욜라 도서관"),
        ("곤자가플라자", "곤자가플라자"),
    )

    TYPE_CHOICES = (
        ("전자기기", "전자기기"),
        ("화장품", "화장품"),
        ("지갑", "지갑"),
        ("의류/액세서리", "의류/액세서리"),
        ("카드/신분증", "카드/신분증"),
        ("기타", "기타"),
    )

    COLOR_CHOICES = (
        ("레드", "레드"),
        ("오렌지", "오렌지"),
        ("옐로우", "옐로우"),
        ("그린", "그린"),
        ("블루", "블루"),
        ("네이비", "네이비"),
        ("퍼플", "퍼플"),
        ("브라운", "브라운"),
        ("화이트", "화이트"),
        ("블랙", "블랙"),
        ("골드", "골드"),
        ("실버", "실버"),
        ("베이지", "베이지"),
        ("핑크", "핑크"),
        ("패턴", "패턴"),
        ("기타", "기타"),
    )

    place = MultiSelectField(max_length=100, choices=PLACES_CHOICES)
    type = MultiSelectField(max_length=100, choices=TYPE_CHOICES)
    color = MultiSelectField(max_length=100, choices=COLOR_CHOICES)
