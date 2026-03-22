#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: info_serveur
short_description: Collecte des informations de base sur un serveur
version_added: "1.0.0"
description:
  - Ce module collecte des informations système basiques.
  - Il retourne le nom d'hôte, le nombre de CPU et la mémoire disponible.
  - Utile pour générer des rapports d'inventaire.
options:
  afficher_memoire:
    description:
      - Si true, inclut les informations de mémoire dans le résultat.
    required: false
    type: bool
    default: true
  afficher_disque:
    description:
      - Si true, inclut les informations de disque dans le résultat.
    required: false
    type: bool
    default: false
author:
  - Votre Nom (@votre_github)
'''

EXAMPLES = r'''
- name: Collecter les informations du serveur
  infracloud.utils.info_serveur:

- name: Collecter sans les informations mémoire
  infracloud.utils.info_serveur:
    afficher_memoire: false

- name: Collecter avec les informations disque
  infracloud.utils.info_serveur:
    afficher_disque: true
'''

RETURN = r'''
hostname:
  description: Le nom d'hôte du serveur
  type: str
  returned: always
cpu_count:
  description: Le nombre de processeurs
  type: int
  returned: always
memoire_totale_mo:
  description: La mémoire totale en Mo
  type: int
  returned: when afficher_memoire is true
disque_racine_go:
  description: Espace disque de la partition racine en Go
  type: float
  returned: when afficher_disque is true
'''

import platform
import os
from ansible.module_utils.basic import AnsibleModule

def get_memoire_totale():
    """Retourne la mémoire totale en Mo"""
    try:
        with open('/proc/meminfo', 'r') as f:
            for ligne in f:
                if ligne.startswith('MemTotal'):
                    # Format: MemTotal: 1234567 kB
                    parts = ligne.split()
                    if len(parts) >= 2:
                        kb = int(parts[1])
                        return kb // 1024
        return -1
    except (IOError, IndexError, ValueError):
        return -1

def get_espace_disque():
    """Retourne l'espace disque de / en Go"""
    try:
        stat = os.statvfs('/')
        # f_blocks * f_frsize = taille totale en octets
        total_go = (stat.f_blocks * stat.f_frsize) / (1024 ** 3)
        return round(total_go, 2)
    except (OSError, AttributeError):
        return -1.0

def run_module():
    module_args = dict(
        afficher_memoire=dict(type='bool', required=False, default=True),
        afficher_disque=dict(type='bool', required=False, default=False),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    resultat = dict(
        changed=False,
        hostname=platform.node(),
        cpu_count=os.cpu_count() or 1,
    )

    if module.params['afficher_memoire']:
        resultat['memoire_totale_mo'] = get_memoire_totale()

    if module.params['afficher_disque']:
        resultat['disque_racine_go'] = get_espace_disque()

    module.exit_json(**resultat)

def main():
    run_module()

if __name__ == '__main__':
    main()