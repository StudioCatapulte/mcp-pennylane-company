---
url: "https://pennylane.readme.io/reference/gettrialbalance"
title: "Get the trial balance"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

period\_start

date

required

The start of the period you want the trial balance for.

period\_end

date

required

The end of the period you want the trial balance for.

is\_auxiliary

boolean

Whether to include auxiliary accounts or not.

truetruefalse

page

integer

required

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

required

1 to 1000

The number of items returned per page.

# `` 200      Returns a list of balances grouped by ledger accounts.

object

items

array of objects

required

items\*

object

number

string

required

Ledger account number

formatted\_number

string

required

Ledger account number with padded

label

string

required

Ledger account label

debits

string

required

Ledger account debits

credits

string

required

Ledger account credits

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

Updated 4 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/trial_balance \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

15



1

{

2

  "items": [\
\
3\
\
    {\
\
4      "number": "512",\
\
5      "formatted_number": "51200000",\
\
6      "label": "Capital souscrit - appelé, versé",\
\
7      "debits": "45353.95",\
\
8      "credits": "2343.05"\
\
9    }\
\
10  ],

11  "total_pages": 5,

12  "current_page": 1,

13  "total_items": 12,

14  "per_page": 40

15}

```

Updated 4 months ago

* * *