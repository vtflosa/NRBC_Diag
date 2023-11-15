#!/usr/bin/python3
# -*- coding: Utf-8 -*

from definition import *
from dataclasses import dataclass


@dataclass
class Disease:
    """ dataclass to describe full disease"""
    name: str
    nrbc: NRBC
    agent: Agent
    localisation: list[Localisation]
    symptoms: list[Symptoms]
