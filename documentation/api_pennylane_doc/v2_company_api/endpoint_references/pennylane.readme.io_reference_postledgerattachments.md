---
url: "https://pennylane.readme.io/reference/postledgerattachments"
title: "Upload a file"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

file

file

required

The file you want to upload.

Allowed content types:

- image/png
- image/jpeg
- image/tiff
- image/bmp
- image/gif
- application/pdf

filename

string

# `` 201      Returns the created attachment

object

url

string

required

id

integer

required

filename

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

Updated about 1 month ago

* * *

ShellNodeRubyPHPPython

Bearer

```

xxxxxxxxxx

1curl --request POST \

2     --url https://app.pennylane.com/api/external/v2/ledger_attachments \

3     --header 'accept: application/json' \

4     --header 'content-type: multipart/form-data'

```

```

xxxxxxxxxx



1

{

2  "url": "string",

3  "id": 0,

4  "filename": "string"

5}

```

Updated about 1 month ago

* * *