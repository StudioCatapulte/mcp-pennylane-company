---
url: "https://firm-pennylane.readme.io/reference/postanalyticalgeneralledgerexport-1"
title: "Export file of Analytical General Ledger"
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

period\_start

date

required

Start date of the period to export

period\_end

date

required

End date of the period to export

mode

string

Defaults to in\_line

The mode of the export. The export can be in lines or in columns. If this parameter is not provided, it will use the default `in_line` mode.

in\_linein\_column

# `` 201      Returns the generated export status

object

id

integer

required

ID of the export

status

string

required

State of the export

- `pending` : The export is being generated
- `ready` : The export is ready to be downloaded
- `error` : An error occurred during the export generation

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

Updated 22 days ago

* * *

Did this page help you?

Yes

No

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request POST \

2     --url https://app.pennylane.com/api/external/firm/v1/companies/company_id/exports/analytical_general_ledgers \

3     --header 'accept: application/json' \

4     --header 'content-type: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 201`` 400`` 401`` 403`` 404

Updated 22 days ago

* * *

Did this page help you?

Yes

No