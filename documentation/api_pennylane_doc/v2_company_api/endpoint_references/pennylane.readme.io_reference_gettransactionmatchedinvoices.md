---
url: "https://pennylane.readme.io/reference/gettransactionmatchedinvoices"
title: "List invoices matched to a bank transaction"
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

# `` 200      A list of invoices matched to the bank transaction

object

items

array of objects

required

items\*

object

id

integer

required

Invoice identifier

type

string

required

`customer` `supplier`

url

string

required

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

2     --url https://app.pennylane.com/api/external/v2/transactions/transaction_id/matched_invoices \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

11



1

{

2

  "items": [\
\
3\
\
    {\
\
4      "id": 42,\
\
5      "type": "customer",\
\
6      "url": "https://app.pennylane.com/api/external/v2/customer_invoices/42"\
\
7    }\
\
8  ],

9  "has_more": true,

10  "next_cursor": "dXBkYXRlZF9hdDoxNjc0MTIzNDU2"

11}

```

Updated about 1 month ago

* * *