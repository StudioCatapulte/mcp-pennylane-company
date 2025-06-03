---
url: "https://pennylane.readme.io/reference/getledgerentriesledgerentrylines"
title: "List ledger entry lines of a Ledger Entry"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

ledger\_entry\_id

number

required

Existing Ledger Entry (id)

page

integer

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

1 to 100

Items are paginated. By default, you get 20 items per page. You can specify another number of items per page.

filter

string

You can choose to filter items on specific fields.

Available fields : `ledger_account_id`

Available operators : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`

# `` 200      Returns Ledger Entry lines of requested Ledger Entry

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

The number of items per page

items

array of objects

required

Array of entry lines of requested Ledger Entry

items\*

object

id

integer

required

ID of the entry line

debit

string

required

Debit amount for the entry line

credit

string

required

Credit amount for the entry line

label

string

required

Label that describes the entry line

ledger\_account\_id

integer

required

Ledger account ID

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

2     --url https://app.pennylane.com/api/external/v2/ledger_entries/ledger_entry_id/ledger_entry_lines \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

15



1

{

2  "total_pages": 5,

3  "current_page": 1,

4  "total_items": 12,

5  "per_page": 40,

6

  "items": [\
\
7\
\
    {\
\
8      "id": 42,\
\
9      "debit": "100.00",\
\
10      "credit": "0.00",\
\
11      "label": "Employees - Jean Dupont / Salary May 2023",\
\
12      "ledger_account_id": 987\
\
13    }\
\
14  ]

15}

```

Updated 4 months ago

* * *