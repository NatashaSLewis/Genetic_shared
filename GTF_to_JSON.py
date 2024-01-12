import pandas as pd
import json
import os

#*** Insert path to your directory with GTF file here
directory_path = '/Users/natasha/Noor'  #*** Replace with the actual path to your directory
os.chdir(directory_path)

def gtf_to_json(gtf_file, json_file):
    # Read GTF file into a DataFrame using pandas
    columns = ["seqname", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
    df = pd.read_csv(gtf_file, sep='\t', comment='#', header=None, names=columns, dtype={0: str})

    # Convert DataFrame to a list of dictionaries
    gtf_list = []
    for index, row in df.iterrows():
        entry = {
            "seqname": row["seqname"],
            "source": row["source"],
            "feature": row["feature"],
            "start": int(row["start"]),
            "end": int(row["end"]),
            "score": row["score"],
            "strand": row["strand"],
            "frame": row["frame"],
            "attribute": row["attribute"]
        }
        gtf_list.append(entry)

    # Write the list of dictionaries to a JSON file
    with open(json_file, 'w') as json_out:
        json.dump(gtf_list, json_out, indent=2)

#*** Insert name of your Input GTF file and output JSON file here
gtf_to_json('sample.GTF', 'output.json') 
