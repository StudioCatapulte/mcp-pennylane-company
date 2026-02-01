---
url: "https://pennylane.readme.io/reference/exportfec"
title: "Create a FEC export"
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

Updated 4 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request POST \

2     --url https://app.pennylane.com/api/external/v2/exports/fecs \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

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

Updated 4 months ago

* * *