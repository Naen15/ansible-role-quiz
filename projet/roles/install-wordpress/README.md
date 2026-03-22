# Ansible Role: WordPress conteneurisé

Déploie WordPress et MariaDB sur des environnements Linux (Ubuntu/Rocky) sans Systemd (type Docker).

## Requirements

- Python 3 et `python3-pymysql`.
- Un conteneur cible accessible via SSH ou connexion locale.

## Role Variables

Variables disponibles dans `defaults/main.yml`:

- `wp_db_name`: Nom de la base (defaut: wordpress)
- `wp_db_user`: Utilisateur DB (defaut: example)
- `wp_db_password`: Mot de passe DB
- `wp_install_dir`: Dossier d'installation (defaut: /var/www/html)

## Example Playbook

```yaml
- hosts: all
  become: yes
  roles:
    - my_wordpress_role
```
