---
url: "https://firm-pennylane.readme.io/reference/companies-1"
title: "List companies"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

page

integer

Items are paginated, this is the current page which will be returned. The page index is starting at 1.

per\_page

integer

1 to 1000

Items are paginated. By default, you get 20 items per page. You can specify another number of items per page.

# `` 200      Returns a list of companies related to the firm the access token is associated with.

object

items

array of objects

required

items\*

object

id

integer

required

Company's unique identifier

name

string

required

Company's legal name.

billing\_company\_name

string

required

Company's trade name.

siren

string

required

Company's SIREN

address

string

required

The number and street address of the company.

city

string

required

The city the company is in.

postal\_code

string

required

The postal/zip code of the company.

activity\_nomenclature

string

required

The activity nomenclature code, e.g. "code NAF" in France.

external\_id

string

required

The external identifier of the company.

total\_pages

integer

required

The total number of pages available

current\_page

integer

required

The current page returned

total\_items

integer

required

The total number of items available

per\_page

integer

required

The number of items per page

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

1curl --request GET \

2     --url https://app.pennylane.com/api/external/firm/v1/companies \

3     --header 'accept: application/json'

```

Click `Try It!` to start a request and see the response here! Or choose an example:

application/json

`` 200`` 401`` 403`` 404

Updated 22 days ago

* * *

Did this page help you?

Yes

No