import pandas as pd

def truncar_fields(valor):
    if isinstance(valor, str):
        return valor[:5000]
    return valor

def join_data(df,column):
        df = df.join(df[column].apply(pd.Series))
        return df

def rename_columns(df,alias):
        df = df.rename(columns=lambda x: x + '_' + alias)
        return df

def convert_to_datetime(df,column_date):
    df[column_date] = pd.to_datetime(df[column_date])
    return df

def drop_column(df,column):
    df = df.drop([column], axis=1)
    return df

def filter_by_date(df, date_column, start_date, end_date):
    return df[(df[date_column] >= start_date) & (df[date_column] <= end_date)]

def merge_dataframes(df_left, df_right, how,left_on, right_on):
    return pd.merge(df_left, df_right, how=how, left_on=left_on, right_on=right_on)

def process_data(df_left, df_right, how, left_on, right_on, column_filter,start_date, end_date,name_column_counts):
    df = pd.merge(df_left, df_right, how=how, left_on=left_on, right_on=right_on)
    df = df[(df[column_filter] >= start_date) & (df[column_filter] <= end_date)]
    counts = df.groupby(left_on).size()
    df = counts.reset_index(name=name_column_counts)
    return df

def process_data_plus(df_left, df_right, how, left_on, right_on, column_filter,start_date, end_date,sum_total,name_column_counts):
    df = pd.merge(df_left, df_right, how=how, left_on=left_on, right_on=right_on)
    df = df[(df[column_filter] >= start_date) & (df[column_filter] <= end_date)]
    counts = df.groupby(left_on).size()
    df_grouped = df.groupby(left_on)[sum_total].sum().reset_index()
    df = counts.reset_index(name=name_column_counts)
    return df,df_grouped

def add_clicked_or_not_column(df,new_column,column_name):
    df[new_column] = df[column_name].apply(lambda x: True if x == 1 else False)
    return df

def fill_na_with_zero(df,new_column,column_name):
    df[new_column] = df[column_name].fillna(0)
    return df

def group_and_count(df, group_columns, count_name):
    counts = df.groupby(group_columns).size()
    return counts.reset_index(name=count_name)

def remove_string_from_column_names(df, string_to_remove):
    df = df.rename(columns={col: col.replace(string_to_remove, '') for col in df.columns})
    return df