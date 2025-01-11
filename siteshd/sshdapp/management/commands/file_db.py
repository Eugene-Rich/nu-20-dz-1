from django.core.management.base import BaseCommand
from sshdapp.models import Sezon, Razm, Tovost


# from blogapp.models import Poll

class Command(BaseCommand):

    def handle(self, *args, **options):

        # Заполнение сезонности

        leto = Sezon.objects.filter(name='Летняя').first()
        if leto == None:
            Sezon.objects.create(name='Летняя')
            leto = Sezon.objects.filter(name='Летняя').first()

        zima = Sezon.objects.filter(name='Зимняя').first()
        if zima == None:
            Sezon.objects.create(name='Зимняя')
            zima = Sezon.objects.filter(name='Зимняя').first()

        vses = Sezon.objects.filter(name='Всесезонная').first()
        if vses == None:
            Sezon.objects.create(name='Всесезонная')
            vses = Sezon.objects.filter(name='Всесезонная').first()

        print(leto, zima, vses)

        # Заполнение размеров и товаров с остатками

        file = open("dann.txt", "r")
        while True:
            sttf = file.readline()
            if not sttf:
                break
            print(sttf)

            if sttf[0] == '*':

                ms = sttf.split('|')

                frasm = ms[2]
                tekrazm = Razm.objects.filter(name=frasm).first()
                if tekrazm == None:
                    Razm.objects.create(name=frasm)
                    tekrazm = Razm.objects.filter(name=frasm).first()

                if ms[4] == 'шипованная':
                    ship = True
                else:
                    ship = False

                if ms[3] == 'зима':
                    sez = leto
                elif ms[3] == 'лето':
                    sez = zima
                else:
                    sez = vses

                uintov = ms[1]
                tektov = Tovost.objects.filter(uin=uintov).first()
                if tektov == None:

                    Tovost.objects.create(uin=uintov, name=ms[5], ostatok=int(ms[6]), cena=int(ms[7]), kartss=ms[8], ship=ship, razmer=tekrazm, sezonnost=sez, descriptions=ms[9])
                    tektov = Tovost.objects.filter(uin=uintov).first()

                else:

                    tektov.name=ms[5]
                    tektov.ostatok=int(ms[6])
                    tektov.cena=int(ms[7])
                    tektov.kartss=ms[8]
                    tektov.ship=ship
                    tektov.razmer=tekrazm
                    tektov.sezonnost=sez
                    tektov.descriptions=ms[9]
                    tektov.save()

            else:

                if tektov != None:

                    descr = tektov.descriptions;
                    descr = descr + sttf.replace('|', '')
                    tektov.descriptions=descr
                    tektov.save()

        if tektov != None:

             descr = tektov.descriptions;
             descr = descr + sttf.replace('|', '')
             tektov.descriptions=descr
             tektov.save()


        file.close()

