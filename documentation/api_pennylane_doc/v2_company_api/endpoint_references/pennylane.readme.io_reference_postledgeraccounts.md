---
url: "https://pennylane.readme.io/reference/postledgeraccounts"
title: "Create a ledger account"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

number

string

required

Ledger Account's number.

If the number starts with 401 (supplier) or 411 (customer) a corresponding supplier or company customer will also be created.

label

string

required

Ledger Account's label

vat\_rate

string

FR\_1\_05FR\_1\_75FR\_09FR\_21FR\_40FR\_55FR\_60FR\_65FR\_85FR\_92FR\_100FR\_130FR\_15\_385FR\_196FR\_200AD\_10AD\_45AD\_95AT\_100AT\_130AT\_200BE\_60BE\_120BE\_210BG\_90BG\_200CH\_25CH\_37CH\_77CH\_26CH\_38CH\_81CY\_50CY\_90CY\_190CZ\_100CZ\_120CZ\_150CZ\_210DE\_70DE\_190DK\_250EE\_90EE\_200EE\_220ES\_40ES\_100ES\_210FI\_100FI\_140FI\_240FI\_255GB\_50GB\_200GR\_60GR\_130GR\_240HR\_50HR\_130HR\_250HU\_50HU\_180HU\_270IE\_48IE\_90IE\_135IE\_210IE\_230IT\_40IT\_50IT\_100IT\_220LT\_50LT\_90LT\_210LU\_30LU\_70LU\_80LU\_130LU\_140LU\_160LU\_170LV\_50LV\_120LV\_210MC\_09MC\_21MC\_55MC\_85MC\_100MC\_200MT\_50MT\_70MT\_180MU\_150NL\_90NL\_210PL\_50PL\_80PL\_230PT\_60PT\_130PT\_230RO\_50RO\_90RO\_190SE\_60SE\_120SE\_250SI\_50SI\_95SI\_220SK\_100SK\_200SK\_230NO\_120NO\_150NO\_250exemptextracomintracom\_21intracom\_55intracom\_85intracom\_100crossborderFR\_85\_constructionFR\_100\_constructionFR\_200\_constructionanymixed

country\_alpha2

string

ATBEBGCYCZDEDKEEESFIFRGRHRHUIEITLTLULVMTNLPLPTROSESISKGBMCCHADMUNOany

# `` 201      Returns the created ledger account

object

id

integer

required

number

string

required

label

string

required

vat\_rate

string

required

Ledger Account's VAT rate in percentage

country\_alpha2

string

required

Ledger Account's country code (alpha2)

enabled

boolean

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

# `` 422      Unprocessable entity

object

error

string

required

status

integer

required

Updated 4 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request POST \

2     --url https://app.pennylane.com/api/external/v2/ledger_accounts \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

```

xxxxxxxxxx



1

{

2  "id": 124,

3  "number": "512",

4  "label": "Secondary Account",

5  "vat_rate": "any",

6  "country_alpha2": "FR",

7  "enabled": true

8}

```

Updated 4 months ago

* * *