# Ansible Role: Quiz Ansible

Un rôle Ansible complet pour déployer automatiquement l'application Node.js **quiz-ansible** sur des serveurs Linux.

Ce rôle est conçu pour être **portable** et fonctionne indifféremment sur :

- **Debian / Ubuntu**
- **RedHat / Rocky Linux** (CentOS, AlmaLinux...)

## Fonctionnalités

- ✅ Installation des pré-requis (Git, Curl).
- ✅ Installation automatique de **Node.js** (via NodeSource, compatible RPM & DEB).
- ✅ Clonage du code source depuis GitLab.
- ✅ Installation des dépendances (`npm install`) et compilation (`npm run build`).
- ✅ Installation du serveur web léger `serve`.
- ✅ Lancement de l'application en tâche de fond (persistant).

## Variables du Rôle

Les variables suivantes sont définies dans `defaults/main.yml` et peuvent être surchargées :

| Variable         | Valeur par défaut                                     | Description                              |
| ---------------- | ----------------------------------------------------- | ---------------------------------------- |
| `nodejs_version` | `"23.x"`                                              | Version de Node.js à installer.          |
| `app_repo`       | `https://gitlab.com/ftutorials-labs/quiz-ansible.git` | URL du dépôt Git de l'application.       |
| `app_dest`       | `/opt/quiz-ansible`                                   | Dossier de destination sur le serveur.   |
| `app_build_dir`  | `dist`                                                | Dossier généré contenant l'app compilée. |
| `app_port`       | `3000`                                                | Port d'écoute de l'application.          |

## Pré-requis

- Ansible 2.9+
- Une connexion Internet sur les machines cibles (pour télécharger Node.js et les paquets).

## Exemple de Playbook

Voici comment utiliser ce rôle dans vos projets :

```yaml
---
- name: Déployer l'application Quiz
  hosts: all
  become: yes

  roles:
    - role: ansible-role-quiz
      vars:
        app_port: 8080 # Exemple : changer le port par défaut
```
