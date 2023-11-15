#!/usr/bin/python3
# -*- coding: Utf-8 -*
""" This program is aimed to help emergency services to diagnose an NRBC disease from symptoms in a patient"""
from classes import *


def main():
    disease = Disease("Intoxication à la javel", NRBC.CHIMIQUE, Agent.JAVEL,
                      [Localisation.TETE, Localisation.BOUCHE, Localisation.DIGESTIF],
                      [Symptoms.NAUSEE, Symptoms.VOMISSEMENT, Symptoms.BRULURE, Symptoms.ROUGEUR])


    print("votre patient a des troubles digestifs avec vomissements ? OUI")
    print("votre patient à des brulures à la langue? OUI")
    print("votre patient à des céphalées? OUI")
    print()
    print(f"votre patient est atteint de : {disease.name}")

    print("\nles symptomes les plus fréquents sont :")
    for s in disease.symptoms:
        print(f"{s.name} ", end="")

    print("\nLes localisations principales sont : ")
    for l in disease.localisation:
        print(f"{l.name}")

if __name__ == '__main__':
    main()
