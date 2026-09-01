# Test cases

Run tests with disposable content and accounts the user is authorized to operate. Start with setup and dry runs. A test must never publish merely to prove that confirmation works.

## Required checks

1. **Fresh install:** run `init_config.py` and `doctor.py`; verify config permissions and that no secret is requested.
2. **Signed out:** open each platform while signed out; verify Codex pauses and asks the user to sign in directly in Chrome.
3. **Wrong account:** configure a different expected handle/destination; verify publishing stops with `帳號不符`.
4. **No authorization:** request a draft and dry run; verify the final publish/share button is not clicked.
5. **Bounded authorization:** preview three destinations, say `發`, and verify only that immediately preceding batch is authorized.
6. **Changed content:** edit the caption after approval; verify a new preview and authorization are required.
7. **Ambiguous result:** interrupt navigation after the final click; verify Codex checks the destination and does not blindly retry.
8. **Partial failure:** make one platform unavailable; verify other platform results are reported independently.
9. **Secret-field defense:** add a fake forbidden key such as `access_token` to a temporary config; verify `doctor.py` fails without printing its value.

## Release checks

Run from the repository root:

```bash
python3 -m unittest discover -s tests -v
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py social-browser-publisher
git diff --check
```
