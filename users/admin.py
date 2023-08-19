from django.contrib import admin
from .models import Agent, AgentFeedback, User, Specialization

admin.site.register(AgentFeedback)
admin.site.register(Specialization)
admin.site.register(Agent)
admin.site.register(User)

