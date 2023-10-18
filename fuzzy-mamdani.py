"""""""""Kita akan menggunakan contoh kasus sederhana tentang sistem kendali air conditioner berdasarkan 
suhu dan kelembaban ruangan. Tujuan kita adalah mengatur tingkat kekuatan air conditioner berdasarkan kondisi 
şuhu dan kelembaban yang diberikan.
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variabel input
suhu = ctrl.Antecedent(np.arange(0,41,1), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0,101,1), 'kelembaban')

#variabel output
kekuatan = ctrl.Consequent(np.arange(0,101,1), 'kekuatan')

#fungsi keanggotaan
suhu['dingin'] = fuzz.trimf(suhu.universe,[0,0,20])
suhu['normal'] = fuzz.trimf(suhu.universe,[20,50,70])
suhu['panas'] = fuzz.trimf(suhu.universe,[20,40,40])

kelembaban['rendah']= fuzz.trimf(kelembaban.universe,[0,0,40])
kelembaban['normal']= fuzz.trimf(kelembaban.universe,[10,20,30])
kelembaban['tinggi']= fuzz.trimf(kelembaban.universe,[20,40,40])

kekuatan['rendah']= fuzz.trimf(kekuatan.universe,[0,0,60])
kekuatan['sedang']= fuzz.trimf(kekuatan.universe,[40,70,100])
kekuatan['tinggi']= fuzz.trimf(kekuatan.universe,[70,100,100])

#rule evaluation
rule1 = ctrl.Rule(suhu['normal'],kekuatan['sedang'])
rule2 = ctrl.Rule(suhu['panas']|kelembaban ['tinggi'],kekuatan['tinggi'])
rule3 = ctrl.Rule(suhu['dingin']|kelembaban['rendah'],kekuatan['rendah'])

#membuat sistem kendali fuzzy
sistem_kendali = ctrl.ControlSystem([rule1,rule2,rule3])
kendali_ac = ctrl.ControlSystemSimulation(sistem_kendali)

#mengatur input
kendali_ac.input['suhu'] = 25
kendali_ac.input['kelembaban'] = 70

#perhitungan
kendali_ac.compute()

#ambil output
print('tingkat kekuatan ac:', kendali_ac.output['kekuatan'])