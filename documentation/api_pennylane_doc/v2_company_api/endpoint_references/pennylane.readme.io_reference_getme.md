---
url: "https://pennylane.readme.io/reference/getme"
title: "User Profile"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

# `` 200      Returns the user and the company

object

user

object \| null

required

id

integer

required

first\_name

string

required

last\_name

string

required

email

string

required

locale

string

required

`fr` `en` `de`

company

object

required

id

integer

required

name

string

required

reg\_no

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

Updated 2 months ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/v2/me \

3     --header 'accept: application/json'

```

```

xxxxxxxxxx

14



1

{

2

  "user": {

3    "id": 12345,

4    "first_name": "John",

5    "last_name": "Doe",

6    "email": "jdoe@pennylane.com",

7    "locale": "fr"

8  },

9

  "company": {

10    "id": 123456,

11    "name": "Pennylane",

12    "reg_no": 123456789

13  }

14}

```

Updated 2 months ago

* * *