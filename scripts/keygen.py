"""
GEM Content Engine — license key generator.

Deterministic HMAC-SHA256 from a per-environment secret + the order ID.
Same order ID always produces the same key, so you never need a database
to recover a key — re-derive it from the order ID.

Usage:
    export GEM_KEYGEN_SECRET="a-long-random-string-kept-out-of-git"
    python scripts/keygen.py gumroad-order-12345
    # GEM-7B3C-91F0-4A2E-D8B6

Verify a quoted key:
    python scripts/keygen.py --verify gumroad-order-12345 GEM-7B3C-91F0-4A2E-D8B6

Rotate the secret only if you have a known leak. Rotating invalidates
every previously-issued key.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import os
import sys


def _secret() -> bytes:
    s = os.environ.get('GEM_KEYGEN_SECRET')
    if not s:
        sys.exit(
            'GEM_KEYGEN_SECRET is not set. Export it before running:\n'
            '    export GEM_KEYGEN_SECRET="<a-long-random-string>"\n'
            'Keep this value out of Git.'
        )
    return s.encode('utf-8')


def make_key(order_id: str) -> str:
    """Return the canonical GEM-XXXX-XXXX-XXXX-XXXX license key for an order."""
    raw = hmac.new(_secret(), order_id.encode('utf-8'), hashlib.sha256).hexdigest()
    chunks = (raw[0:4], raw[4:8], raw[8:12], raw[12:16])
    return 'GEM-' + '-'.join(c.upper() for c in chunks)


def verify_key(order_id: str, claimed_key: str) -> bool:
    """Constant-time equality between the recomputed key and what the buyer quoted."""
    return hmac.compare_digest(make_key(order_id), claimed_key.strip())


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description='GEM license key generator / verifier.')
    p.add_argument('order_id', help='Order ID from Gumroad / Lemon Squeezy / Stripe.')
    p.add_argument('claimed_key', nargs='?', default=None,
                   help='If provided, verify this key against the order ID.')
    p.add_argument('--verify', action='store_true',
                   help='Force verify mode (alias for providing a second positional arg).')
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    if args.claimed_key or args.verify:
        if not args.claimed_key:
            sys.exit('--verify requires a key as the second positional argument.')
        ok = verify_key(args.order_id, args.claimed_key)
        print('valid' if ok else 'INVALID')
        sys.exit(0 if ok else 1)
    print(make_key(args.order_id))


if __name__ == '__main__':
    main()
