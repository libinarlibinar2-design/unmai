from __future__ import annotations

from typing import Any, Dict


def own_dict(obj: Any) -> Dict[str, Any]:
    return obj if isinstance(obj, dict) else {}
