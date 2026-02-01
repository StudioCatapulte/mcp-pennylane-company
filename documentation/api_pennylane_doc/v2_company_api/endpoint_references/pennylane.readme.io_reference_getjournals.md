---
url: "https://pennylane.readme.io/reference/getjournals"
title: "List journals"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

page

integer

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

1 to 100

Items are paginated. By default, you get 20 items per page. You can specify another number of items per page.

# `` 200      Returns a list of journals

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

code

string

required

id

integer

required

label

string

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

2     --url https://app.pennylane.com/api/external/v2/journals \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

13



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
8      "code": "string",\
\
9      "id": 0,\
\
10      "label": "string"\
\
11    }\
\
12  ]

13}

```

Updated 4 months ago

* * *