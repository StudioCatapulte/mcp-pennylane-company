---
url: "https://pennylane.readme.io/reference/getcategories"
title: "List categories"
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

- `category_group_id` : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
- `analytical_code` : `eq`, `not_eq`, `in`, `not_in`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`

# `` 200      A list of categories

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

direction

string \| null

required

`cash_in` `cash_out`

created\_at

date-time

required

updated\_at

date-time

required

category\_group

object

required

category\_group object

analytical\_code

string \| null

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

2     --url 'https://app.pennylane.com/api/external/v2/categories?sort=-id' \

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
6      "id": 42,\
\
7      "label": "Alimentaire",\
\
8      "direction": "cash_in",\
\
9      "created_at": "2023-08-30T10:08:08.146343Z",\
\
10      "updated_at": "2023-08-30T10:08:08.146343Z",\
\
11\
\
      "category_group": {\
\
12        "id": 348\
\
13      },\
\
14      "analytical_code": "CODE123"\
\
15    }\
\
16  ]

17}

```

Updated about 1 month ago

* * *