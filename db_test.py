import argparse
import os
import sys

import psycopg


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Test a PostgreSQL connection.")
    parser.add_argument("password", nargs="?", default=os.getenv("POSTGRES_PASSWORD", ""), help="PostgreSQL password")
    parser.add_argument("--host", default=os.getenv("POSTGRES_HOST", "localhost"))
    parser.add_argument("--dbname", default=os.getenv("POSTGRES_DB", "postgres"))
    parser.add_argument("--user", default=os.getenv("POSTGRES_USER", "postgres"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    conn_params = {
        "host": args.host,
        "dbname": args.dbname,
        "user": args.user,
        "password": args.password,
    }

    if not conn_params["password"]:
        print("Provide your PostgreSQL password as an argument or set POSTGRES_PASSWORD and run again.")
        return 1

    try:
        with psycopg.connect(**conn_params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                print(cur.fetchone()[0])
    except Exception as exc:
        print(f"Connection failed: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
