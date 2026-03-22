# Collection Ansible : naen_bah.drupal

Cette collection Ansible permet de déployer le CMS Drupal de manière entièrement automatisée et idempotente. Elle est conçue pour fonctionner sur des environnements conteneurisés basés sur **Ubuntu (famille Debian)** et **Rocky Linux (famille RedHat)**.

## Fonctionnalités

- Installation des prérequis (Serveur Web Apache, PHP, MariaDB).
- Configuration dynamique selon le système d'exploitation cible (APT vs DNF).
- Prise en charge spécifique des environnements Docker (contournement de l'absence de `systemd` pour les services).
- Création de la base de données et de l'utilisateur MariaDB.
- Téléchargement, extraction et configuration des droits pour Drupal.

## Prérequis

- Ansible 2.9 ou supérieur.
- Accès privilégié (`become: yes`) sur les machines cibles.
- Dépendance requise (Collection MySQL communautaire) à installer sur le nœud de contrôle :
  ```bash
  ansible-galaxy collection install community.mysql
  ```
