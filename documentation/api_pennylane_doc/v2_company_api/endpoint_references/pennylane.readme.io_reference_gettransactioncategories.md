---
url: "https://pennylane.readme.io/reference/gettransactioncategories"
title: "List categories of a bank transaction"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

transaction\_id

integer

required

cursor

string

Cursor for pagination. Use this to fetch the next set of results.

The cursor is an opaque string returned in the previous response's metadata.

Leave empty for the first request.

limit

integer

1 to 100

Number of items to return per request.

Defaults to 20 if not specified.

Must be between 1 and 100.

# `` 200      The list of categories of the bank transaction

object

has\_more

boolean

required

Indicates whether additional results are available beyond this set.

Use this flag to determine if another request is needed.

next\_cursor

string \| null

required

Cursor to retrieve the next set of results.

Include this value in the cursor parameter of your next request to fetch subsequent items.

A `null` `next_cursor` in the response indicates no further results.

items

array of objects

required

items\*

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/transactions/transaction_id/categories \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

17



1

{

2  "has_more": true,

3  "next_cursor": "dXBkYXRlZF9hdDoxNjc0MTIzNDU2",

4

  "items": [\
\
5\
\
    {\
\
6      "id": 421,\
\
7      "label": "HR - Salaries",\
\
8      "weight": "0.25",\
\
9\
\
      "category_group": {\
\
10        "id": 229\
\
11      },\
\
12      "analytical_code": "CODE123",\
\
13      "created_at": "2023-08-30T10:08:08.146343Z",\
\
14      "updated_at": "2023-08-30T10:08:08.146343Z"\
\
15    }\
\
16  ]

17}

```

Updated about 1 month ago

* * *