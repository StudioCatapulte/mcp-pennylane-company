---
url: "https://pennylane.readme.io/reference/deletecustomerinvoicematchedtransactions"
title: "Unmatch a transaction to a customer invoice"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

customer\_invoice\_id

integer

required

id

integer

required

`` 204

Transaction unmatched successfully

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request DELETE \

2     --url https://app.pennylane.com/api/external/v2/customer_invoices/customer_invoice_id/matched_transactions/id \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 400`` 401`` 403`` 404`` 422

Updated about 1 month ago

* * *