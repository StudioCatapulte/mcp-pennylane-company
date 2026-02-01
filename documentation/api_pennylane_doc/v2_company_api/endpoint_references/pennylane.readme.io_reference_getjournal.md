---
url: "https://pennylane.readme.io/reference/getjournal"
title: "Retrieve a journal"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

integer

required

# `` 200      Returns a journal

object

code

string

required

id

integer

required

label

string

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

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/journals/id \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx



1

{

2  "code": "string",

3  "id": 0,

4  "label": "string"

5}

```

Updated 3 months ago

* * *