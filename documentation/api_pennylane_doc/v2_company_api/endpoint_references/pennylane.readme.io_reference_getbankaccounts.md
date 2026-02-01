---
url: "https://pennylane.readme.io/reference/getbankaccounts"
title: "List bank accounts"
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

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`

# `` 200      A list of bank accounts

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

name

string

required

currency

string

required

Defaults to EUR

`EUR` `USD` `GBP` `AED` `AFN` `ALL` `AMD` `ANG` `AOA` `ARS` `AUD` `AWG` `AZN` `BAM` `BBD` `BDT` `BGN` `BHD` `BIF` `BMD` `BND` `BOB` `BRL` `BSD` `BTN` `BWP` `BYN` `BYR` `BZD` `CAD` `CDF` `CHF` `CLF` `CLP` `CNY` `COP` `CRC` `CUC` `CUP` `CVE` `CZK` `DJF` `DKK` `DOP` `DZD` `EGP` `ERN` `ETB` `FJD` `FKP` `GEL` `GGP` `GHS` `GIP` `GMD` `GNF` `GTQ` `GYD` `HKD` `HNL` `HRK` `HTG` `HUF` `IDR` `ILS` `IMP` `INR` `IQD` `IRR` `ISK` `JEP` `JMD` `JOD` `JPY` `KES` `KGS` `KHR` `KMF` `KPW` `KRW` `KWD` `KYD` `KZT` `LAK` `LBP` `LKR` `LRD` `LSL` `LTL` `LVL` `LYD` `MAD` `MDL` `MGA` `MKD` `MMK` `MNT` `MOP` `MRO` `MUR` `MVR` `MWK` `MXN` `MYR` `MZN` `NAD` `NGN` `NIO` `NOK` `NPR` `NZD` `OMR` `PAB` `PEN` `PGK` `PHP` `PKR` `PLN` `PYG` `QAR` `RON` `RSD` `RUB` `RWF` `SAR` `SBD` `SCR` `SDG` `SEK` `SGD` `SHP` `SLL` `SOS` `SRD` `STD` `SVC` `SYP` `SZL` `THB` `TJS` `TMT` `TND` `TOP` `TRY` `TTD` `TWD` `TZS` `UAH` `UGX` `UYU` `UZS` `VEF` `VND` `VUV` `WST` `XAF` `XCD` `XDR` `XOF` `XPF` `YER` `ZAR` `ZMK` `ZMW` `ZWL`

created\_at

date-time

required

updated\_at

date-time

required

journal

object \| null

required

journal object \| null

ledger\_account

object

required

ledger\_account object

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

2     --url 'https://app.pennylane.com/api/external/v2/bank_accounts?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

21



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
7      "name": "Main account",\
\
8      "currency": "EUR",\
\
9      "created_at": "2023-08-30T10:08:08.146343Z",\
\
10      "updated_at": "2023-08-30T10:08:08.146343Z",\
\
11\
\
      "journal": {\
\
12        "id": 42,\
\
13        "url": "https://app.pennylane.com/api/external/v2/journals/7"\
\
14      },\
\
15\
\
      "ledger_account": {\
\
16        "id": 42,\
\
17        "url": "https://app.pennylane.com/api/external/v2/ledger_accounts/8"\
\
18      }\
\
19    }\
\
20  ]

21}

```

Updated about 1 month ago

* * *