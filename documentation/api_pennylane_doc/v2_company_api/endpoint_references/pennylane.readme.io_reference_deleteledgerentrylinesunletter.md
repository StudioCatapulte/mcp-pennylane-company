---
url: "https://pennylane.readme.io/reference/deleteledgerentrylinesunletter"
title: "Unletter ledger entry lines"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

unbalanced\_lettering\_strategy

string

required

- `none`: the API won't let you create an unbalanced lettering


and will respond with an error.
- `partial`: a potentially unbalanced lettering will be created.

nonepartial

ledger\_entry\_lines

array of objects

required

length ≥ 1

The list of ledger entry lines you want to unletter.

ledger\_entry\_lines\*
object

id

integer

required

Id of the ledger entry line

ADD object

`` 204

No content

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

1curl --request DELETE \

2     --url https://app.pennylane.com/api/external/v2/ledger_entry_lines/lettering \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "unbalanced_lettering_strategy": "none"

8}

9'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 400`` 401`` 403`` 404`` 422

Updated 4 months ago

* * *