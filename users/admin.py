from django.contrib import admin
from .models import Agent, AgentFeedback, User

admin.site.register(AgentFeedback)
admin.site.register(Agent)
admin.site.register(User)

