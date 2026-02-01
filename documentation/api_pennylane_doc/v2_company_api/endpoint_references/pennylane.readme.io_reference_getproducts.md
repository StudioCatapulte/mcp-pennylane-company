---
url: "https://pennylane.readme.io/reference/getproducts"
title: "List products"
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

Available fields : `id`

Available operators : `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`

sort

string

Defaults to -id

You can choose to sort items on specific attributes

Sort field may be prefixed with `-` for descending order.

Example : `id` will sort by ascending order, `-id` will sort by descending order.

Available fields : `id`

# `` 200      A list of Products

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

label

string

required

Product label

description

string

required

Product description

external\_reference

string

required

The unique external reference assigned to this Product, assigned on creation either by you or Pennylane. (Same attribute as `source_id` in the API v1)

price\_before\_tax

string

required

Product price without taxes

vat\_rate

string

required

Product VAT rate. A 20% VAT in France is FR\_200.

`FR_1_05` `FR_1_75` `FR_09` `FR_21` `FR_40` `FR_55` `FR_60` `FR_65` `FR_85` `FR_92` `FR_100` `FR_130` `FR_15_385` `FR_196` `FR_200` `AD_10` `AD_45` `AD_95` `AT_100` `AT_130` `AT_200` `BE_60` `BE_120` `BE_210` `BG_90` `BG_200` `CH_25` `CH_26` `CH_37` `CH_38` `CH_77` `CH_81` `CY_50` `CY_90` `CY_190` `CZ_100` `CZ_120` `CZ_150` `CZ_210` `DE_70` `DE_190` `DK_250` `EE_90` `EE_200` `EE_220` `ES_40` `ES_100` `ES_210` `FI_100` `FI_140` `FI_240` `FI_255` `GB_50` `GB_200` `GR_60` `GR_130` `GR_240` `HR_50` `HR_130` `HR_250` `HU_50` `HU_180` `HU_270` `IE_48` `IE_90` `IE_135` `IE_210` `IE_230` `IT_40` `IT_50` `IT_100` `IT_220` `LT_50` `LT_90` `LT_210` `LU_30` `LU_70` `LU_80` `LU_130` `LU_140` `LU_160` `LU_170` `LV_50` `LV_120` `LV_210` `MC_09` `MC_21` `MC_55` `MC_85` `MC_100` `MC_200` `MT_50` `MT_70` `MT_180` `MU_150` `NL_90` `NL_210` `PL_50` `PL_80` `PL_230` `PT_60` `PT_130` `PT_230` `RO_50` `RO_90` `RO_190` `SE_60` `SE_120` `SE_250` `SI_50` `SI_95` `SI_220` `SK_100` `SK_200` `SK_230` `NO_120` `NO_150` `NO_250` `exempt` `extracom` `intracom_21` `intracom_55` `intracom_85` `intracom_100` `crossborder` `FR_85_construction` `FR_100_construction` `FR_200_construction` `mixed`

price

string

required

unit

string

required

Product unit

currency

string

required

Defaults to EUR

`EUR` `USD` `GBP` `AED` `AFN` `ALL` `AMD` `ANG` `AOA` `ARS` `AUD` `AWG` `AZN` `BAM` `BBD` `BDT` `BGN` `BHD` `BIF` `BMD` `BND` `BOB` `BRL` `BSD` `BTN` `BWP` `BYN` `BYR` `BZD` `CAD` `CDF` `CHF` `CLF` `CLP` `CNY` `COP` `CRC` `CUC` `CUP` `CVE` `CZK` `DJF` `DKK` `DOP` `DZD` `EGP` `ERN` `ETB` `FJD` `FKP` `GEL` `GGP` `GHS` `GIP` `GMD` `GNF` `GTQ` `GYD` `HKD` `HNL` `HRK` `HTG` `HUF` `IDR` `ILS` `IMP` `INR` `IQD` `IRR` `ISK` `JEP` `JMD` `JOD` `JPY` `KES` `KGS` `KHR` `KMF` `KPW` `KRW` `KWD` `KYD` `KZT` `LAK` `LBP` `LKR` `LRD` `LSL` `LTL` `LVL` `LYD` `MAD` `MDL` `MGA` `MKD` `MMK` `MNT` `MOP` `MRO` `MUR` `MVR` `MWK` `MXN` `MYR` `MZN` `NAD` `NGN` `NIO` `NOK` `NPR` `NZD` `OMR` `PAB` `PEN` `PGK` `PHP` `PKR` `PLN` `PYG` `QAR` `RON` `RSD` `RUB` `RWF` `SAR` `SBD` `SCR` `SDG` `SEK` `SGD` `SHP` `SLL` `SOS` `SRD` `STD` `SVC` `SYP` `SZL` `THB` `TJS` `TMT` `TND` `TOP` `TRY` `TTD` `TWD` `TZS` `UAH` `UGX` `UYU` `UZS` `VEF` `VND` `VUV` `WST` `XAF` `XCD` `XDR` `XOF` `XPF` `YER` `ZAR` `ZMK` `ZMW` `ZWL`

reference

string \| null

required

Product reference

ledger\_account

object \| null

required

ledger\_account object \| null

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url 'https://app.pennylane.com/api/external/v2/products?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

23



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
6      "id": 1,\
\
7      "label": "Product 1",\
\
8      "description": "This is product 1",\
\
9      "external_reference": "0e67fc3c-c632-4feb-ad34-e18ed5fbf66a",\
\
10      "price_before_tax": 12.5,\
\
11      "vat_rate": "FR_200",\
\
12      "price": 13.6,\
\
13      "unit": "piece",\
\
14      "currency": "EUR",\
\
15      "reference": "REF-123",\
\
16\
\
      "ledger_account": {\
\
17        "id": 0\
\
18      },\
\
19      "created_at": "2023-08-30T10:08:08.146343Z",\
\
20      "updated_at": "2023-08-30T10:08:08.146343Z"\
\
21    }\
\
22  ]

23}

```

Updated about 1 month ago

* * *