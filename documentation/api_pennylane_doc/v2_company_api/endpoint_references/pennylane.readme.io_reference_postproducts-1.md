---
url: "https://pennylane.readme.io/reference/postproducts-1"
title: "Create a product"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

label

string

required

Product label

description

string

Product description

external\_reference

string

You can use your own unique value when creating the product. If not provided, Pennylane will pick one for you. Value must be unique

price\_before\_tax

string

required

Product price without taxes

vat\_rate

string

required

Product VAT rate. A 20% VAT in France is FR\_200.

FR\_1\_05FR\_1\_75FR\_09FR\_21FR\_40FR\_55FR\_60FR\_65FR\_85FR\_92FR\_100FR\_130FR\_15\_385FR\_196FR\_200AD\_10AD\_45AD\_95AT\_100AT\_130AT\_200BE\_60BE\_120BE\_210BG\_90BG\_200CH\_25CH\_26CH\_37CH\_38CH\_77CH\_81CY\_50CY\_90CY\_190CZ\_100CZ\_120CZ\_150CZ\_210DE\_70DE\_190DK\_250EE\_90EE\_200EE\_220ES\_40ES\_100ES\_210FI\_100FI\_140FI\_240FI\_255GB\_50GB\_200GR\_60GR\_130GR\_240HR\_50HR\_130HR\_250HU\_50HU\_180HU\_270IE\_48IE\_90IE\_135IE\_210IE\_230IT\_40IT\_50IT\_100IT\_220LT\_50LT\_90LT\_210LU\_30LU\_70LU\_80LU\_130LU\_140LU\_160LU\_170LV\_50LV\_120LV\_210MC\_09MC\_21MC\_55MC\_85MC\_100MC\_200MT\_50MT\_70MT\_180MU\_150NL\_90NL\_210PL\_50PL\_80PL\_230PT\_60PT\_130PT\_230RO\_50RO\_90RO\_190SE\_60SE\_120SE\_250SI\_50SI\_95SI\_220SK\_100SK\_200SK\_230NO\_120NO\_150NO\_250exemptextracomintracom\_21intracom\_55intracom\_85intracom\_100crossborderFR\_85\_constructionFR\_100\_constructionFR\_200\_constructionmixed

unit

string

Product unit

currency

string

Defaults to EUR

EURUSDGBPAEDAFNALLAMDANGAOAARSAUDAWGAZNBAMBBDBDTBGNBHDBIFBMDBNDBOBBRLBSDBTNBWPBYNBYRBZDCADCDFCHFCLFCLPCNYCOPCRCCUCCUPCVECZKDJFDKKDOPDZDEGPERNETBFJDFKPGELGGPGHSGIPGMDGNFGTQGYDHKDHNLHRKHTGHUFIDRILSIMPINRIQDIRRISKJEPJMDJODJPYKESKGSKHRKMFKPWKRWKWDKYDKZTLAKLBPLKRLRDLSLLTLLVLLYDMADMDLMGAMKDMMKMNTMOPMROMURMVRMWKMXNMYRMZNNADNGNNIONOKNPRNZDOMRPABPENPGKPHPPKRPLNPYGQARRONRSDRUBRWFSARSBDSCRSDGSEKSGDSHPSLLSOSSRDSTDSVCSYPSZLTHBTJSTMTTNDTOPTRYTTDTWDTZSUAHUGXUYUUZSVEFVNDVUVWSTXAFXCDXDRXOFXPFYERZARZMKZMWZWL

reference

string

Product reference

ledger\_account\_id

integer

# `` 201      The created product

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

id

integer

required

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

2     --url https://app.pennylane.com/api/external/v2/products \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "vat_rate": "FR_1_05",

8  "currency": "EUR"

9}

10'

```

```

xxxxxxxxxx

17



1

{

2  "id": 1,

3  "label": "Product 1",

4  "description": "This is product 1",

5  "external_reference": "0e67fc3c-c632-4feb-ad34-e18ed5fbf66a",

6  "price_before_tax": 12.5,

7  "vat_rate": "FR_200",

8  "price": 13.6,

9  "unit": "piece",

10  "currency": "EUR",

11  "reference": "REF-123",

12

  "ledger_account": {

13    "id": 0

14  },

15  "created_at": "2023-08-30T10:08:08.146343Z",

16  "updated_at": "2023-08-30T10:08:08.146343Z"

17}

```

Updated about 1 month ago

* * *