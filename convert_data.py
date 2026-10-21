import argparse
import pandas as pd
import yaml
import json


def main():
    parser = argparse.ArgumentParser(description="convert data")

    parser.add_argument("--data_file", type=str, help="data file")
    parser.add_argument("--data_type", type=str, help="tsv or csv")
    parser.add_argument("--output_file", type=str, help="output file")
    parser.add_argument("--output_type", type=str, help="yaml or json")
    parser.add_argument("--top_level", type=str, help="string for top level")
    
    args = parser.parse_args()

    if args.data_type == "tsv":
        sep = "\t"
    elif args.data_type == "csv":
        sep = ","
    else:
        raise ValueError("data type must be tsv or csv")

    df = pd.read_csv(args.data_file, sep=sep)

    data = df.to_dict(orient='records')
    if args.top_level is not None:
        data = { args.top_level: data }

    with open(args.output_file, "w", encoding="utf-8") as file:
        if args.output_type == "json":
            json.dump(data, file, sort_keys=False, indent=2)
        elif args.output_type == "yaml":
            yaml.safe_dump(data, file, sort_keys=False)
        else:
            raise ValueError("output type must be json or yaml")


if __name__ == "__main__":
    main()
