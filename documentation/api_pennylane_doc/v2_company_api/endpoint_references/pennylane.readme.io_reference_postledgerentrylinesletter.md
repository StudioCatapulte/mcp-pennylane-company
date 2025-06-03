---
url: "https://pennylane.readme.io/reference/postledgerentrylinesletter"
title: "Letter ledger entry lines"
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

length ≥ 2

The list of ledger entry lines you want to letter together.

You can provide ledger entry lines already lettered and they don't have to be part of the same lettering.

All received entry lines will be lettered together. If a passed entry line is already lettered, then the lettering will be applied to its lettered entry lines as well. For example:

Ledger entry lines `A` and `B` are already lettered together. `C` in not lettered.

When requesting `[A, C]` to be lettered, the final lettering will be `[A, B, C]`.

ledger\_entry\_lines\*
object

id

integer

required

Id of the ledger entry line

object

id

integer

required

Id of the ledger entry line

ADD object

# `` 200      Returns all the ledger entry lines of the new lettering

array of objects

object

id

integer

required

Id of the ledger entry line

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

2     --url https://app.pennylane.com/api/external/v2/ledger_entry_lines/lettering \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json' \

5     --data '

6{

7  "unbalanced_lettering_strategy": "none"

8}

9'

```

```

xxxxxxxxxx



1

[\
\
2\
\
  {\
\
3    "id": 1\
\
4  }\
\
5]

```

Updated 4 months ago

* * *