---
url: "https://firm-pennylane.readme.io/reference/getdmsfileschanges"
title: "Get DMS files changes events"
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

Cursor for pagination. Use this to fetch the next set of results. The cursor is an opaque string returned in the previous response's metadata. Leave empty for the first request.

limit

integer

1 to 1000

Number of items to return per request.

Defaults to 20 if not specified.

Must be between 1 and 1000.

start\_date

date-time

Filter the changes based on the event date. The date should follow RFC3339 format. If no date is provided, the oldest changes will be returned. Changes for the last 4 weeks are retained, thus providing a `start_date` older than that will result in a 422 response. Providing both `start_date` and `cursor` parameters will result in a 400 response.

# `` 200      A list of DMS files changes

object

items

array of objects

required

items\*

object

id

integer

required

Unique identifier of the dms file record

operation

string

required

`insert` `update` `delete`

processed\_at

date-time

required

Timestamp when the event arrived in the change log pipeline

updated\_at

date-time

required

Timestamp when the record was updated in the database (can vary due to data restoration)

created\_at

date-time

required

Timestamp when the record was initially created

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

`` 500

Internal server error

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

2     --url https://app.pennylane.com/api/external/firm/v1/companies/company_id/changelogs/dms_files \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200`` 400`` 401`` 403`` 404`` 422

Updated 21 days ago

* * *

Did this page help you?

Yes

No