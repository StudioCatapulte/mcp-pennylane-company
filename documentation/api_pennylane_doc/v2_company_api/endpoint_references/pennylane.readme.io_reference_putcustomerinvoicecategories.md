---
url: "https://pennylane.readme.io/reference/putcustomerinvoicecategories"
title: "Categorize a customer invoice"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

customer\_invoice\_id

integer

required

ADD object

# `` 200      The list of categories of the customer invoice

array of objects

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request PUT \

2     --url https://app.pennylane.com/api/external/v2/customer_invoices/customer_invoice_id/categories \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

```

xxxxxxxxxx

13



1

[\
\
2\
\
  {\
\
3    "id": 421,\
\
4    "label": "HR - Salaries",\
\
5    "weight": "0.25",\
\
6\
\
    "category_group": {\
\
7      "id": 229\
\
8    },\
\
9    "analytical_code": "CODE123",\
\
10    "created_at": "2023-08-30T10:08:08.146343Z",\
\
11    "updated_at": "2023-08-30T10:08:08.146343Z"\
\
12  }\
\
13]

```

Updated about 1 month ago

* * *