import json
import os
from django.core.management.base import BaseCommand
from invapp.models import Tuote

class Command(BaseCommand):
    help = 'Load tuotteet from koodit.json into the database'

    def handle(self, *args, **options):
        
        polku = 'demo\\invapp\\management\\commands\\koodit.json'
        with open(polku, 'r', encoding='utf-8') as file:
            tuotteet_data = json.load(file)
        try:
            for tuote_data in tuotteet_data:
                if len(tuote_data['text']) > 100:
                    tuote_data['text'] = tuote_data['text'][:100]
                obj, created = Tuote.objects.update_or_create(
                    ean_koodi=tuote_data['ean'],
                    defaults={
                        'nimi': tuote_data['text'],
                        'kuva': tuote_data['photo'],
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created Tuote: {obj.ean_koodi} - {obj.nimi}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Updated Tuote: {obj.ean_koodi} - {obj.nimi}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error occurred: {e}'))

        self.stdout.write(self.style.SUCCESS('Successfully loaded tuotteet into the database'))