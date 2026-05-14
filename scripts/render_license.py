"""
GEM Content Engine — render a per-order LICENSE.txt.

For manual or semi-automated fulfillment paths where you want a buyer-specific
LICENSE.txt inside their ZIP (instead of the generic dist/LICENSE.template.txt
that ships with every Gumroad auto-fulfillment).

Usage:
    export GEM_KEYGEN_SECRET="..."
    python scripts/render_license.py gumroad-order-12345 buyer@example.com --tier "Founder's Edition"
    # writes LICENSE.txt to stdout; redirect to a file:
    python scripts/render_license.py gumroad-order-12345 buyer@example.com > LICENSE.txt

Or import as a module:
    from scripts.render_license import render
    print(render('gumroad-order-12345', 'buyer@example.com'))
"""
from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

# Local import — works when run as a script from the repo root.
sys.path.insert(0, str(Path(__file__).parent))
from keygen import make_key  # noqa: E402

VERSION = 'v1.7'


def render(order_id: str, email: str, tier: str = "Founder's Edition",
           purchased_at: str | None = None) -> str:
    if purchased_at is None:
        purchased_at = datetime.date.today().isoformat()
    key = make_key(order_id)
    return f"""GEM Content Engine — License

License key:    {key}
Order ID:       {order_id}
Licensee:       {email}
Tier:           {tier}
Purchased:      {purchased_at}
Version:        {VERSION}

License grant
-------------
This license grants you a perpetual, worldwide, non-exclusive,
non-transferable right to use GEM Content Engine for personal and
commercial content creation. Use it for your own brand, your clients,
your agency, and your team.

Lifetime updates within the v1.x major version.
Founder's Edition includes the commercial-use license.

Restrictions
------------
You may not redistribute, resell, sublicense, or share the gem.html
file with anyone outside your purchased seat count. White-label
rebranding is reserved for future tiers.

Output ownership
----------------
You own everything you create with GEM. We have no server and never
see your prompts, scripts, or generated assets.

Full terms:    https://thegeminfo.com/terms.html
Privacy:       https://thegeminfo.com/privacy.html

Support
-------
General:       hello@thegeminfo.com
Privacy:       privacy@thegeminfo.com
Legal:         legal@thegeminfo.com

Quote your license key above when contacting support.

— The GEM team
  thegeminfo.com · {VERSION}
"""


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description='Render a per-order LICENSE.txt for GEM.')
    p.add_argument('order_id', help='Order ID from Gumroad / Lemon Squeezy / Stripe.')
    p.add_argument('email', help='Buyer email address.')
    p.add_argument('--tier', default="Founder's Edition",
                   help="Tier label (default: Founder's Edition).")
    p.add_argument('--purchased-at', default=None,
                   help='ISO date (default: today).')
    p.add_argument('--output', '-o', default=None,
                   help='Write to file instead of stdout.')
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    text = render(args.order_id, args.email, args.tier, args.purchased_at)
    if args.output:
        Path(args.output).write_text(text, encoding='utf-8')
        print(f'Wrote {args.output}', file=sys.stderr)
    else:
        sys.stdout.write(text)


if __name__ == '__main__':
    main()
