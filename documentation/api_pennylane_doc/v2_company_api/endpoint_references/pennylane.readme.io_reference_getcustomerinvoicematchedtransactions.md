---
url: "https://pennylane.readme.io/reference/getcustomerinvoicematchedtransactions"
title: "List matched transactions for a customer invoice"
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

# `` 200      Returns the list of matched transactions for a customer invoice. If the invoice is archived, or draft, an empty list will be returned.

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

Bank transaction identifier

label

string \| null

required

date

date

required

outstanding\_balance

string \| null

required

This is the balance of the bank transaction after it has been

processed.

created\_at

date-time

required

updated\_at

date-time

required

archived\_at

date-time \| null

required

currency

required

string

string \| null

currency\_amount

string

required

Amount in the currency of the transaction.

amount

string

required

Transaction amount in euros. If the currency is euro, `currency_amount` and `amount` are identical.

currency\_fee

string \| null

required

Fee in the currency of the transaction.

fee

string \| null

required

Transaction fee in euros. If the currency is euro, `currency_fee` and `fee`

are identical.

journal

object

required

journal object

bank\_account

object

required

bank\_account object

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url 'https://app.pennylane.com/api/external/v2/customer_invoices/customer_invoice_id/matched_transactions?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

40
}

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
6      "id": 42,\
\
7      "label": "VIR SEPA MY SUPPLIER SAS",\
\
8      "date": "2023-08-30",\
\
9      "outstanding_balance": "49.3",\
\
10      "created_at": "2023-08-30T10:08:08.146343Z",\
\
11      "updated_at": "2023-08-30T10:08:08.146343Z",\
\
12      "archived_at": "2023-08-30T10:08:08.146343Z",\
\
13      "currency": "EUR",\
\
14      "currency_amount": "120.00",\
\
15      "amount": "120.00",\
\
16      "currency_fee": "120.00",\
\
17      "fee": "120.00",\
\
18\
\
      "journal": {\
\
19        "id": 42\
\
20      },\
\
21\
\
      "bank_account": {\
\
22        "id": 53,\
\
23        "url": "https://app.pennylane.com/api/external/v2/bank_accounts/53"\
\
24      },\
\
25\
\
      "categories": [\
\
```\
\
Updated about 1 month ago\
\
* * *