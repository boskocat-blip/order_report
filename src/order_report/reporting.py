import json
from pathlib import Path
from order_report.config import logger

def spara_rapport_till_json(data: dict, output_path: Path) -> None:
    """
    Sparar en rapport (dict) till en JSON-fil.
    """
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logger.info(f"Rapport sparad till: {output_path}")
    except Exception as e:
        logger.error(f"Misslyckades att spara rapporten till {output_path}: {e}")
        raise