---
url: "https://pennylane.readme.io/reference/postcustomerinvoiceappendices"
title: "Upload an appendix for a customer invoice"
---

| time | status | user agent |  |
| :-- | :-- | :-- | :-- |
| Make a request to see history. |

#### URL Expired

The URL for this request expired after 30 days.

customer\_invoice\_id

integer

required

file

file

required

The appendix file you want to upload.

Allowed content types:

- image/png
- image/jpeg
- image/tiff
- image/bmp
- image/gif
- application/pdf

# `` 201      Returns the created appendix

object

id

integer

required

url

string

required

URL to the uploaded file.

filename

string

required

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

# `` 422      Unprocessable entity

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

2     --url https://app.pennylane.com/api/external/v2/customer_invoices/customer_invoice_id/appendices \

3     --header 'accept: application/json' \

4     --header 'content-type: multipart/form-data'

```

```

xxxxxxxxxx



1

{

2  "id": 0,

3  "url": "https://www.pennylane.com/rails/active_storage/blobs/redirect/eyJfc..==--26d6e7391dd728fae2cde59bd3fbe4dd11e20a95/Invoice42.pdf",

4  "filename": "string",

5  "created_at": "2023-08-30T10:08:08.146343Z",

6  "updated_at": "2023-08-30T10:08:08.146343Z"

7}

```

Updated about 1 month ago

* * *