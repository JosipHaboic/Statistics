import json
import xlrd
from os import chdir
from os.path import dirname, abspath
chdir(dirname(abspath(__file__)))
from pprint import pprint, pformat
from matplotlib import pyplot
from pymymath.statistics.quantitative_sample import QuantitativeSample
from pymymath.statistics.quantitative_population import QuantitativePopulation


class LottoData:

    def __init__(self, 
        kolo,
        datum,
        dobitna_kombinacija,
        zlatna_kuglica,
        slovo_za_super_7,
        dobitak,
        dobitak_super_7,
        joker,
        uplata,
        ukupno,
        uplata_super_7,
        ukupno_super_7):
        self.kolo = kolo
        self.datum = datum
        self.dobitna_kombinacija = QuantitativePopulation(dobitna_kombinacija)
        self.zlatna_kuglica = zlatna_kuglica
        self.slovo_za_super_7 = slovo_za_super_7
        self.dobitak = dobitak
        self.dobitak_super_7 = dobitak_super_7
        self.joker = joker
        self.uplata = uplata
        self.ukupno = ukupno
        self.uplata_super_7 = uplata_super_7
        self.ukupno_super_7 = ukupno_super_7

    def __repr__(self):
        return '''
        Kolo:                {}
        Datum:               {}
        Dobitna kombincaija: {}
        Zlatna kuglica:      {}
        Slovo za Super7:     {}
        Dobitak:             {} HRK
        Dobitak Super7:      {} HRK
        Joker broj:          {}
        Uplata:              {} HRK
        Ukupno:              {} HRK
        Uplata Super7:       {} HRK
        Ukupno Super7:       {} HRK '''.format(
            self.kolo,
            self.datum,
            (   
                self.dobitna_kombinacija,
                pformat(self.dobitna_kombinacija.summary)
            ),
            self.zlatna_kuglica,
            self.slovo_za_super_7,
            self.dobitak,
            self.dobitak_super_7,
            self.joker,
            self.uplata,
            self.ukupno,
            self.uplata_super_7,
            self.ukupno_super_7
        )

    


LOTO_2017 = xlrd.open_workbook('../data/Loto7od39_2017.xls').sheets()
DATA = list(LOTO_2017[0].get_rows())[1:]
del DATA[1]

LABLES = DATA[0]
del DATA[0]

LOTTO_DATA = {}
for item in DATA:
    LOTTO_DATA[item[1].value] = LottoData(
        int(item[0].value.replace('.','')),
        item[1].value,
        list(map(int,[item[2].value, item[3].value, item[4].value, item[5].value, item[6].value, item[7].value, item[8].value])),
        True if item[9].value == 'DA' else False,
        item[10].value,
        item[11].value,
        item[12].value,
        int(item[13].value),
        int(item[14].value),
        item[15].value,
        int(item[16].value),
        int(item[17].value)
    )

# for value in LOTTO_DATA.values():print(value)
for i in sorted(filter(lambda x: x.dobitak != '-',LOTTO_DATA.values()), key=lambda x:x.kolo):
    pprint(i)
