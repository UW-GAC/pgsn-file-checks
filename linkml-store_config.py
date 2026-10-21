import argparse
import pandas as pd
import yaml


def main():
    parser = argparse.ArgumentParser(description="convert data")

    #parser.add_argument("--table_files", type=str, help="tsv with table files")
    parser.add_argument("--schema", type=str, help="schema")
    parser.add_argument("--config_file", type=str, default="config.yaml", help="config file")
    parser.add_argument("--db_file", type=str, default="data.ddb", help="db file")
    
    args = parser.parse_args()

    #df = pd.read_csv(args.table_files, sep="\t", header=None)
    #tables = df.iloc[:, 0]
    #col = [{t+"s": {"type": t}} for t in tables]

    #data = {"databases": {"db": {"handle": "duckdb:///data.ddb", "schema_location": args.schema, "collections": col}}}

    data = {"databases": {"db": {"handle": "duckdb:///"+args.db_file, "schema_location": args.schema}}}
    with open(args.config_file, "w", encoding="utf-8") as file:
        yaml.safe_dump(data, file, sort_keys=False)


if __name__ == "__main__":
    main()
