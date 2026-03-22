# k3d-deploy

Rôle Ansible (Exercice 34) pour déployer un cluster **k3d** et une application **Nginx** (ConfigMap + Deployment + Service NodePort). Conçu pour être exécuté **dans le conteneur Ansible** (`hosts: client1`).

## Structure du rôle

```
.
├── defaults/main.yml   # Variables (nom du cluster, node port, texte page)
├── tasks/main.yml      # Tâches (kubectl, k3d, cluster, manifest, apply)
├── templates/          # Manifest Kubernetes (Nginx)
│   └── nginx.yaml.j2
├── meta/main.yml       # Métadonnées (Galaxy, plateformes, tags)
├── k3d-role-test.yaml  # Exemple d’utilisation du rôle
└── README.md
```

## Variables (defaults)

| Variable             | Défaut                                                  | Description               |
| -------------------- | ------------------------------------------------------- | ------------------------- |
| `k3d_cluster_name`   | `k3d-lab`                                               | Nom du cluster k3d        |
| `k3d_node_port`      | `30080`                                                 | NodePort du service Nginx |
| `k3d_nginx_title`    | `Bienvenue dans le k3d LAB déployé via un rôle ansible` | Titre de la page HTML     |
| `k3d_nginx_subtitle` | `Deploye automatiquement avec Ansible !`                | Sous-titre                |

## Installation

```bash
git clone https://github.com/Naen15/k3d-deploy
cd projet/k3d-deploy
```

## Utilisation

**Depuis la racine du repo (conteneur Ansible recommandé) :**

```bash
cd projet
ansible-playbook playboos/k3d-role-test.yaml
```

**Avec variables :**

```yaml
- hosts: client1
  connection: local
  gather_facts: false
  roles:
    - role: .
  vars:
    k3d_cluster_name: "mon-cluster"
    k3d_node_port: 30081
```

**Installation via Galaxy (si publié) :**

```bash
ansible-galaxy role install Naen15.k3d-deploy
```

Puis dans un playbook : `roles: [ansible-galaxy role install Naen15.k3d-deploy]`.

## Prérequis

- Conteneur ou machine avec **Docker** et socket monté (`/var/run/docker.sock`) pour k3d.
- utilisé le docker de la machine locale
- Linux (k3d/kubectl en binaire Linux).

L’application est accessible sur **http://localhost:30080** (ou le `k3d_node_port` choisi).
