
import argparse
import json
from agent.core import run_agent


def main():
    parser = argparse.ArgumentParser(
        description="Early Warning System for Students at Risk"
    )
    parser.add_argument("--json", help="Question to analyze")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    query = args.json

    if not query:
        parser.error('Use --json "your question"')

    result = run_agent(query, dry_run=args.dry_run)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
