---
url: "https://pennylane.readme.io/reference/getledgerentrylinesletteredledgerentrylines"
title: "List ledger entry lines lettered to a given ledger entry line"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

number

required

Ledger Entry line (id)

page

integer

This is the current page that will be returned. The page index starts at 1.

per\_page

integer

1 to 100

The number of items per page, default is 20.

# `` 200      Returns a list of ledger entry lines

object

total\_pages

integer

required

The total number of pages available

current\_page

integer

required

The current page returned

per\_page

integer

required

The number of items returned per page

total\_items

integer

required

The total number of items available

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

Updated 4 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/ledger_entry_lines/id/lettered_ledger_entry_lines \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

35
}

1

{

2  "total_pages": 5,

3  "current_page": 1,

4  "per_page": 20,

5  "total_items": 12,

6

  "items": [\
\
7\
\
    {\
\
8      "id": 42,\
\
9      "debit": "100.00",\
\
10      "credit": "0.00",\
\
11      "label": "Employees - Jean Dupont / Salary May 2023",\
\
12\
\
      "ledger_account": {\
\
13        "id": 987,\
\
14        "url": "https://app.pennylane.com/api/external/v2/ledger_accounts/42"\
\
15      },\
\
16\
\
      "journal": {\
\
17        "id": 123,\
\
18        "url": "https://app.pennylane.com/api/external/v2/journals/42"\
\
19      },\
\
20      "date": "2023-08-30",\
\
21\
\
      "ledger_entry": {\
\
22        "id": 123001\
\
23      },\
\
24\
\
      "lettered_ledger_entry_lines": {\
\
25\
\
        "ids": [\
\
```\
\
Updated 4 months ago\
\
* * *