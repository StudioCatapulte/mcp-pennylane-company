---
url: "https://firm-pennylane.readme.io/reference/company-dms-files"
title: "List Company's DMS Files"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

company\_id

integer

required

Existing company identifier (id)

cursor

string

Cursor for pagination. Use this to fetch the next set of results.

The cursor is an opaque string returned in the previous response's metadata.

Leave empty for the first request.

limit

integer

1 to 100

Number of items to return per request.

Defaults to 20 if not specified.

Must be between 1 and 100.

filter

string

You can choose to filter items on specific fields.

Available fields and values:

- `id`: `lt`, `lteq`, `gt`, `gteq`, `eq`, `not_eq`, `in`, `not_in`

# `` 200      Returns the list of DMS files of the company.

object

has\_more

boolean

required

Indicates whether additional results are available beyond this set.

Use this flag to determine if another request is needed.

next\_cursor

string \| null

required

Cursor to retrieve the next set of results.

Include this value in the cursor parameter of your next request to fetch subsequent items.

A `null` `next_cursor` in the response indicates no further results.

items

array of objects

required

items\*

object

id

integer

required

ID of the file

name

string

required

Name of the file

path

string

required

Path of the file

url

string

required

URL to download the file

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

Updated 21 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request GET \

2     --url https://app.pennylane.com/api/external/firm/v1/companies/company_id/dms/files \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200`` 400`` 401`` 403`` 404

Updated 21 days ago

* * *

Did this page help you?

Yes

No