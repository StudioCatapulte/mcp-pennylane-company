---
url: "https://pennylane.readme.io/reference/getcustomer"
title: "Retrieve a customer"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

integer

required

Customer identifier

# `` 200      Returns a company customer

Company customer

Individual customer

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/customers/id \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

35
}

1

{

2  "id": 42,

3  "name": "My company",

4  "billing_iban": "FR1420041010050500013M02606",

5  "payment_conditions": "upon_receipt",

6  "recipient": "John Doe",

7  "phone": "+33612345678",

8  "reference": "REF-1234",

9  "notes": "Some notes",

10  "vat_number": "FR12345678901",

11  "reg_no": "123456789",

12

  "ledger_account": {

13    "id": 0

14  },

15

  "emails": [\
\
16    "hello@example.org"\
\
17  ],

18

  "billing_address": {

19    "address": "string",

20    "postal_code": "string",

21    "city": "string",

22    "country_alpha2": "string"

23  },

24

  "delivery_address": {

25    "address": "string",

```

Updated about 1 month ago

* * *