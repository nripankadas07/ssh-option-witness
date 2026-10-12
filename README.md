# ssh-option-witness

Public alpha prepared on 12 October 2026. **Remote verification pending; not yet a verified launch.**
Original Python implementation, MIT, zero runtime dependencies. AI-assisted development.

Developer debugging host-specific SSH client settings. Show which matching declaration supplied a value without connecting or executing commands.

Strict documented Host/option subset, first scalar value and additive identity files, with source line trace and skipped override reasons.

## Install and first useful result

Python 3.10+ (only Linux Python 3.12.14 tested in this preparation). Build requires setuptools 61+ and wheel already available; install into a fresh venv uses only the generated wheel. Run source tests with your build interpreter:

```sh
python -m pip wheel --no-index --no-deps --no-build-isolation --wheel-dir wheelhouse .
python -m venv .venv
.venv/bin/python -m pip install --no-index --no-deps wheelhouse/*.whl
.venv/bin/ssh-option-witness example.json
python -m unittest -v
```

The included synthetic input documents the exact normalized JSON schema.
Output is deterministic JSON; malformed inputs exit 2. Inputs are limited to 1 MiB.
No network connections, credential reads or writes to input files occur.
Hostnames, identifiers, paths and selected SSH values may be disclosed in output.
Review exported inputs and outputs before sharing. Use synthetic examples for reports.

## Scope and limits

No full OpenSSH emulation, includes, token expansion, command execution, filesystem lookup or connections.

Specific demand: Inferred from OpenSSH configuration semantics and established parser workflows; no verified request.
Discovery: SSH configuration troubleshooting examples.
Portfolio distinction: Existing network tools do not resolve host declarations.
See RESEARCH.md and the bundled research record for alternatives and incomplete research coverage.
No competitor absence, performance superiority or customer-adoption claim.

## Acceptance criteria

- Positive and negated host patterns, case-insensitive host matching.
- Earlier scalar wins; additive identity files preserve declaration order.
- Reject Include, Match and unsupported options rather than ignoring them.

## Support and contribution

Report a reproducible synthetic input, expected result, actual output and Python version.
Keep changes bounded and run the unit suite and clean installed example.
Do not submit private host configuration, production metric labels or credentials.
Security reports should omit secrets; this offline diagnostic is not a security boundary.
The source distribution is the supported install path; no registry release is claimed.
