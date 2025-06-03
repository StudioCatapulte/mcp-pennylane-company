---
url: "https://pennylane.readme.io/reference/postsupplier"
title: "Create a Supplier"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

name

string

required

establishment\_no

string

Supplier identification number (SIRET).

- 14-digit number combining SIREN (9 digits) and NIC (5 digits)
- Only applicable for French companies

postal\_address

object

postal\_address object

vat\_number

string

ledger\_account

object \| null

ledger\_account object \| null

emails

array of strings

emails
ADD string

iban

string

supplier\_payment\_method

string \| null

automatic\_transfermanual\_transferautomatic\_debitingbill\_of\_exchangecheckcashcard

supplier\_due\_date\_delay

integer

supplier\_due\_date\_rule

string \| null

daysdays\_or\_end\_of\_month

external\_reference

string

A unique external reference you can provide to track this supplier. If not provided, Pennylane will generate an identifier for you.

# `` 201      Returns the created supplier

object

id

integer

required

name

string

required

establishment\_no

string \| null

required

Supplier identification number (SIRET).

- 14-digit number combining SIREN (9 digits) and NIC (5 digits)
- Only applicable for French companies

vat\_number

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

iban

string

required

The IBAN of the supplier

postal\_address

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

supplier\_payment\_method

string \| null

required

`automatic_transfer` `manual_transfer` `automatic_debiting` `bill_of_exchange` `check` `cash` `card`

supplier\_due\_date\_delay

integer \| null

required

supplier\_due\_date\_rule

string \| null

required

`days` `days_or_end_of_month`

external\_reference

string

required

The unique external reference that was assigned during creation either by you or Pennylane

created\_at

date-time

required

updated\_at

date-time

required

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

1curl --request POST \

2     --url https://app.pennylane.com/api/external/v2/suppliers \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

```

xxxxxxxxxx

25



1

{

2  "id": 42,

3  "name": "Pennylane",

4  "establishment_no": "82762938500014",

5  "vat_number": "FR32123456789",

6

  "ledger_account": {

7    "id": 0

8  },

9

  "emails": [\
\
10    "hello@example.org"\
\
11  ],

12  "iban": "FRXXXXXXXXXXXXXXXXXXXXXXXXX",

13

  "postal_address": {

14    "address": "string",

15    "postal_code": "string",

16    "city": "string",

17    "country_alpha2": "string"

18  },

19  "supplier_payment_method": "automatic_transfer",

20  "supplier_due_date_delay": 30,

21  "supplier_due_date_rule": "days",

22  "external_reference": "FR123",

23  "created_at": "2023-08-30T10:08:08.146343Z",

24  "updated_at": "2023-08-30T10:08:08.146343Z"

25}

```

Updated about 1 month ago

* * *