---
url: "https://pennylane.readme.io/reference/getledgerentrylines"
title: "List ledger entry lines"
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

Available fields : `id`, `journal_id`, `ledger_account_id`, `date`

Available operators : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`, `date`

# `` 200      Returns ledger entry lines

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

ID of the entry line

debit

string

required

Debit amount for the entry line

credit

string

required

Credit amount for the entry line

label

string

required

Label that describes the entry line

ledger\_account

object

required

ledger\_account object

journal

object

required

journal object

date

date

required

Date of the ledger entry line (ISO 8601)

ledger\_entry

object

required

ledger\_entry object

lettered\_ledger\_entry\_lines

object

required

Ledger entry lines that are lettered with this entry line.

lettered\_ledger\_entry\_lines object

created\_at

date-time

required

The time the entry line has been created

updated\_at

date-time

required

The last time the entry line has been updated

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

Updated 3 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url 'https://app.pennylane.com/api/external/v2/ledger_entry_lines?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

33
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
7      "debit": "100.00",\
\
8      "credit": "0.00",\
\
9      "label": "Employees - Jean Dupont / Salary May 2023",\
\
10\
\
      "ledger_account": {\
\
11        "id": 987,\
\
12        "url": "https://app.pennylane.com/api/external/v2/ledger_accounts/42"\
\
13      },\
\
14\
\
      "journal": {\
\
15        "id": 123,\
\
16        "url": "https://app.pennylane.com/api/external/v2/journals/42"\
\
17      },\
\
18      "date": "2023-08-30",\
\
19\
\
      "ledger_entry": {\
\
20        "id": 123001\
\
21      },\
\
22\
\
      "lettered_ledger_entry_lines": {\
\
23\
\
        "ids": [\
\
24          42,\
\
25          1271004\
\
```\
\
Updated 3 months ago\
\
* * *