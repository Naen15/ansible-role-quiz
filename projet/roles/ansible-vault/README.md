# Déploiement Sécurisé - MonAppSecurisee (Ansible Vault)

Ce projet automatise le déploiement de l'application interne **MonAppSecurisee** sur des serveurs Linux (Ubuntu/Rocky) en utilisant **Ansible Vault** pour garantir qu'aucun secret (mots de passe, clés API, tokens) n'apparaisse en clair dans le code.

## Prérequis

Avant de lancer le déploiement, assurez-vous que le contrôleur Ansible dispose des éléments suivants :

1.  **Ansible** installé.
2.  **Bibliothèque Python `passlib`** (nécessaire pour le hachage des mots de passe utilisateurs).
    ```bash
    # Installation sur Debian/Ubuntu
    apt install python3-passlib
    # Installation sur RHEL/Rocky
    dnf install python3-passlib
    # Ou via pip (si géré)
    pip install passlib
    ```

## Structure du Projet

```text
projet/
├── playbooks/
│   └── vault-role.yaml        # Playbook principal
├── roles/
│   └── ansible-vault/
│       ├── defaults/main.yml  # Vars par défaut + pwd utilisateur chiffré (inline)
│       ├── vars/main.yml      # Vars sensibles entièrement chiffrées (DB, API)
│       ├── tasks/main.yml     # Instructions de déploiement
│       └── templates/
│           └── app_config.conf.j2 # Modèle de configuration
└── inventory.ini              # Inventaire (non inclus dans ce repo)
```
