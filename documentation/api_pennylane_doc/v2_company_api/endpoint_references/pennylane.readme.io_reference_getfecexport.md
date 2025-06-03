---
url: "https://pennylane.readme.io/reference/getfecexport"
title: "Retrieve a FEC export"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

integer

required

Existing export identifier (id)

# `` 200      Returns the export

object

id

integer

required

ID of the export

file\_url

string \| null

required

URL to download the export file. The URL will expire after 10 minutes.

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

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/exports/fecs/id \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx



1

{

2  "id": 124,

3  "file_url": "https://app.pennylane.com/my_export.xlsx",

4  "status": "pending",

5  "created_at": "2023-08-30T10:08:08.146343Z",

6  "updated_at": "2023-08-30T10:08:08.146343Z"

7}

```

Updated 4 months ago

* * *