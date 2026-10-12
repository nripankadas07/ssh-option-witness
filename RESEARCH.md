# Qualitative research — 12 October 2026

Observed 2026-10-12 06:35:23 UTC. Search queries: `ssh config parser sort:stars-desc; ssh_config sort:stars-desc`.

GitHub search requested star ordering through query qualifiers. Direct repository-search REST fetch was unsupported; connector results were noisy and some irrelevant matches were rejected. Established adjacent tools were added explicitly, with current repository metadata, README and three recent open issue/PR records inspected. Ranking is the highest-star relevant comparable among these found sources, not an exhaustive global ranking. Code inspected for one relevant comparable in each area; complete competitor installations and full feature inventories were not tested.

| Repository | Stars | Last pushed UTC | API license |
| --- | ---: | --- | --- |
| [paramiko/paramiko](https://github.com/paramiko/paramiko) | 9879 | 2026-10-10T21:28:12Z | LGPL-2.1 |
| [openssh/openssh-portable](https://github.com/openssh/openssh-portable) | 4040 | 2026-10-11T10:29:08Z | NOASSERTION |
| [kevinburke/ssh_config](https://github.com/kevinburke/ssh_config) | 476 | 2026-05-04T16:41:02Z | NOASSERTION |

Highest-star relevant/adjacent source found in this inspected set: paramiko/paramiko.

Paramiko is a Python SSH implementation, OpenSSH is the authoritative complete client/server implementation, and ssh_config parses and preserves configuration, with single and additive retrieval APIs. This candidate explains a small configuration subset offline. It has no Include, Match, expansion, connection or execution behavior. Unsupported directives fail even in unmatched blocks, preventing incomplete analysis being presented as a complete SSH configuration.

Installability, examples and support were assessed from current README/issue evidence. No measured time-to-result, reliability ranking, comparative speed or superiority claim is made. Our offline installed example passes; that establishes our behavior only. Specific demand remains inferred, as stated in README. All implementation code is original; no third-party source or prose was imported.

## Current evidence links

- paramiko/paramiko: [README](https://github.com/paramiko/paramiko/blob/main/README.rst), observed blob `53129721c2a4c9a310aa0ef2c44d64d1dd329efc`.
  - [PR](https://github.com/paramiko/paramiko/pull/2702) — Preserve extended SFTP attribute names and values
  - [PR](https://github.com/paramiko/paramiko/pull/2701) — Fix Ed25519Key.write_private_key_file AttributeError
  - [issue](https://github.com/paramiko/paramiko/issues/2700) — [BUG] - Error writing Ed25519Key to file
- openssh/openssh-portable: [README](https://github.com/openssh/openssh-portable/blob/master/README.md), observed blob `c7c0805211c1689e83a0881e4c1fda30393f127a`.
  - [PR](https://github.com/openssh/openssh-portable/pull/716) — obvious issue in check of a newline
  - [PR](https://github.com/openssh/openssh-portable/pull/715) — Add utmps support, the utmps implementation for musl libc
  - [PR](https://github.com/openssh/openssh-portable/pull/714) — Load a trust anchor file before validating DNSSEC
- kevinburke/ssh_config: [README](https://github.com/kevinburke/ssh_config/blob/master/README.md), observed blob `705605e2fd7835535082e53bd276038211e8ebb4`.
  - [PR](https://github.com/kevinburke/ssh_config/pull/92) — feat: add ToClientConfig helper to convert parsed host configuration to ssh.ClientConfig
  - [PR](https://github.com/kevinburke/ssh_config/pull/91) — feat: add ClientConfig helper for ssh.ClientConfig construction
  - [issue](https://github.com/kevinburke/ssh_config/issues/90) — Feature Request: Return `ssh.ClientConfig`
