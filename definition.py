#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""This file is aimed to contain definitions of disease and symptomes"""
from enum import Enum

class Symptoms(Enum):
    """ Possible symptomes of diseases"""
    ROUGEUR = "ROUGEUR"
    NAUSEE = "NAUSEE"
    VOMISSEMENT = "VOMISSEMENT"
    EVANOUISSEMENT = "EVANOUISSEMENT"
    ARRET_CARDIAQUE = "ARRET_CARDIAQUE"
    ARYTHMIE = "ARYTHMIE"
    BLOC_AV = "BLOC_AV"
    BRULURE = "BRULURE"


class Localisation(Enum):
    """ Possible localisation of symptoms"""
    TETE = "TETE"
    MEMBRE_SUPERIEUR = "MEMBRE_SUPERIEUR"
    MEMBRE_INFERIEUR = "MEMBRE_INFERIEUR"
    POUMONS = "POUMONS"
    COEUR = "COEUR"
    DIGESTIF = "DIGESTIF"
    BOUCHE = "BOUCHE"


class NRBC(Enum):
    NUCLEAIRE = "NUCLEAIRE"
    RADIOLOGIQUE = "RADIOLOGIQUE"
    BIOLOGIQUE = "BIOLOGIQUE"
    CHIMIQUE = "CHIMIQUE"


class Agent(Enum):
    """ Possible NRBC agents"""
    VIRUS = "VIRUS"
    BACTERIE = "BACTERIE"
    PARASITE = "PARASITE"
    CHAMPIGNON = "CHAMPIGNON"
    RADIOACTIF = "RADIOACTIF"
    ACIDE = "ACIDE"
    JAVEL = "JAVEL"





