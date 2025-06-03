---
url: "https://pennylane.readme.io/reference/exportanalyticalgeneralledger"
title: "Create an Analytical General Ledger export"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

period\_start

date

required

Start date of the period to export

period\_end

date

required

End date of the period to export

mode

string

Defaults to in\_line

The mode of the export. The export can be in lines or in columns. If this parameter is not provided, it will use the default `in_line` mode.

in\_linein\_column

# `` 201      Returns the generated export status

object

id

integer

required

ID of the export

status

string

required

The state of the export

`pending` `ready` `error`

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

Updated 3 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request POST \

2     --url https://app.pennylane.com/api/external/v2/exports/analytical_general_ledgers \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '{"mode":"in_line"}'

```

```

xxxxxxxxxx



1

{

2  "id": 124,

3  "status": "pending",

4  "created_at": "2023-08-30T10:08:08.146343Z",

5  "updated_at": "2023-08-30T10:08:08.146343Z"

6}

```

Updated 3 months ago

* * *