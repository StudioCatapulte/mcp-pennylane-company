---
url: "https://pennylane.readme.io/reference/getcustomerinvoices"
title: "List customer invoices"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

cursor

string

Cursor for pagination. Use this to fetch the next set of results.

The cursor is an opaque string returned in the previous response's metadata.

Leave empty for the first request.

limit

integer

1 to 100

Number of items to return per request.

Defaults to 20 if not specified.

Must be between 1 and 100.

filter

string

You can choose to filter items on specific fields.

Available fields and values:

- `id`, `date`, `customer_id`, `billing_subscription_id`, `estimate_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
- `invoice_number`: `eq`, `not_eq`, `in`, `not_in`
- `draft`: `eq` (boolean)
- `credit_note`: `eq` (boolean)
- `category_id`: `in`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`, `date`

# `` 200      A list of Customer Invoices and/or credit notes

object

has\_more

boolean

required

Indicates whether additional results are available beyond this set.

Use this flag to determine if another request is needed.

next\_cursor

string \| null

required

Cursor to retrieve the next set of results.

Include this value in the cursor parameter of your next request to fetch subsequent items.

A `null` `next_cursor` in the response indicates no further results.

items

array of objects

required

items\*

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

discount object

ledger\_entry

object

required

ledger\_entry object

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

customer object \| null

invoice\_line\_sections

object

required

invoice\_line\_sections object

invoice\_lines

object

required

invoice\_lines object

categories

object

required

categories object

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

billing\_subscription object \| null

credited\_invoice

object \| null

required

The credited invoice if the invoice is a credit note.

credited\_invoice object \| null

customer\_invoice\_template

object \| null

required

customer\_invoice\_template object \| null

transaction\_reference

object \| null

required

This reconciles the invoice with a transaction. See documentation about [automatic payment matching](https://pennylane.readme.io/docs/automating-payment-matching).

transaction\_reference object \| null

payments

object

required

payments object

matched\_transactions

object

required

matched\_transactions object

appendices

object

required

appendices object

from\_estimate\_id

integer \| null

required

deprecated

The ID of the estimate at the origin of the invoice

estimate

object \| null

required

The estimate at the origin of the invoice

estimate object \| null

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url 'https://app.pennylane.com/api/external/v2/customer_invoices?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

83
}

1

{

2  "has_more": true,

3  "next_cursor": "dXBkYXRlZF9hdDoxNjc0MTIzNDU2",

4

  "items": [\
\
5\
\
    {\
\
6      "id": 42,\
\
7      "label": "Invoice label",\
\
8      "invoice_number": "F20230001",\
\
9      "currency": "EUR",\
\
10      "amount": "230.32",\
\
11      "currency_amount": "230.32",\
\
12      "currency_amount_before_tax": "196.32",\
\
13      "exchange_rate": "1.0",\
\
14      "date": "2023-08-30",\
\
15      "deadline": "2020-09-02",\
\
16      "currency_tax": "34.0",\
\
17      "tax": "34.0",\
\
18      "language": "fr_FR",\
\
19      "paid": false,\
\
20      "status": "archived",\
\
21\
\
      "discount": {\
\
22        "type": "absolute",\
\
23        "value": "25"\
\
24      },\
\
25\
\
      "ledger_entry": {\
\
```\
\
Updated about 1 month ago\
\
* * *