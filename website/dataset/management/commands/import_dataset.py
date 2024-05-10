from django.core.management.base import BaseCommand
from django.utils import timezone
from dataset.models import DatasetEntry
import csv

class Command(BaseCommand):
    help = 'Imports dataset from a CSV file'

    def handle(self, *args, **options):
        with open('/Users/anniewhite 1/Programming/4yearsrecoding/14day_sample.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row) 
                entry = DatasetEntry(
                    date=timezone.datetime.strptime(row['Date'], '%m/%d/%Y').date(),
                    notes=row['NOTES'],
                    moca=row['MOCA'],
                    exercise=row.get('Exercise', ''),
                    b=row['B'],
                    biosense=row.get('BIOSENSE', ''),
                    breakfast_ace=row.get('BREAKFAST ACE', ''),  # Corrected line
                    lunch_ace=row.get('LUNCH ACE', ''),  # Add this line
                    dinner_ace=row.get('DINNER ACE', ''),
                    meals=row.get('MEALS', ''),
                    breakfast=row.get('BREAKFAST', ''),
                    lunch=row.get('LUNCH', ''),
                    dinner=row.get('DINNER', ''),
                    supplements=row.get('SUPPLEMENTS', ''),
                    omega_3=row.get('OMEGA3', ''),
                    iron=row.get('IRON', ''),
                    b1=row.get('B1', ''),
                    d=row['D'],
                    synapsin=row.get('SYNAPSIN', ''),
                    hormones=row.get('HORMONES', ''),
                    thyroid=row.get('THYROID', ''),
                    estradiol=row.get('ESTRADIOL', ''),
                    progesterone=row.get('PROGESTERONE', ''),
                    mycotoxin_binders=row.get('MYCOTOXIN BINDERS', ''),
                    sac_b=row.get('SAC B', ''),
                    nac=row.get('NAC', ''),
                    charcoal=row.get('CHARCOAL', ''),
                    bentonite_clay=row.get('BENTONITE CLAY', ''),
                    optifibre=row.get('OPTIFIBRE', ''),
                    interfase_plus=row.get('INTERFASE PLUS', ''),
                    welchol=row.get('WELCHOL', ''),
                    itraconazole=row.get('ITRACONAZOLE', ''),
                    nystain_oral=row.get('NYSTAIN ORAL', ''),
                    nystatin_nasal=row.get('NYSTATIN NASAL', ''),
                    medication=row.get('MEDICATION', ''),
                    code_gg=row.get('CODE GG', ''),
                    code_mm=row.get('CODE MM', ''),
                    code_zz=row.get('CODE ZZ', ''),
                    code_ss=row.get('CODE SS', ''),
                    fsm_protocol=row.get('FSM PROTOCOL', ''),
                )
                entry.save()

        self.stdout.write(self.style.SUCCESS('Dataset imported successfully'))