# Export file of Analytical General Ledger

**POST**
`https://app.pennylane.com/api/external/firm/v1/companies/{company_id}/exports/analytical_general_ledgers`

---

## Description
Cet endpoint permet de générer un export du Grand Livre Analytique (Analytical General Ledger) pour une société donnée. Le fichier généré est au format `.xlsx` et utilise le mode analytique en ligne par défaut.

---

## Authentification
- **Type** : OAuth2 (Bearer Token)
- **Scope requis** : `exports:agl`

---

## Paramètres

### Path parameter
- `company_id` (integer, requis) : Identifiant de la société existante

### Body parameters
- `period_start` (date, requis) : Date de début de la période à exporter
- `period_end` (date, requis) : Date de fin de la période à exporter
- `mode` (string, optionnel) : Mode d'export, valeurs possibles : `in_line` (défaut) ou `in_column`

---

## Exemple de requête

```bash
curl --request POST \
     --url https://app.pennylane.com/api/external/firm/v1/companies/{company_id}/exports/analytical_general_ledgers \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer <votre_token>' \
     --data '{
       "period_start": "2023-01-01",
       "period_end": "2023-12-31",
       "mode": "in_line"
     }'
```

---

## Réponses

### 201 - Succès
- Retourne un objet avec l'état de l'export généré :
  - `id` (integer) : ID de l'export
  - `status` (string) : État de l'export (`pending`, `ready`, `error`)
  - `created_at` (date-time)
  - `updated_at` (date-time)

### 400 - Mauvaise requête
### 401 - Token d'accès manquant ou invalide
### 403 - Accès interdit à cette ressource
### 404 - Ressource non trouvée

Chaque erreur retourne un objet avec :
- `error` (string)
- `status` (integer)

---

**Documentation d'origine :** [Pennylane API - Export file of Analytical General Ledger](https://firm-pennylane.readme.io/reference/postanalyticalgeneralledgerexport-1)
