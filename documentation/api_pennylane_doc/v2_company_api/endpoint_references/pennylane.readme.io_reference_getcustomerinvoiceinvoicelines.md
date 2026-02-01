---
url: "https://pennylane.readme.io/reference/getcustomerinvoiceinvoicelines"
title: "List invoice lines for a customer invoice"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

customer\_invoice\_id

integer

required

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

# `` 200      Returns the list of invoice lines for a customer invoice

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

number

required

Invoice line id

label

string

required

Invoice line label

unit

string \| null

required

The kind of unit which applies to the amount

quantity

string

required

Invoice line item quantity (number of items)

amount

string

required

The total amount of the invoice lines in euros including taxes and deducting discounts

currency\_amount

string

required

The total amount of the invoice lines in the document's currency including taxes and deducting discounts.

If the currency is euro, amount and currency\_amount are identical.

description

string

required

Invoice line description

product

object \| null

required

product object \| null

vat\_rate

string

required

Product VAT rate. A 20% VAT in France is FR\_200.

`FR_1_05` `FR_1_75` `FR_09` `FR_21` `FR_40` `FR_55` `FR_60` `FR_65` `FR_85` `FR_92` `FR_100` `FR_130` `FR_15_385` `FR_196` `FR_200` `AD_10` `AD_45` `AD_95` `AT_100` `AT_130` `AT_200` `BE_60` `BE_120` `BE_210` `BG_90` `BG_200` `CH_25` `CH_26` `CH_37` `CH_38` `CH_77` `CH_81` `CY_50` `CY_90` `CY_190` `CZ_100` `CZ_120` `CZ_150` `CZ_210` `DE_70` `DE_190` `DK_250` `EE_90` `EE_200` `EE_220` `ES_40` `ES_100` `ES_210` `FI_100` `FI_140` `FI_240` `FI_255` `GB_50` `GB_200` `GR_60` `GR_130` `GR_240` `HR_50` `HR_130` `HR_250` `HU_50` `HU_180` `HU_270` `IE_48` `IE_90` `IE_135` `IE_210` `IE_230` `IT_40` `IT_50` `IT_100` `IT_220` `LT_50` `LT_90` `LT_210` `LU_30` `LU_70` `LU_80` `LU_130` `LU_140` `LU_160` `LU_170` `LV_50` `LV_120` `LV_210` `MC_09` `MC_21` `MC_55` `MC_85` `MC_100` `MC_200` `MT_50` `MT_70` `MT_180` `MU_150` `NL_90` `NL_210` `PL_50` `PL_80` `PL_230` `PT_60` `PT_130` `PT_230` `RO_50` `RO_90` `RO_190` `SE_60` `SE_120` `SE_250` `SI_50` `SI_95` `SI_220` `SK_100` `SK_200` `SK_230` `NO_120` `NO_150` `NO_250` `exempt` `extracom` `intracom_21` `intracom_55` `intracom_85` `intracom_100` `crossborder` `FR_85_construction` `FR_100_construction` `FR_200_construction` `mixed`

currency\_amount\_before\_tax

string

required

Total amount before tax in currency

currency\_tax

string

required

Total tax amount in currency

tax

string

required

Total tax amount in euros

raw\_currency\_unit\_price

string

required

Unit price (excluding tax)

discount

object

required

discount object

section\_rank

integer \| null

required

Has to correspond to the rank number of a line items section in which the line item should be

imputation\_dates

object \| null

required

imputation\_dates object \| null

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

2     --url 'https://app.pennylane.com/api/external/v2/customer_invoices/customer_invoice_id/invoice_lines?sort=-id' \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

35
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
6      "id": 444,\
\
7      "label": "Demo label",\
\
8      "unit": "piece",\
\
9      "quantity": "12",\
\
10      "amount": "50.4",\
\
11      "currency_amount": "50.4",\
\
12      "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor",\
\
13\
\
      "product": {\
\
14        "id": 3049,\
\
15        "url": "https://app.pennylane.com/api/external/v2/products/42"\
\
16      },\
\
17      "vat_rate": "FR_200",\
\
18      "currency_amount_before_tax": "30",\
\
19      "currency_tax": "10",\
\
20      "tax": "10",\
\
21      "raw_currency_unit_price": "5",\
\
22\
\
      "discount": {\
\
23        "type": "absolute",\
\
24        "value": 25\
\
25      },\
\
```\
\
Updated about 1 month ago\
\
* * *