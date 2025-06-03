---
url: "https://pennylane.readme.io/reference/getcustomerinvoiceinvoicelinesections"
title: "List invoice line sections for a customer invoice"
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

# `` 200      Returns the list of invoice line sections for a customer invoice

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

Invoice line section id

title

string \| null

required

Invoice line section label

description

string \| null

required

Invoice line section description

rank

integer

required

The rank of the section in the invoice. The rank is used to order the sections in the invoice.

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

2     --url 'https://app.pennylane.com/api/external/v2/customer_invoices/customer_invoice_id/invoice_line_sections?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

14



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
7      "title": "Section #1",\
\
8      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",\
\
9      "rank": 1,\
\
10      "created_at": "2023-08-30T10:08:08.146343Z",\
\
11      "updated_at": "2023-08-30T10:08:08.146343Z"\
\
12    }\
\
13  ]

14}

```

Updated about 1 month ago

* * *