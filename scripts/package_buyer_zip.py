"""
GEM Content Engine — build the buyer ZIP.

Cross-platform Python replacement for the Bash snippet in
GEM-Fulfillment-Playbook.pdf Appendix B.1. Produces a single ZIP suitable for
upload to Gumroad / Lemon Squeezy / Stripe-fulfilled checkouts.

Usage:
    python scripts/package_buyer_zip.py
    # → GEM-Content-Engine-v1.7.zip in the repo root

    python scripts/package_buyer_zip.py --version v1.8 --output dist/GEM-Content-Engine-v1.8.zip

Contents of the ZIP:
    gem.html                  — the product
    GEM-User-Manual.pdf       — full user manual
    WELCOME.md                — 60-second start guide
    LICENSE.txt               — generic license template (key arrives via receipt email)
    CHANGELOG.txt             — customer-facing changelog

For a per-order ZIP with the buyer's actual key in LICENSE.txt, run
scripts/render_license.py to overwrite LICENSE.txt before zipping.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

VERSION = 'v1.7'
REPO_ROOT = Path(__file__).resolve().parent.parent


def _ensure(p: Path) -> Path:
    if not p.exists():
        sys.exit(f'Missing source file: {p}')
    return p


def build(version: str, output: Path, license_override: Path | None = None) -> None:
    sources: list[tuple[Path, str]] = [
        (_ensure(REPO_ROOT / 'gem.html'), 'gem.html'),
        (_ensure(REPO_ROOT / 'GEM-User-Manual.pdf'), 'GEM-User-Manual.pdf'),
        (_ensure(REPO_ROOT / 'dist' / 'WELCOME.md'), 'WELCOME.md'),
        (_ensure(REPO_ROOT / 'dist' / 'CHANGELOG.txt'), 'CHANGELOG.txt'),
    ]
    if license_override:
        sources.append((_ensure(license_override), 'LICENSE.txt'))
    else:
        sources.append(
            (_ensure(REPO_ROOT / 'dist' / 'LICENSE.template.txt'), 'LICENSE.txt')
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for src, name_in_zip in sources:
            zf.write(src, arcname=name_in_zip)

    size_kb = output.stat().st_size / 1024
    print(f'Built {output} ({size_kb:.1f} KB)')
    print('Contents:')
    for _, name in sources:
        print(f'  - {name}')


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description='Build the GEM buyer ZIP.')
    p.add_argument('--version', default=VERSION, help=f'Version tag (default: {VERSION}).')
    p.add_argument('--output', '-o', default=None,
                   help='Output path (default: GEM-Content-Engine-<version>.zip in repo root).')
    p.add_argument('--license', default=None,
                   help='Path to a pre-rendered LICENSE.txt to use instead of the generic template '
                        '(produced by scripts/render_license.py for per-order ZIPs).')
    return p.parse_args()


def main() -> None:
    args = _parse_args()
    output = Path(args.output) if args.output else REPO_ROOT / f'GEM-Content-Engine-{args.version}.zip'
    license_override = Path(args.license) if args.license else None
    build(args.version, output, license_override)


if __name__ == '__main__':
    main()
