# MCP Pennylane Company

Un serveur Model Context Protocol (MCP) pour interagir avec l'API Pennylane v2, permettant aux LLMs d'accéder et de gérer les données comptables via MCP.

## 🚀 Fonctionnalités

Ce serveur MCP expose l'ensemble des endpoints de l'API Pennylane v2, organisés en modules. **85 outils disponibles** couvrant :

### 📊 Comptabilité (`accounting`)
- Gestion des journaux comptables
- Plan comptable (comptes du grand livre)
- Écritures comptables et lignes d'écriture
- Lettrage/délettrage
- Balance générale
- Exports FEC et Grand Livre Analytique
- Années fiscales

### 👥 Clients (`customers`)
- CRUD clients entreprises et particuliers
- Recherche et filtrage avancés
- Gestion des informations de facturation

### 💰 Factures clients (`invoices`)
- Création et gestion des factures
- Finalisation et envoi par email
- Import de factures depuis fichiers
- Gestion des avoirs
- Modèles de factures

### 📦 Produits (`products`)
- Catalogue produits/services
- Gestion des prix et TVA

### 🏢 Fournisseurs (`suppliers`)
- CRUD fournisseurs
- Factures fournisseurs
- Import de factures
- Suivi des paiements

### 🏦 Transactions bancaires (`transactions`)
- Liste des comptes bancaires
- Transactions et rapprochement
- Matching avec factures

### 📈 Analytique (`analytics`)
- Catégories analytiques
- Groupes de catégories
- Affectation aux factures et écritures

### 📎 Fichiers (`files`)
- Upload de pièces jointes
- Annexes de factures
- Pièces comptables

### 📝 Divers (`misc`)
- Profil utilisateur
- Journaux de modifications (changelogs)

## 📋 Prérequis

- Python 3.11+
- Compte Pennylane avec accès API
- Clé API Pennylane (ou OAuth pour les partenaires)

## 🛠️ Installation

1. Cloner le repository :
```bash
git clone https://github.com/yourusername/mcp-pennylane-company.git
cd mcp-pennylane-company
```

2. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installer les dépendances :
```bash
pip install -e .
```

## ⚙️ Configuration

1. Copier le fichier d'exemple :
```bash
cp .env.example .env
```

2. Éditer `.env` avec vos informations :
```env
# Authentification API
PENNYLANE_API_KEY=votre_cle_api_pennylane

# URL de l'API (optionnel, utilise la prod par défaut)
PENNYLANE_BASE_URL=https://app.pennylane.com/api/external/v2

# Configuration serveur (optionnel)
PENNYLANE_LOG_LEVEL=INFO
```

### Obtenir une clé API

1. Connectez-vous à votre compte Pennylane
2. Allez dans Paramètres > API
3. Générez une nouvelle clé API
4. Copiez la clé dans votre fichier `.env`

## 🚀 Utilisation

### Avec Claude Desktop

1. Ajouter la configuration dans Claude Desktop :

```json
{
  "mcpServers": {
    "pennylane": {
      "command": "python",
      "args": ["/chemin/vers/mcp-pennylane-company/src/server.py"],
      "env": {
        "PENNYLANE_API_KEY": "votre_cle_api"
      }
    }
  }
}
```

2. Redémarrer Claude Desktop

3. Utiliser les outils Pennylane dans vos conversations :
   - "Liste mes clients"
   - "Crée une facture pour le client X"
   - "Quel est le solde du compte 411000 ?"
   - etc.

### En ligne de commande (test)

⚠️ **Important** : N'utilisez PAS `mcp dev` - il n'est pas compatible avec FastMCP.

```bash
# Activer l'environnement virtuel
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Définir la variable d'environnement (ou utiliser le fichier .env)
export PENNYLANE_API_KEY=votre_cle_api

# Lancer le serveur
python src/server.py
```

Pour tester le serveur, utilisez l'un des scripts de test :
- `python test_mcp_proper.py` - Test complet avec séquence d'initialisation
- `python test_interactive.py` - Mode interactif
- `python test_list_all_tools.py` - Liste tous les outils disponibles

Pour plus de détails sur le démarrage du serveur, consultez [START_SERVER.md](START_SERVER.md) et [TEST_SERVER.md](TEST_SERVER.md).

## 📚 Liste des outils disponibles

### Clients
- `pennylane_customers_list` - Lister les clients
- `pennylane_customers_get` - Obtenir un client
- `pennylane_customers_create_company` - Créer un client entreprise
- `pennylane_customers_create_individual` - Créer un client particulier
- `pennylane_customers_update_company` - Mettre à jour un client entreprise
- `pennylane_customers_update_individual` - Mettre à jour un client particulier

### Factures
- `pennylane_invoices_list` - Lister les factures
- `pennylane_invoices_get` - Obtenir une facture
- `pennylane_invoices_create` - Créer une facture
- `pennylane_invoices_update` - Modifier un brouillon
- `pennylane_invoices_finalize` - Finaliser une facture
- `pennylane_invoices_send_email` - Envoyer par email
- `pennylane_invoices_mark_paid` - Marquer comme payée
- `pennylane_invoices_delete` - Supprimer un brouillon
- `pennylane_invoices_import` - Importer depuis fichier

### Comptabilité
- `pennylane_ledger_accounts_list` - Plan comptable
- `pennylane_ledger_entries_create` - Créer une écriture
- `pennylane_trial_balance_get` - Obtenir la balance
- `pennylane_export_fec_create` - Export FEC

(Et bien d'autres... voir la documentation complète)

## 🧪 Tests

```bash
# Installer les dépendances de développement
pip install -e ".[dev]"

# Lancer les tests
pytest

# Avec couverture
pytest --cov=src
```

## 🔧 Développement

### Structure du projet

```
mcp-pennylane-company/
├── src/
│   ├── server.py          # Serveur FastMCP principal
│   ├── config.py          # Configuration
│   ├── tools/             # Modules d'outils MCP
│   │   ├── accounting.py  # Outils comptables
│   │   ├── customers.py   # Gestion clients
│   │   ├── invoices.py    # Factures clients
│   │   └── ...
│   └── utils/
│       └── api_client.py  # Client HTTP pour l'API
├── tests/                 # Tests unitaires
├── pyproject.toml         # Configuration Python
└── README.md
```

### Ajouter un nouvel endpoint

1. Identifier le module approprié dans `src/tools/`
2. Ajouter une fonction décorée avec `@mcp.tool()`
3. Documenter les paramètres avec Pydantic Field
4. Gérer les erreurs avec try/except
5. Tester la nouvelle fonctionnalité

## 📝 Licence

MIT

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Soumettre des pull requests

## 📞 Support

- Documentation API Pennylane : https://pennylane.readme.io/
- Documentation MCP : https://modelcontextprotocol.io/
- Issues : https://github.com/yourusername/mcp-pennylane-company/issues 