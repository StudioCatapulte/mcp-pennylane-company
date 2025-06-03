---
url: "https://pennylane.readme.io/reference/getindividualcustomer"
title: "Retrieve an individual customer"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

string

required

Individual customer identifier

# `` 200      Returns an individual customer

object

id

integer

required

name

string

required

billing\_iban

string \| null

required

payment\_conditions

string

required

Note that the `custom` option is only used on Pennylane's web app to avoid pre-filling the deadline when creating an invoice. On the API it has no effect and you will still have to provide a deadline when creating an invoice.

`upon_receipt` `custom` `15_days` `30_days` `45_days` `60_days`

recipient

string

required

phone

string

required

reference

string \| null

required

notes

string \| null

required

first\_name

string

required

last\_name

string

required

ledger\_account

object \| null

required

id

integer

required

emails

array of strings

required

emails\*

billing\_address

object

required

address

string

required

postal\_code

string

required

city

string

required

country\_alpha2

string

required

delivery\_address

object

required

address

string

required

postal\_code

string

required

city

string

required

country\_alpha2

string

required

created\_at

date-time

required

updated\_at

date-time

required

external\_reference

string

required

The unique external reference assigned to this customer, assigned on creation either by you or Pennylane. (Same attribute as `source_id` in the API v1)

billing\_language

string

required

The language in which the customer will receive invoices. Default is `fr_FR`

`fr_FR` `en_GB` `de_DE`

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

2     --url https://app.pennylane.com/api/external/v2/individual_customers/id \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

34
}

1

{

2  "id": 42,

3  "name": "John Doe",

4  "billing_iban": "FR1420041010050500013M02606",

5  "payment_conditions": "upon_receipt",

6  "recipient": "John Doe",

7  "phone": "+33612345678",

8  "reference": "REF-1234",

9  "notes": "Some notes",

10  "first_name": "John",

11  "last_name": "Doe",

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