---
url: "https://pennylane.readme.io/reference/updatesupplierinvoicepaymentstatus"
title: "Update a supplier invoice payment status"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

supplier\_invoice\_id

integer

required

Supplier invoice identifier

payment\_status

string

required

paidto\_be\_paid

`` 204

The supplier invoice payment status was successfully updated

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

1curl --request PUT \

2     --url https://app.pennylane.com/api/external/v2/supplier_invoices/supplier_invoice_id/payment_status \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "payment_status": "paid"

8}

9'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 400`` 401`` 403`` 404`` 422

Updated about 1 month ago

* * *