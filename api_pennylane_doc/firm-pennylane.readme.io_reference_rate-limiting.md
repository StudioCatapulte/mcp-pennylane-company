---
url: "https://firm-pennylane.readme.io/reference/rate-limiting"
title: "Rate Limiting"
---

Pennylane API relies on rate limits to ensure stability and reliability. Rate limiting is enabled on both production and sandbox environments and all endpoints are affected.

You are allowed to make 4 API calls (requests) per second.

If you go over this limit, you will receive a 429 HTTP Error :

Text

```rdmd-code lang-text theme-light

You made too many requests. Retry in 60s !

```

Updated 5 months ago

* * *

Did this page help you?

Yes

No

Updated 5 months ago

* * *

Did this page help you?

Yes

No