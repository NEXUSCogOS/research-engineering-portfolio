"""Profile simple record collections without third-party dependencies."""

from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Mapping
from typing import Any


def profile_records(
    records: Iterable[Mapping[str, Any]],
    required_fields: Iterable[str],
    identity_field: str,
) -> dict[str, Any]:
    """Summarize missing required values and duplicate record identities."""
    rows = list(records)
    required = tuple(required_fields)
    missing = {
        field: sum(row.get(field) in (None, "") for row in rows)
        for field in required
    }
    identities = [row.get(identity_field) for row in rows]
    counts = Counter(value for value in identities if value not in (None, ""))
    duplicates = sorted(value for value, count in counts.items() if count > 1)
    return {
        "record_count": len(rows),
        "missing_required": missing,
        "duplicate_identities": duplicates,
        "complete": not any(missing.values()) and not duplicates,
    }

