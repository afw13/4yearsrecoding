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
                entry = DatasetEntry(
                    date=timezone.datetime.strptime(row['Date'], '%m/%d/%Y').date(),
                    notes=row['NOTES'],
                    moca=row['MOCA'],
                    exercise=row['EXERCISE'],
                    b=row['B'],
                    biosense=row['BIOSENSE'],
                    breakfast_ace=row['BREAKFAST ACE'],
                    lunch_ace=row['LUNCH ACE'],
                    dinner_ace=row['DINNER ACE'],
                    meals=row['MEALS'],
                    breakfast=row['BREAKFAST'],
                    lunch=row['LUNCH'],
                    dinner=row['DINNER'],
                    supplements=row['SUPPLEMENTS'],
                    omega_3=row['OMEGA 3'],
                    iron=row['IRON'],
                    b1=row['B1'],
                    d=row['D'],
                    synapsin=row['SYNAPSIN'],
                    hormones=row['HORMONES'],
                    thyroid=row['THYROID'],
                    estradiol=row['ESTRADIOL'],
                    progesterone=row['PROGESTERONE'],
                    mycotoxin_binders=row['MYCOTOXIN BINDERS'],
                    sac_b=row['SAC B'],
                    nac=row['NAC'],
                    charcoal=row['CHARCOAL'],
                    bentonite_clay=row['BENTONITE CLAY'],
                    optifibre=row['OPTIFIBRE'],
                    interfase_plus=row['INTERFASE PLUS'],
                    welchol=row['WELCHOL'],
                    itraconazole=row['ITRACONAZOLE'],
                    nystain_oral=row['NYSTAIN ORAL'],
                    nystatin_nasal=row['NYSTATIN NASAL'],
                    medication=row['MEDICATION'],
                    code_gg=row['CODE GG'],
                    code_mm=row['CODE MM'],
                    code_zz=row['CODE ZZ'],
                    code_ss=row['CODE SS'],
                    fsm_protocol=row['FSM PROTOCOL'],
                )
                entry.save()

        self.stdout.write(self.style.SUCCESS('Dataset imported successfully'))