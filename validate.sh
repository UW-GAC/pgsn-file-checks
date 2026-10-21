#! /bin/bash

schema=$1
file=$2
db_config="tmp_config.yaml"
db_file="tmp_db.ddb"

python3 linkml-store_config.py --schema $schema --config_file ${db_config} --db_file ${db_file}

while read -r table_name table_file; do
    data_type="${table_file##*.}"
    yaml_file="${table_file%.*}".yaml
    python3 convert_data.py \
        --data_type ${data_type} --data_file ${table_file} \
        --output_type yaml --output_file ${yaml_file} \
        --top_level ${table_name}s

    echo "Checking ${table_file}"
    linkml validate -s ${schema} ${yaml_file}

    linkml-store -C ${db_config} -d ${db_file} -c ${table_name} insert ${table_file}
done < "$file"

echo "Checking table references"
linkml-store --set ensure_referential_integrity=true \
    --schema $schema \
    -d ${db_file} \
    validate -O csv \
    | grep Referential

rm ${db_config} ${db_file}
