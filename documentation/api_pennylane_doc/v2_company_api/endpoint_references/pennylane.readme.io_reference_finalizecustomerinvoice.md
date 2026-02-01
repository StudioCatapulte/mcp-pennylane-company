---
url: "https://pennylane.readme.io/reference/finalizecustomerinvoice"
title: "Turn the draft invoice into a finalized invoice."
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

integer

required

# `` 200      A Customer Invoice

object

id

integer

required

Invoice identifier

label

string \| null

required

invoice\_number

string

required

currency

string

required

Defaults to EUR

`EUR` `USD` `GBP` `AED` `AFN` `ALL` `AMD` `ANG` `AOA` `ARS` `AUD` `AWG` `AZN` `BAM` `BBD` `BDT` `BGN` `BHD` `BIF` `BMD` `BND` `BOB` `BRL` `BSD` `BTN` `BWP` `BYN` `BYR` `BZD` `CAD` `CDF` `CHF` `CLF` `CLP` `CNY` `COP` `CRC` `CUC` `CUP` `CVE` `CZK` `DJF` `DKK` `DOP` `DZD` `EGP` `ERN` `ETB` `FJD` `FKP` `GEL` `GGP` `GHS` `GIP` `GMD` `GNF` `GTQ` `GYD` `HKD` `HNL` `HRK` `HTG` `HUF` `IDR` `ILS` `IMP` `INR` `IQD` `IRR` `ISK` `JEP` `JMD` `JOD` `JPY` `KES` `KGS` `KHR` `KMF` `KPW` `KRW` `KWD` `KYD` `KZT` `LAK` `LBP` `LKR` `LRD` `LSL` `LTL` `LVL` `LYD` `MAD` `MDL` `MGA` `MKD` `MMK` `MNT` `MOP` `MRO` `MUR` `MVR` `MWK` `MXN` `MYR` `MZN` `NAD` `NGN` `NIO` `NOK` `NPR` `NZD` `OMR` `PAB` `PEN` `PGK` `PHP` `PKR` `PLN` `PYG` `QAR` `RON` `RSD` `RUB` `RWF` `SAR` `SBD` `SCR` `SDG` `SEK` `SGD` `SHP` `SLL` `SOS` `SRD` `STD` `SVC` `SYP` `SZL` `THB` `TJS` `TMT` `TND` `TOP` `TRY` `TTD` `TWD` `TZS` `UAH` `UGX` `UYU` `UZS` `VEF` `VND` `VUV` `WST` `XAF` `XCD` `XDR` `XOF` `XPF` `YER` `ZAR` `ZMK` `ZMW` `ZWL`

amount

string

required

Invoice amount (total value of the invoice in euros. If the currency is euro, `currency_amount` and `amount` are identical)

currency\_amount

string

required

Invoice currency amount (total value of the invoice in the currency of the invoice)

currency\_amount\_before\_tax

string

required

Invoice currency amount before tax (total value before tax of the invoice in the currency of the invoice)

exchange\_rate

string

required

Invoice exchange rate (used to convert the invoice to euros. If the invoice currency is euro it will be 1.0)

date

date \| null

required

Invoice issue date (ISO 8601)

deadline

string \| null

required

Invoice payment deadline (ISO 8601)

currency\_tax

string

required

Invoice taxable amount (in euros. If the currency is euro, `currency_amount` and `amount` are identical)

tax

string

required

Invoice taxable amount (in invoice currency)

language

string

required

Defaults to fr\_FR

`fr_FR` `en_GB`

paid

boolean

required

Invoice paid status (set to True if the invoice is paid)

status

string

required

`archived` `incomplete` `cancelled` `paid` `partially_cancelled` `upcoming` `late` `draft` `credit_note`

discount

object

required

type

string

required

Discount type.

- absolute if it is an amount
- relative if it is a percentage

`absolute` `relative`

value

string \| null

required

Discount value on the total amount before tax of the line

ledger\_entry

object

required

id

integer

required

Ledger entry identifier

public\_file\_url

string \| null

required

Public URL of the invoice file. The URL will expire after 30 minutes.

filename

string \| null

required

Name of the file attached to the invoice

remaining\_amount\_with\_tax

string \| null

required

The remaining amount with VAT to pay for the invoice to be considered paid

remaining\_amount\_without\_tax

string \| null

required

The remaining amount without VAT to pay for the invoice to be considered paid

draft

boolean

required

Indicates if the invoice is in draft (has not been finalized)

special\_mention

string \| null

required

Additional details

customer

object \| null

required

id

integer

required

url

string

required

URL to get the customer.

invoice\_line\_sections

object

required

url

string

required

URL to get the invoice line sections of the invoice.

invoice\_lines

object

required

url

string

required

URL to get the invoice lines of the invoice.

categories

object

required

url

string

required

URL to get the categories of the invoice.

pdf\_invoice\_free\_text

string

required

pdf\_invoice\_subject

string

required

pdf\_description

string \| null

required

billing\_subscription

object \| null

required

id

integer

required

credited\_invoice

object \| null

required

The credited invoice if the invoice is a credit note.

id

integer

required

url

string

required

URL to get the credited invoice.

customer\_invoice\_template

object \| null

required

id

integer

required

transaction\_reference

object \| null

required

This reconciles the invoice with a transaction. See documentation about [automatic payment matching](https://pennylane.readme.io/docs/automating-payment-matching).

banking\_provider

string

required

The banking provider for the transaction

provider\_field\_name

string

required

Name of the field that you want to match

provider\_field\_value

string

required

Value that you want to match

payments

object

required

url

string

required

URL to get the payments of the invoice.

matched\_transactions

object

required

url

string

required

URL to get the transactions of the invoice.

appendices

object

required

url

string

required

URL to get the appendices of the invoice.

from\_estimate\_id

integer \| null

required

deprecated

The ID of the estimate at the origin of the invoice

estimate

object \| null

required

The estimate at the origin of the invoice

id

integer

required

external\_reference

string

required

The unique external reference that was assigned during creation either by you or Pennylane. (Same attribute as `external_id` in the API v1)

archived\_at

date-time \| null

required

The time the invoice has been archived

created\_at

date-time

required

The time the invoice has been created

updated\_at

date-time

required

The last time the invoice has been updated

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

2     --url https://app.pennylane.com/api/external/v2/customer_invoices/id/finalize \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

77
}

1

{

2  "id": 42,

3  "label": "Invoice label",

4  "invoice_number": "F20230001",

5  "currency": "EUR",

6  "amount": "230.32",

7  "currency_amount": "230.32",

8  "currency_amount_before_tax": "196.32",

9  "exchange_rate": "1.0",

10  "date": "2023-08-30",

11  "deadline": "2020-09-02",

12  "currency_tax": "34.0",

13  "tax": "34.0",

14  "language": "fr_FR",

15  "paid": false,

16  "status": "archived",

17

  "discount": {

18    "type": "absolute",

19    "value": "25"

20  },

21

  "ledger_entry": {

22    "id": 42002

23  },

24  "public_file_url": "https://app.pennylane.com/public/invoice/pdf?encrypted_id=bzjoVJe...3D%3D",

25  "filename": "my_file.pdf",

```

Updated about 1 month ago

* * *