---
url: "https://pennylane.readme.io/reference/importsupplierinvoice"
title: "Import a supplier invoice with a file attached"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

file\_attachment\_id

integer

required

The ID of the supplier invoice file attachment to import

import\_as\_incomplete

boolean

Defaults to false

This will mark the invoice as incomplete.

truefalse

supplier\_id

integer

required

The ID of the supplier to import the invoice for

date

date

required

The date of the invoice (ISO 8601)

deadline

date

required

Invoice payment deadline (ISO 8601)

invoice\_number

string

The invoice number

currency

string

Defaults to EUR

EURUSDGBPAEDAFNALLAMDANGAOAARSAUDAWGAZNBAMBBDBDTBGNBHDBIFBMDBNDBOBBRLBSDBTNBWPBYNBYRBZDCADCDFCHFCLFCLPCNYCOPCRCCUCCUPCVECZKDJFDKKDOPDZDEGPERNETBFJDFKPGELGGPGHSGIPGMDGNFGTQGYDHKDHNLHRKHTGHUFIDRILSIMPINRIQDIRRISKJEPJMDJODJPYKESKGSKHRKMFKPWKRWKWDKYDKZTLAKLBPLKRLRDLSLLTLLVLLYDMADMDLMGAMKDMMKMNTMOPMROMURMVRMWKMXNMYRMZNNADNGNNIONOKNPRNZDOMRPABPENPGKPHPPKRPLNPYGQARRONRSDRUBRWFSARSBDSCRSDGSEKSGDSHPSLLSOSSRDSTDSVCSYPSZLTHBTJSTMTTNDTOPTRYTTDTWDTZSUAHUGXUYUUZSVEFVNDVUVWSTXAFXCDXDRXOFXPFYERZARZMKZMWZWL

currency\_amount\_before\_tax

string

required

Invoice currency amount before tax (total value before tax of the invoice in the currency of the invoice)

currency\_amount

string

required

Invoice currency amount (total value of the invoice in the currency of the invoice)

amount

string

Invoice amount in euros (total value of the invoice in euros). If the currency is euro, `currency_amount` and `amount` are identical.

currency\_tax

string

required

Invoice taxable amount (in invoice currency)

tax

string

Invoice taxable amount (in euros). If the currency is euro, `currency_tax` and `tax` are identical.

transaction\_reference

object

By adding this field you can automatically reconcile the newly imported invoice with a transaction. See documentation about [automatic payment matching](https://pennylane.readme.io/docs/automating-payment-matching).

transaction\_reference object

invoice\_lines

array of objects

required

invoice\_lines\*
ADD object

external\_reference

string

A unique external reference you can provide to track this supplier. If not provided, Pennylane will generate an identifier for you.

# `` 201      The imported supplier invoice

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

id

integer

required

Ledger entry identifier

supplier

object \| null

required

id

integer

required

url

string

required

URL to get the supplier.

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

payment\_status

string

required

`to_be_processed` `to_be_paid` `partially_paid` `payment_error` `payment_scheduled` `payment_in_progress` `payment_emitted` `payment_found` `paid_offline` `fully_paid`

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

10

1curl --request POST \

2     --url https://app.pennylane.com/api/external/v2/supplier_invoices/import \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "import_as_incomplete": false,

8  "currency": "EUR"

9}

10'

```

```

xxxxxxxxxx

49
}

1

{

2  "id": 123,

3  "label": "Demo label",

4  "invoice_number": "F20230001",

5  "currency": "EUR",

6  "amount": "230.32",

7  "currency_amount": "230.32",

8  "currency_amount_before_tax": "196.32",

9  "exchange_rate": "1.0",

10  "date": "2023-08-30",

11  "deadline": "2023-09-30",

12  "currency_tax": "34.0",

13  "tax": "34.0",

14  "reconciled": false,

15  "accounting_status": "draft",

16  "filename": "my_file.pdf",

17  "public_file_url": "https://app.pennylane.com/public/invoice/pdf?encrypted_id=bzjoVJe...3D%3D",

18  "remaining_amount_with_tax": "20.0",

19  "remaining_amount_without_tax": "16.0",

20

  "ledger_entry": {

21    "id": 42003

22  },

23

  "supplier": {

24    "id": 456,

25    "url": "https://app.pennylane.com/api/external/v2/suppliers/42"

```

Updated about 1 month ago

* * *