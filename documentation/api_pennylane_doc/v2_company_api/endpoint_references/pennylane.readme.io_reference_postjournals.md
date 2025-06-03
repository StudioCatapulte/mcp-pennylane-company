---
url: "https://pennylane.readme.io/reference/postjournals"
title: "Create a journal"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

code

string

required

2 to 5 letters that represents the journal

label

string

required

Label that describes the journal

# `` 201      Returns the created journal

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

2     --url https://app.pennylane.com/api/external/v2/journals \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

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

Updated 4 months ago

* * *