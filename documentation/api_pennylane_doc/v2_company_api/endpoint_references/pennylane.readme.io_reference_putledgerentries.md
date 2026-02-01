---
url: "https://pennylane.readme.io/reference/putledgerentries"
title: "Update a ledger entry"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

string

required

date

date

> `date-time` format is deprecated. **Please use `date` format (ISO 8601)**.

label

string

Label that describes the ledger entry

journal\_id

integer

The journal ID where you want to create the ledger entry

ledger\_attachment\_id

integer

Ledger attachment ID

currency

string

Currency code of the ledger entry as per ISO 4217. This currency is applicable to all ledger\_entry\_lines

EUREURUSDGBPAEDAFNALLAMDANGAOAARSAUDAWGAZNBAMBBDBDTBGNBHDBIFBMDBNDBOBBRLBSDBTNBWPBYNBYRBZDCADCDFCHECHFCLFCLPCNYCOPCRCCUCCUPCVECZKDJFDKKDOPDZDEGPERNETBFJDFKPGELGGPGHSGIPGMDGNFGTQGYDHKDHNLHRKHTGHUFIDRILSIMPINRIQDIRRISKJEPJMDJODJPYKESKGSKHRKMFKPWKRWKWDKYDKZTLAKLBPLKRLRDLSLLTLLVLLYDMADMDLMGAMKDMMKMNTMOPMROMRUMURMVRMWKMXNMYRMZNNADNGNNIONOKNPRNZDOMRPABPENPGKPHPPKRPLNPYGQARRONRSDRUBRWFSARSBDSCRSDGSEKSGDSHPSLLSOSSRDSTDSVCSYPSZLTHBTJSTMTTNDTOPTRYTTDTWDTZSUAHUGXUYUUZSVEFVNDVUVWSTXAFXCDXDRXOFXPFYERZARZMKZMWZWL

ledger\_entry\_lines

object

Add, update, delete ledger entry lines. The entry lines must be balanced.

**In total**, max number of entry lines that you can create, update or delete using this endpoint is 1000 per request.

ledger\_entry\_lines object

# `` 200      Returns the updated ledger entry

object

id

integer

required

ID of the ledger entry

label

string

required

Label that describes the ledger entry

date

date

required

Date of the ledger entry (ISO 8601)

journal\_id

integer

required

The journal ID where the ledger entry was created

ledger\_attachment\_filename

string \| null

required

Attachment's filename

ledger\_attachment\_id

integer \| null

required

Ledger attachment ID

ledger\_entry\_lines

array of objects

required

Array of entry lines

ledger\_entry\_lines\*

object

id

integer

required

ID of the entry line

debit

string

required

Debit amount for the entry line

credit

string

required

Credit amount for the entry line

ledger\_account\_id

integer

required

Ledger account ID

label

string

required

Label that describes the entry line

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

1curl --request PUT \

2     --url https://app.pennylane.com/api/external/v2/ledger_entries/id \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

```

xxxxxxxxxx

17



1

{

2  "id": 1,

3  "label": "Payment for Services",

4  "date": "2023-08-30",

5  "journal_id": 123,

6  "ledger_attachment_filename": "filename.pdf",

7  "ledger_attachment_id": 42,

8

  "ledger_entry_lines": [\
\
9\
\
    {\
\
10      "id": 42,\
\
11      "debit": "100.00",\
\
12      "credit": "0.00",\
\
13      "ledger_account_id": 987,\
\
14      "label": "Transaction label"\
\
15    }\
\
16  ]

17}

```

Updated 4 months ago

* * *