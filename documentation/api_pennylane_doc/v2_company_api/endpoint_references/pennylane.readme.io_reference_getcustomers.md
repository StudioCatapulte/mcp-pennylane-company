---
url: "https://pennylane.readme.io/reference/getcustomers"
title: "List customers (company and individual)"
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
- `customer_type`: `eq`, `not_eq`
- `ledger_account_id`: `eq`, `not_eq`
- `name`: `start_with`
- `external_reference`: `start_with`, `eq`, `not_eq`, `in`, `not_in`
- `reg_no`: `eq`, `not_eq`, `in`, `not_in`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`

# `` 200      Returns a list of both company and individual customers

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

array

required

items\*

Company customer

Individual customer

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

2     --url 'https://app.pennylane.com/api/external/v2/customers?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

76
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
7      "name": "My company",\
\
8      "billing_iban": "FR1420041010050500013M02606",\
\
9      "payment_conditions": "upon_receipt",\
\
10      "recipient": "John Doe",\
\
11      "phone": "+33612345678",\
\
12      "reference": "REF-1234",\
\
13      "notes": "Some notes",\
\
14      "vat_number": "FR12345678901",\
\
15      "reg_no": "123456789",\
\
16\
\
      "ledger_account": {\
\
17        "id": 0\
\
18      },\
\
19\
\
      "emails": [\
\
20        "hello@example.org"\
\
21      ],\
\
22\
\
      "billing_address": {\
\
23        "address": "string",\
\
24        "postal_code": "string",\
\
25        "city": "string",\
\
```\
\
Updated about 1 month ago\
\
* * *