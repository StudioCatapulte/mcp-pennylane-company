---
url: "https://pennylane.readme.io/reference/getledgerentryline"
title: "Retrieve a Ledger entry line"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

integer

required

# `` 200      A ledger entry line

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

label

string

required

Label that describes the entry line

ledger\_account

object

required

id

integer

required

Ledger account ID

url

string

required

The URL to the ledger account

journal

object

required

id

integer

required

Journal ID

url

string

required

The URL to the journal

date

date

required

Date of the ledger entry line (ISO 8601)

ledger\_entry

object

required

id

integer

required

The ledger entry ID of the ledger entry line

lettered\_ledger\_entry\_lines

object

required

Ledger entry lines that are lettered with this entry line.

ids

array of integers

required

IDs of all ledger entry lines that share the same lettering, including the ID of this entry line itself. Will be empty if this entry line is not lettered.

ids\*

url

string

required

URL to fetch the lettered ledger entry lines.

created\_at

date-time

required

The time the entry line has been created

updated\_at

date-time

required

The last time the entry line has been updated

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

2     --url https://app.pennylane.com/api/external/v2/ledger_entry_lines/id \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

27
}

1

{

2  "id": 42,

3  "debit": "100.00",

4  "credit": "0.00",

5  "label": "Employees - Jean Dupont / Salary May 2023",

6

  "ledger_account": {

7    "id": 987,

8    "url": "https://app.pennylane.com/api/external/v2/ledger_accounts/42"

9  },

10

  "journal": {

11    "id": 123,

12    "url": "https://app.pennylane.com/api/external/v2/journals/42"

13  },

14  "date": "2023-08-30",

15

  "ledger_entry": {

16    "id": 123001

17  },

18

  "lettered_ledger_entry_lines": {

19

    "ids": [\
\
20      42,\
\
21      1271004\
\
22    ],

23    "url": "https://app.pennylane.com/api/external/v2/ledger_entry_lines/42/lettered_ledger_entry_lines"

24  },

25  "created_at": "2023-08-30T10:08:08.146343Z",

```

Updated about 1 month ago

* * *