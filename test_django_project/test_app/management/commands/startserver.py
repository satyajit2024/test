# custom_commands/management/commands/startserver.py
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Call the function you want to execute when the server starts
        # For example:
        self.startup_function()

    def startup_function(self):
        # Your startup function logic here
        print("Server is starting. Execute startup tasks here.")
