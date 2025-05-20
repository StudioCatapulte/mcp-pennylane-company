---
url: "https://firm-pennylane.readme.io/reference/company-trial-balance-1"
title: "Get the trial balance of a company"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

company\_id

integer

required

Existing company identifier (id)

period\_start

string

required

The start of the period you want the trial balance for.

period\_end

string

required

The end of the period you want the trial balance for.

is\_auxiliary

boolean

Whether to include auxiliary accounts or not.

truetruefalse

page

integer

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

1 to 1000

Items are paginated. By default, you get 500 items per page. You can specify another number of items per page.

# `` 200      Returns a list of balances grouped by ledger account.

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

formatted\_number

string

required

Formatted ledger account number

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

# `` 404      The resource was not found

object

error

string

required

status

integer

required

# `` 422      Unprocessable entity

object

error

string

required

status

integer

required

Updated 22 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/firm/v1/companies/company_id/trial_balance \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200`` 400`` 401`` 403`` 404`` 422

Updated 22 days ago

* * *

Did this page help you?

Yes

No