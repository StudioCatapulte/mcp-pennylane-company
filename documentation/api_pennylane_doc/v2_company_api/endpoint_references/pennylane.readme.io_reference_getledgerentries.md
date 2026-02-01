---
url: "https://pennylane.readme.io/reference/getledgerentries"
title: "List Ledger Entries"
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

filter

string

You can choose to filter items on specific fields.

Available fields and values:

- `updated_at, created_at, date`: `lt, lteq, gt, gteq, eq, not_eq`
- `journal_id`: `lt, lteq, gt, gteq, eq, not_eq`, `in`, `not_in`

sort

string

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `updated_at` will sort by ascending order, `-updated_at` will sort by descending order.

Available fields : `updated_at`, `created_at`, `date`

# `` 200      Returns a list of ledger entries.   By default, entries from fiscal periods that are closed or frozen are excluded.   However, if a 'date' filter is provided, it will return all entries within the specified date range, even if they fall within a closed or frozen fiscal period.

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

The number of items per page

items

array of objects

required

items\*

object

id

integer

required

ID of the ledger entry

created\_at

date-time

required

Created at

updated\_at

date-time

required

Last update

label

string \| null

required

Label that describes the ledger entry

date

date

required

Date of the ledger entry (ISO 8601)

journal\_id

integer

required

The journal ID where the ledger entry was created

ledger\_attachment\_filename

string \| null

required

Attachment's filename

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

2     --url https://app.pennylane.com/api/external/v2/ledger_entries \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

17



1

{

2  "total_pages": 5,

3  "current_page": 1,

4  "total_items": 12,

5  "per_page": 40,

6

  "items": [\
\
7\
\
    {\
\
8      "id": 1,\
\
9      "created_at": "2023-06-14T12:12:56.146343Z",\
\
10      "updated_at": "2023-08-30T10:08:08.146343Z",\
\
11      "label": "Payment for Services",\
\
12      "date": "2023-08-30",\
\
13      "journal_id": 123,\
\
14      "ledger_attachment_filename": "filename.pdf"\
\
15    }\
\
16  ]

17}

```

Updated 4 months ago

* * *