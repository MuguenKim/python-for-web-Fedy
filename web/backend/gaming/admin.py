from django.contrib import admin
from gaming.models import Game, Gamer, Company, Genre

# Register your models here.
admin.site.register(Game)
admin.site.register(Gamer)
admin.site.register(Company)
admin.site.register(Genre)
