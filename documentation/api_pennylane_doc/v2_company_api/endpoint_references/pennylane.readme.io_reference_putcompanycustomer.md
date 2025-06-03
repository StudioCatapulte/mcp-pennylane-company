---
url: "https://pennylane.readme.io/reference/putcompanycustomer"
title: "Update a company customer"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

string

required

Company customer identifier

name

string

vat\_number

string

reg\_no

string

phone

string

billing\_address

object

billing\_address object

delivery\_address

object \| null

delivery\_address object \| null

payment\_conditions

string

Defaults to 30\_days

Note that the `custom` option is only used on Pennylane's web app to avoid pre-filling the deadline when creating an invoice. On the API it has no effect and you will still have to provide a deadline when creating an invoice.

upon\_receiptcustom15\_days30\_days45\_days60\_days

billing\_iban

string \| null

recipient

string

The name of the person to whom the invoice is addressed

reference

string \| null

notes

string \| null

emails

array of strings

emails
ADD string

external\_reference

string

You can use your own unique value when creating the customer. If not provided, Pennylane will pick one for you. Value must be unique

billing\_language

string

The language in which the customer will receive invoices. Default is `fr_FR`

fr\_FRen\_GBde\_DE

# `` 200      Returns the updated company customer

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

The name of the person to whom the invoice is addressed

phone

string

required

reference

string \| null

required

notes

string \| null

required

vat\_number

string

required

reg\_no

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

# `` 409      Conflict with the current state of the target resource, such as when trying to create a resource that already exists.

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

2     --url https://app.pennylane.com/api/external/v2/company_customers/id \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "payment_conditions": "30_days"

8}

9'

```

```

xxxxxxxxxx

34
}

1

{

2  "id": 42,

3  "name": "My Company",

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