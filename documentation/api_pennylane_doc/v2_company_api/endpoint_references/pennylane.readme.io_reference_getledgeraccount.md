---
url: "https://pennylane.readme.io/reference/getledgeraccount"
title: "Get a ledger account"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

integer

required

Ledger Account ID

# `` 200      Returns the ledger account

object

id

integer

required

number

string

required

label

string

required

vat\_rate

string

required

Ledger Account's VAT rate in percentage

country\_alpha2

string

required

Ledger Account's country code (alpha2)

enabled

boolean

required

# `` 400      Bad request

object

object

object

object

object

object

# `` 401      Access token is missing or invalid

object

error

string

required

status

integer

required

# `` 403      Access to this resource forbidden

object

error

string

required

status

integer

required

# `` 404      The resource was not found

object

error

string

required

status

integer

required

Updated 4 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/ledger_accounts/id \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx



1

{

2  "id": 124,

3  "number": "512",

4  "label": "Secondary Account",

5  "vat_rate": "any",

6  "country_alpha2": "FR",

7  "enabled": true

8}

```

Updated 4 months ago

* * *