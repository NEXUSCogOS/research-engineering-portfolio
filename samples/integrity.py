"""Create and verify deterministic SHA-256 file manifests."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Return the SHA-256 digest for *path* without loading it all at once."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_manifest(root: Path, excluded_names: Iterable[str] = ()) -> dict[str, str]:
    """Return a stable relative-path-to-digest manifest for regular files."""
    root = root.resolve()
    excluded = set(excluded_names) | {".git"}
    files = (
        path
        for path in root.rglob("*")
        if path.is_file() and not any(part in excluded for part in path.parts)
    )
    return {
        path.relative_to(root).as_posix(): sha256_file(path)
        for path in sorted(files)
    }


def verify_manifest(root: Path, manifest: dict[str, str]) -> dict[str, list[str]]:
    """Report missing, changed and unexpected files relative to *manifest*."""
    current = build_manifest(root)
    expected_paths = set(manifest)
    current_paths = set(current)
    return {
        "missing": sorted(expected_paths - current_paths),
        "changed": sorted(
            path
            for path in expected_paths & current_paths
            if manifest[path] != current[path]
        ),
        "unexpected": sorted(current_paths - expected_paths),
    }

