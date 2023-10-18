"""Kita akan menggunakan contoh kasus pengambilan keputusan investasi berdasarkan faktor keuntungan dan risiko.
Tujuan kita adalah menghitung tingkat keputusan investasi berdasarkan nilai keuntungan dan risiko yang diberikan."""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#variabel input
keuntungan = ctrl.Antecedent(np.arange(0,1.1,0.1), 'keuntungan')
resiko = ctrl.Antecedent(np.arange(0,1.1,0.1), 'resiko')

#variabel output
keputusan = ctrl.Consequent(np.arange(0,1.1,0.1), 'keputusan')

#fungsi keangotaan

keuntungan['rendah'] = fuzz.trimf(keuntungan.universe, [0,0,0.5])
keuntungan['sedang'] = fuzz.trimf(keuntungan.universe, [0,0.5,1])
keuntungan['tinggi'] = fuzz.trimf(keuntungan.universe, [0.5,1,1])

resiko['rendah']= fuzz.trimf(resiko.universe, [0,0,0.5])
resiko['sedang']= fuzz.trimf(resiko.universe, [0,0.5,1])
resiko['tinggi']= fuzz.trimf(resiko.universe, [0.5,1,1])

keputusan['rendah']= fuzz.trimf(keputusan.universe,[0,0,0.5])
keputusan['sedang']= fuzz.trimf(keputusan.universe,[0,0.5,1])
keputusan['tinggi']= fuzz.trimf(keputusan.universe,[0.5,1,1])

#rule evaluation
rule1 = ctrl.Rule(keuntungan['rendah'] & resiko['rendah'], keputusan['rendah'] )
rule2 = ctrl.Rule((keuntungan['tinggi']|resiko['sedang']), keputusan['sedang'])
rule3 = ctrl.Rule((keuntungan['sedang']|resiko['sedang']), keputusan['tinggi'])

#sistem kendali fuzzy
kendali = ctrl.ControlSystem([rule1,rule2,rule3])
investasi= ctrl.ControlSystemSimulation(kendali)

#mengatur input

investasi.input['keuntungan'] = 0.8
investasi.input['resiko'] = 0.6

#perhitungan
investasi.compute()

#output
print('tingkat keputusan investasi:', investasi.output['keputusan'] )