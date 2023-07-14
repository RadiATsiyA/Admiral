from django.contrib import admin
from .models import Client, Agent, AgentFeedback, User

admin.site.register(AgentFeedback)
admin.site.register(Client)
admin.site.register(Agent)
admin.site.register(User)

