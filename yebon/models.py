from django.db import models 
from django.utils import timezone


class HappyThings(models.Model): 
	#모델(Object)을 정의하는 코드 / 
	# models : Post가 장고 모델임을 의미, 
	# 장고는 Post가 데이터베이스에 저장되어야 한다는 것을 알게 됨

	#글쓴이
    reporter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #날 행복하게 만드는 것들의 이름! 
    thing = models.CharField(max_length=200) 
    #설명
    desc = models.TextField() 
    #행복지수
    happinessIndex = models.IntegerField(default=0)
    #노력지수
    effortIndex = models.IntegerField(default=0)


    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def give_happiness(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.thing