---
url: "https://pennylane.readme.io/reference/putledgerentrylinescategories"
title: "Link Analytical Categories to a Ledger Entry line"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

ledger\_entry\_line\_id

number

required

Existing Ledger Entry line (id)

With weights

\[deprecated\] Without weights

# `` 200      Returns the Ledger Entry line with attached Analytical Categories

object

ledger\_entry\_line

object

required

id

integer

required

label

string

required

categories

array of objects

required

categories\*

object

id

integer

required

label

string

required

weight

string

required

category\_group

object

required

category\_group object

analytical\_code

string \| null

required

created\_at

date-time

required

updated\_at

date-time

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

# `` 422      Unprocessable entity

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

1curl --request PUT \

2     --url https://app.pennylane.com/api/external/v2/ledger_entry_lines/ledger_entry_line_id/categories \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

```

xxxxxxxxxx

19



1

{

2

  "ledger_entry_line": {

3    "id": 2,

4    "label": "Employee - remuneration and contributions",

5

    "categories": [\
\
6\
\
      {\
\
7        "id": 421,\
\
8        "label": "HR - Salaries",\
\
9        "weight": "0.25",\
\
10\
\
        "category_group": {\
\
11          "id": 229\
\
12        },\
\
13        "analytical_code": "CODE123",\
\
14        "created_at": "2023-08-30T10:08:08.146343Z",\
\
15        "updated_at": "2023-08-30T10:08:08.146343Z"\
\
16      }\
\
17    ]

18  }

19}

```

Updated 4 months ago

* * *