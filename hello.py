import polars as pl

def main():
    dummy_df = pl.DataFrame(
        {
            "waktu":[1,2,3],
            "tegangan": [1,2,3]
        }
    )
    print(dummy_df)


if __name__ == "__main__":
    main()
