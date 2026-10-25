"""Deterministically order a dependency graph and detect cycles."""

from __future__ import annotations

from collections.abc import Mapping, Set


class DependencyCycleError(ValueError):
    """Raised when a dependency graph contains a cycle."""


def topological_order(graph: Mapping[str, Set[str]]) -> list[str]:
    """Return a stable dependency-first ordering for *graph*."""
    nodes = set(graph)
    for dependencies in graph.values():
        nodes.update(dependencies)

    pending = {node: set(graph.get(node, set())) for node in nodes}
    ordered: list[str] = []

    while pending:
        ready = sorted(node for node, dependencies in pending.items() if not dependencies)
        if not ready:
            cycle_nodes = ", ".join(sorted(pending))
            raise DependencyCycleError(f"cycle detected among: {cycle_nodes}")

        ordered.extend(ready)
        for node in ready:
            pending.pop(node)
        for dependencies in pending.values():
            dependencies.difference_update(ready)

    return ordered

