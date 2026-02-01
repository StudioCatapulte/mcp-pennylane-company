---
url: "https://pennylane.readme.io/reference/gettransactions"
title: "List transactions"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

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

filter

string

You can choose to filter items on specific fields.

Available fields and values:

- `id`: `eq`, `not_eq`, `in`, `not_in`
- `bank_account_id`: `eq`, `not_eq`, `in`, `not_in`
- `journal_id`: `eq`, `not_eq`, `in`, `not_in`
- `date`: `eq`, `not_eq`, `gt`, `lt`, `lteq`, `gteq`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`

# `` 200      A list of transactions

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

Transaction identifier

label

string \| null

required

date

date

required

outstanding\_balance

string \| null

required

This is the balance of the transaction after it has been

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

journal\_id

integer

required

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

matched\_invoices

object

required

matched\_invoices object

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

2     --url 'https://app.pennylane.com/api/external/v2/transactions?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

41
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
18      "journal_id": 42,\
\
19\
\
      "bank_account": {\
\
20        "id": 53,\
\
21        "url": "https://app.pennylane.com/api/external/v2/bank_accounts/53"\
\
22      },\
\
23\
\
      "categories": [\
\
24\
\
        {\
\
25          "id": 421,\
\
```\
\
Updated about 1 month ago\
\
* * *