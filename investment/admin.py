from django.contrib import admin
from .models import Objective, Phase, StockMarketItem, RealEstateItem, RESegment, SMSegment, Blog

admin.site.register(Objective)
admin.site.register(Phase)
admin.site.register(StockMarketItem)
admin.site.register(RealEstateItem)
admin.site.register(RESegment)
admin.site.register(SMSegment)
admin.site.register(Blog)
