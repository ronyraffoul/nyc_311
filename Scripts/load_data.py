import pandas as pd

chunksize = 1_000_000  # adjust as needed
for i, chunk in enumerate(
    pd.read_csv("NYC_311_Data\combined.csv", chunksize=chunksize)
):
    chunk.to_csv(f"combined_part_{i}.csv", index=False)
