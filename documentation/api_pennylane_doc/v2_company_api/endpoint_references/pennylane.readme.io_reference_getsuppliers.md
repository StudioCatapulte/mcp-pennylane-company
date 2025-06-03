---
url: "https://pennylane.readme.io/reference/getsuppliers"
title: "List suppliers"
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

- `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
- `ledger_account_id`: `eq`, `not_eq`
- `name`: `start_with`
- `external_reference`: `eq`, `not_eq`, `in`, `not_in`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`

# `` 200      Returns a list of suppliers

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

The list of items returned

items\*

object

id

integer

required

name

string

required

establishment\_no

string \| null

required

Supplier identification number (SIRET).

- 14-digit number combining SIREN (9 digits) and NIC (5 digits)
- Only applicable for French companies

vat\_number

string

required

ledger\_account

object \| null

required

ledger\_account object \| null

emails

array of strings

required

emails\*

iban

string

required

The IBAN of the supplier

postal\_address

object

required

postal\_address object

supplier\_payment\_method

string \| null

required

`automatic_transfer` `manual_transfer` `automatic_debiting` `bill_of_exchange` `check` `cash` `card`

supplier\_due\_date\_delay

integer \| null

required

supplier\_due\_date\_rule

string \| null

required

`days` `days_or_end_of_month`

external\_reference

string

required

The unique external reference that was assigned during creation either by you or Pennylane

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

2     --url 'https://app.pennylane.com/api/external/v2/suppliers?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

31
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
7      "name": "Pennylane",\
\
8      "establishment_no": "82762938500014",\
\
9      "vat_number": "FR32123456789",\
\
10\
\
      "ledger_account": {\
\
11        "id": 0\
\
12      },\
\
13\
\
      "emails": [\
\
14        "hello@example.org"\
\
15      ],\
\
16      "iban": "FRXXXXXXXXXXXXXXXXXXXXXXXXX",\
\
17\
\
      "postal_address": {\
\
18        "address": "string",\
\
19        "postal_code": "string",\
\
20        "city": "string",\
\
21        "country_alpha2": "string"\
\
22      },\
\
23      "supplier_payment_method": "automatic_transfer",\
\
24      "supplier_due_date_delay": 30,\
\
25      "supplier_due_date_rule": "days",\
\
```\
\
Updated about 1 month ago\
\
* * *