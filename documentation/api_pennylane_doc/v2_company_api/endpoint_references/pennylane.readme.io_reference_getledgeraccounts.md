---
url: "https://pennylane.readme.io/reference/getledgeraccounts"
title: "List Ledger Accounts"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

page

integer

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

1 to 1000

Items are paginated. By default, you get 20 items per page. You can specify another number of items per page.

filter

string

You can choose to filter items on specific fields.

Available fields and values:

- `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
- `number`: `start_with`
- `enabled`: `eq`

# `` 200      Returns a list of ledger accounts

object

total\_pages

integer

required

The total number of pages available

current\_page

integer

required

The current page returned

total\_items

integer

required

The total number of items available

per\_page

integer

required

The number of items returned per page

items

array of objects

required

items\*

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

2     --url https://app.pennylane.com/api/external/v2/ledger_accounts \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

16



1

{

2  "total_pages": 5,

3  "current_page": 1,

4  "total_items": 12,

5  "per_page": 20,

6

  "items": [\
\
7\
\
    {\
\
8      "id": 124,\
\
9      "number": "512",\
\
10      "label": "Secondary Account",\
\
11      "vat_rate": "any",\
\
12      "country_alpha2": "FR",\
\
13      "enabled": true\
\
14    }\
\
15  ]

16}

```

Updated 4 months ago

* * *