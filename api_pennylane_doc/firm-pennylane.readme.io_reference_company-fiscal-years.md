---
url: "https://firm-pennylane.readme.io/reference/company-fiscal-years"
title: "List Company's Fiscal Years"
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

page

integer

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

1 to 100

Items are paginated. By default, you get 20 items per page. You can specify another number of items per page.

# `` 200      Returns the list of fiscal years of the company.

object

items

array of objects

required

items\*

object

start

date

required

The date at which the fiscal year starts.

finish

date

required

The date at which the fiscal year ends.

status

string

required

The status of the fiscal year.

`open` `reopen` `closed` `frozen`

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

2     --url https://app.pennylane.com/api/external/firm/v1/companies/company_id/fiscal_years \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200`` 400`` 401`` 403`` 404

Updated 22 days ago

* * *

Did this page help you?

Yes

No