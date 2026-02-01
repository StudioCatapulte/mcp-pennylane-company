---
url: "https://pennylane.readme.io/reference/getsupplierinvoices"
title: "List supplier invoices"
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

- `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
- `supplier_id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
- `invoice_number`: `eq`, `not_eq`, `in`, `not_in`
- `date`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`
- `category_id`: `in`
- `external_reference`: `eq`, `not_eq`, `in`, `not_in`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`, `date`

# `` 200      A list of supplier invoices

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

The ID of the supplier invoice

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

Invoice amount (total value of the invoice in euros). If the currency is euro, `currency_amount` and `amount` are identical.

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

string \| null

required

Invoice issue date (ISO 8601)

deadline

string \| null

required

Invoice payment deadline (ISO 8601)

currency\_tax

string

required

Invoice taxable amount (in euros). If the currency is euro, `currency_tax` and `tax` are identical.

tax

string

required

Invoice taxable amount (in invoice currency)

reconciled

boolean

required

Whether the invoice has been reconciled or not

accounting\_status

string

required

The accounting state of the invoice.

- `draft`: The invoice is not yet sent to the accountant.
- `archived`: The invoice has been archived.
- `entry`: The invoice is incomplete. Some information is missing on the invoice and needs to be completed by SME.
- `validation_needed`: The invoice is sent to the accountant and needs validation.
- `complete`: The invoice has been validated by the accountant.

`draft` `archived` `entry` `validation_needed` `complete`

filename

string \| null

required

Name of the file attached to the invoice

public\_file\_url

string \| null

required

Public URL of the invoice file. The URL will expire after 30 minutes.

remaining\_amount\_with\_tax

string \| null

required

The remaining amount with VAT to pay for the invoice to be considered paid

remaining\_amount\_without\_tax

string \| null

required

The remaining amount without VAT to pay for the invoice to be considered paid

ledger\_entry

object

required

ledger\_entry object

supplier

object \| null

required

supplier object \| null

invoice\_lines

object

required

invoice\_lines object

categories

object

required

categories object

transaction\_reference

object \| null

required

This reconciles the invoice with a transaction. See documentation about [automatic payment matching](https://pennylane.readme.io/docs/automating-payment-matching).

transaction\_reference object \| null

payment\_status

string

required

`to_be_processed` `to_be_paid` `partially_paid` `payment_error` `payment_scheduled` `payment_in_progress` `payment_emitted` `payment_found` `paid_offline` `fully_paid`

payments

object

required

payments object

matched\_transactions

object

required

matched\_transactions object

external\_reference

string

required

The unique external reference that was assigned during creation either by you or Pennylane

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

2     --url 'https://app.pennylane.com/api/external/v2/supplier_invoices?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

55
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
6      "id": 123,\
\
7      "label": "Demo label",\
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
15      "deadline": "2023-09-30",\
\
16      "currency_tax": "34.0",\
\
17      "tax": "34.0",\
\
18      "reconciled": false,\
\
19      "accounting_status": "draft",\
\
20      "filename": "my_file.pdf",\
\
21      "public_file_url": "https://app.pennylane.com/public/invoice/pdf?encrypted_id=bzjoVJe...3D%3D",\
\
22      "remaining_amount_with_tax": "20.0",\
\
23      "remaining_amount_without_tax": "16.0",\
\
24\
\
      "ledger_entry": {\
\
25        "id": 42003\
\
```\
\
Updated about 1 month ago\
\
* * *