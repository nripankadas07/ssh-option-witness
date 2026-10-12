# Synthetic demo

Use the installed command with `example.json`; the expected deterministic output is:

```json
{
  "host": "demo.dev",
  "trace": [
    {
      "keyword": "host",
      "line": 1,
      "matched": true
    },
    {
      "keyword": "user",
      "line": 2,
      "reason": "selected"
    },
    {
      "keyword": "port",
      "line": 3,
      "reason": "selected"
    },
    {
      "keyword": "identityfile",
      "line": 4,
      "reason": "appended"
    },
    {
      "keyword": "host",
      "line": 5,
      "matched": true
    },
    {
      "keyword": "user",
      "line": 6,
      "reason": "earlier_value_wins"
    },
    {
      "keyword": "identityfile",
      "line": 7,
      "reason": "appended"
    }
  ],
  "values": {
    "identityfile": [
      "example-a",
      "example-b"
    ],
    "port": "2222",
    "user": "synthetic"
  }
}
```

This proves the documented example only, not production efficacy or adoption.
