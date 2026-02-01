# 🚀 Guide de démarrage rapide - MCP Pennylane

## ✅ État du développement

Le serveur MCP Pennylane est maintenant **100% fonctionnel** avec :
- ✅ 85 outils implémentés couvrant toute l'API Pennylane v2
- ✅ Connexion API testée et fonctionnelle
- ✅ Environnement virtuel configuré
- ✅ Toutes les dépendances installées

## 🧪 Tester le serveur

### 1. Vérifier que tout fonctionne

```bash
# Activer l'environnement virtuel
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Tester le serveur
python test_server.py
```

Vous devriez voir :
- La liste des 85 outils disponibles
- Une connexion API réussie
- Un test d'appel d'outil fonctionnel

### 2. Exécuter des exemples

```bash
# Lancer des exemples d'utilisation
python examples.py
```

## 🚀 Utiliser le serveur

### Avec Claude Desktop

1. Lancer le serveur :
```bash
python run_server.py
# ou directement
python src/server.py
```

2. Configurer Claude Desktop (voir instructions complètes dans le README)

### En mode développement/test

```python
import asyncio
from fastmcp import Client
from src.server import mcp

async def use_pennylane():
    client = Client(mcp)
    async with client:
        # Lister les clients
        result = await client.call_tool("pennylane_customers_list", {"limit": 10})
        print(result[0].text)
        
        # Créer une facture
        result = await client.call_tool("pennylane_invoices_create", {
            "customer_id": 123,
            "invoice_lines": [{"product_id": 1, "quantity": 2}],
            "draft": True
        })
        print(result[0].text)

asyncio.run(use_pennylane())
```

## 📝 Outils disponibles par catégorie

- **Clients** (6 outils) : Gestion des clients entreprises et particuliers
- **Factures** (14 outils) : Création, modification, envoi de factures
- **Produits** (4 outils) : Gestion du catalogue produits
- **Comptabilité** (19 outils) : Écritures, journaux, balance
- **Transactions** (8 outils) : Rapprochement bancaire
- **Fournisseurs** (11 outils) : Fournisseurs et factures d'achat
- **Et plus encore...**

## 1. Installation rapide

```bash
# Cloner le projet
git clone https://github.com/yourusername/mcp-pennylane-company.git
cd mcp-pennylane-company

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer le projet
pip install -e .
```

## 2. Configuration

```bash
# Copier le fichier d'exemple
cp env.example .env

# Éditer .env et ajouter votre clé API
# PENNYLANE_API_KEY=votre_cle_api_ici
```

## 3. Test rapide

```bash
# Définir la clé API temporairement
export PENNYLANE_API_KEY=votre_cle_api

# Lancer le serveur pour test
python src/server.py
```

## 4. Intégration Claude Desktop

Ajouter dans les paramètres Claude Desktop :

```json
{
  "mcpServers": {
    "pennylane": {
      "command": "python",
      "args": ["/chemin/absolu/vers/mcp-pennylane-company/src/server.py"],
      "env": {
        "PENNYLANE_API_KEY": "votre_cle_api"
      }
    }
  }
}
```

## 5. Exemples d'utilisation

### Avec Claude Desktop

- "Liste mes 10 derniers clients"
- "Crée une facture de 1000€ HT pour le client ACME Corp"
- "Quel est le solde du compte 411000 ?"
- "Exporte le FEC du mois dernier"
- "Montre-moi les factures impayées"

### Avec le code Python

```python
from src.server import mcp
import asyncio

# Lister les clients
async def test():
    from src.tools.customers import pennylane_customers_list
    result = await pennylane_customers_list(limit=10)
    print(result)

asyncio.run(test())
```

## 6. Dépannage

### Erreur d'authentification
- Vérifier que la clé API est correcte dans `.env`
- Vérifier que la clé a les permissions nécessaires dans Pennylane

### Erreur de connexion
- Vérifier votre connexion internet
- Vérifier que l'API Pennylane est accessible

### Claude Desktop ne trouve pas les outils
- Redémarrer Claude Desktop après ajout de la configuration
- Vérifier le chemin absolu vers server.py
- Vérifier les logs dans la console Claude Desktop

## 7. Ressources

- [Documentation API Pennylane](https://pennylane.readme.io/)
- [Documentation MCP](https://modelcontextprotocol.io/)
- [Support Pennylane](https://help.pennylane.com/) 