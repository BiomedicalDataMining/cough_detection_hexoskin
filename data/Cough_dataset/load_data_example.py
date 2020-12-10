#!/usr/bin/python3

import gzip,pickle
import csv
import ast


#la lecture du disctionnaire
pkl_raw='data_raw.pkl.zip'
with gzip.open(pkl_raw) as fp:
    datapkl_raw = pickle.load(fp)

print(type(datapkl_raw))
print(datapkl_raw.keys())
print(len(datapkl_raw))

new_dict = {}
for key,value in datapkl_raw.items():
    print(value)
    print(key)
print(new_dict)

my_dict = ast.literal_eval(datapkl_raw)
print(my_dict["id"]==137216)
#article HAR sensors
#amendement reponse de neila pour envoyer a marta
#youssef
#convertir en csv
#id x y z resp1 rep2 label
# #id: x: y: z:

# visualisation des 5 courbes pour chaque patient

#preparer un power point, des lacunes
#demander si les données envoyés sont calibrés
#On demande ECG à Hexoskin (en particulier si ils ont la fréquence cardiaque)
#mariem et amal
#literature review on cough detection using time series data(ecg, acceleration, cardiac frequency, respiratory data, audio voice)
#revue systematique
#soumet une conference en mars (pre-resultats), soumet revue systematique
#Time : 1 2 3 4 5 6 7 8 9
#             X
#             |--1s--|
#             XXXXXXXX
#         |--1s--|
#         XXXXXXXX




#est ce que tu veux quand organiser une reunion avant les vacances (15mn): amendement, on travaille sur le code, on pose des questions sur les donnees, partage du code

#mariem et amal
# analyse statistiques

#tester avec le code du HAR (input csv)

#tensor dimension 5


#import ipdb
#ipdb.set_trace()



