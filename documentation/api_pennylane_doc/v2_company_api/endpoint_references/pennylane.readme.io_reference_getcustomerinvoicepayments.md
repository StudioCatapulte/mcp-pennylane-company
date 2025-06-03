---
url: "https://pennylane.readme.io/reference/getcustomerinvoicepayments"
title: "List payments for a customer invoice"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

customer\_invoice\_id

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

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`

# `` 200      Returns the list of payments for a customer invoice.   If the invoice is draft or credit note, an empty list will be returned.

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

number

required

Payment id

label

string

required

Payment label

currency

required

string

string \| null

currency\_amount

string

required

The amount of the payment in the currency

status

string

required

`initiated` `pending` `emitted` `found` `not_found` `aborted` `error` `refunded` `prepared` `pending_customer_approval` `pending_submission` `submitted` `confirmed` `paid_out` `cancelled` `customer_approval_denied` `failed` `charged_back` `resubmission_requested`

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

2     --url 'https://app.pennylane.com/api/external/v2/customer_invoices/customer_invoice_id/payments?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

15



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
6      "id": 444,\
\
7      "label": "Demo label",\
\
8      "currency": "EUR",\
\
9      "currency_amount": "230.32",\
\
10      "status": "initiated",\
\
11      "created_at": "2023-08-30T10:08:08.146343Z",\
\
12      "updated_at": "2023-08-30T10:08:08.146343Z"\
\
13    }\
\
14  ]

15}

```

Updated about 1 month ago

* * *