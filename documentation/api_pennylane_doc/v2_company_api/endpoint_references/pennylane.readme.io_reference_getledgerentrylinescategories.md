---
url: "https://pennylane.readme.io/reference/getledgerentrylinescategories"
title: "List categories of a Ledger Entry line"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

ledger\_entry\_line\_id

integer

required

Existing Ledger Entry line (id)

page

integer

required

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

required

1 to 100

Items are paginated. By default, you get 20 items per page. You can specify another number of items per page.

# `` 200      The list of categories of the Ledger Entry line

object

total\_pages

integer

required

The total number of pages available

current\_page

integer

required

The current page returned

total\_items

integer

required

The total number of items available

per\_page

integer

required

The number of items returned per page

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

Updated 4 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/ledger_entry_lines/ledger_entry_line_id/categories \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

19



1

{

2  "total_pages": 5,

3  "current_page": 1,

4  "total_items": 12,

5  "per_page": 20,

6

  "items": [\
\
7\
\
    {\
\
8      "id": 421,\
\
9      "label": "HR - Salaries",\
\
10      "weight": "0.25",\
\
11\
\
      "category_group": {\
\
12        "id": 229\
\
13      },\
\
14      "analytical_code": "CODE123",\
\
15      "created_at": "2023-08-30T10:08:08.146343Z",\
\
16      "updated_at": "2023-08-30T10:08:08.146343Z"\
\
17    }\
\
18  ]

19}

```

Updated 4 months ago

* * *