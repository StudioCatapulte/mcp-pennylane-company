---
url: "https://pennylane.readme.io/reference/getcategory"
title: "Retrieve a category"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

id

string

required

# `` 200      Returns a category

object

id

integer

required

label

string

required

direction

string \| null

required

`cash_in` `cash_out`

created\_at

date-time

required

updated\_at

date-time

required

category\_group

object

required

id

integer

required

analytical\_code

string \| null

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/categories/id \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

11



1

{

2  "id": 42,

3  "label": "Alimentaire",

4  "direction": "cash_in",

5  "created_at": "2023-08-30T10:08:08.146343Z",

6  "updated_at": "2023-08-30T10:08:08.146343Z",

7

  "category_group": {

8    "id": 348

9  },

10  "analytical_code": "CODE123"

11}

```

Updated about 1 month ago

* * *