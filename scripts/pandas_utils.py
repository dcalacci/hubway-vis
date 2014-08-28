import pandas as pd

def apply_iteratively(df, func, colname=None, percent_alert=10, dump_dir=None):
    """applies func iteratively to df.

    func: a function that does something to each row of df.

    df: the dataframe to apply func to.

    colname: optional. Will apply func only to colname if it is provided.

    percent_alert: optional. the percent progress to print out.

    dump_dir: optional. will save intermediate results to this file if
    it is provided.

    Returns the output column/list of the function application.

    """
    result = []
    count = 0
    percent_alert = float(percent_alert)/100
    for n, row in df.iterrows():
        count += 1
        if count % int(len(df)*percent_alert) == 0:
            print time.strftime("[%m/%d/%y : %H:%M:%S]"), "processed", (float(count)/len(df)) * 100, "% of rows, saving intermediate file..."
            if dump_dir is not None:
                save_res(result, count, dump_dir)

        if colname is None:
            result.append(func(row))
        else:
            result.append(func(row[colname]))

    if dump_dir is not None:
        save_res(result, count, dump_dir, final=True)

    return result