from django.db import models
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
PLACES_CHOICES = (
    ("j", "정하상관"),
    ("r", "리치과학관"),
    ("k", "김대건관"),
    ("ga", "가브리엘관"),
    ("ma", "마태오"),
    ("as", "아담샬관"),
    ("d", "다산관"),
    ("gym", "체육관"),
    ("gn", "경제관"),
    ("bw", "우정관"),
    ("square", "청년광장"),
    ("play", "대운동장"),
    ("e", "엠마오관"),
    ("loyola", "로욜라 도서관"),
    ("plaza", "곤자가플라자"),
)

TYPE_CHOICES = (
    ("electricity", "전자기기"),
    ("cosmetic", "화장품"),
    ("wallet", "지갑"),
    ("cloth", "의류"),
    ("accessory", "액세서리"),
    ("card", "카드/신분증"),
    ("etc", "기타"),
)

COLOR_CHOICES = (
    ("red", "빨강"),
    ("orange", "주황"),
    ("yellow", "노랑"),
    ("green", "초록"),
    ("blue", "파랑"),
    ("navy", "남색"),
    ("purple", "보라"),
    ("brown", "갈색"),
    ("white", "흰색"),
    ("black", "검정"),
    ("gold", "금색"),
    ("silver", "은색"),
    ("beige", "베이지"),
    ("pink", "분홍"),
    ("pattern", "패턴"),
    ("etc", "기타"),
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    password = models.IntegerField(null = True)
    image1 = models.ImageField(null=True, blank=True, upload_to ='img_files/')
    image2 = models.ImageField(null=True, blank=True,upload_to ='img_files/')
    image3 = models.ImageField(null=True, blank=True,upload_to ='img_files/')
    image4 = models.ImageField(null=True, blank=True,upload_to ='img_files/')
    image5 = models.ImageField(null=True, blank=True,upload_to ='img_files/')
    created_at = models.DateField(auto_now_add=True)
    content = models.TextField()

    #True는 분실물, False는 습득물
    flag = models.BooleanField(default=True) 

    
    place = MultiSelectField(max_length=100, choices=PLACES_CHOICES)
    type = MultiSelectField(max_length=100, choices=TYPE_CHOICES)
    color = MultiSelectField(max_length=100, choices=COLOR_CHOICES)
    
    def __str__(self):
        return self.title
