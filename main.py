import os
import time
from datetime import timedelta

import funtions as fun
import read_source as read
from common import config

if __name__=='__main__':

    path_file_prints = config()['source']['path_json_prints']
    path_file_taps = config()['source']['path_json_taps']
    path_file_pays = config()['source']['path_csv_pays']

    current_path = os.getcwd()
    sub_folder_file_prints = current_path + path_file_prints
    sub_folder_file_taps = current_path + path_file_taps
    sub_folder_file_pays = current_path + path_file_pays
    
    start_time = time.time()

    "Extract and transform data from prints, taps and pays files"

    class_file_reader_prints = read.FileReader(sub_folder_file_prints)
    class_file_reader_taps = read.FileReader(sub_folder_file_taps)
    class_file_reader_pays = read.FileReader(sub_folder_file_pays)

    "Transform data from prints, taps and pays files"

    df_prints = (
        class_file_reader_prints.read_and_process_file()
            .pipe(fun.join_data, 'event_data')
            .pipe(fun.rename_columns, 'prints')
            .pipe(fun.convert_to_datetime, 'day_prints')
            .pipe(fun.drop_column, 'event_data_prints')
    )

    df_taps = (
        class_file_reader_taps.read_and_process_file()
            .pipe(fun.join_data, 'event_data')
            .pipe(fun.rename_columns, 'taps')
            .pipe(fun.convert_to_datetime, 'day_taps')
            .pipe(fun.drop_column, 'event_data_taps')
    )

    df_pays = (
        class_file_reader_pays.read_csv_file()
            .pipe(fun.rename_columns, 'pays')
            .pipe(fun.convert_to_datetime, 'pay_date_pays')
    )

    "Parameters for the analysis"

    now = df_prints['day_prints'].max()
    week_ago = now - timedelta(days=7)
    three_weeks_ago = now - timedelta(weeks=3)

    left_on_counts_df_prints = ['user_id_prints', 'value_prop_prints']
    right_on_counts_df_prints = ['user_id_prints_last_week', 'value_prop_prints_last_week']
    left_on_counts_df_taps = ['user_id_taps', 'value_prop_taps']
    right_on_counts_df_taps = ['user_id_prints_last_week', 'value_prop_prints_last_week']
    left_on_df_q1 = ['day_prints_last_week', 'user_id_prints_last_week','value_prop_prints_last_week']
    right_on_df_q1 = ['day_taps', 'user_id_taps','value_prop_taps']
    group_columns = ['day_prints_last_week', 'user_id_prints_last_week','value_prop_prints_last_week']
    left_on_merged_q1 = ['day_prints_last_week', 'user_id_prints_last_week','value_prop_prints_last_week']
    right_on_merged_q1 = ['day_prints_last_week', 'user_id_prints_last_week','value_prop_prints_last_week']

    "Process data"

    df_last_week = fun.filter_by_date(df_prints, 'day_prints', week_ago, now)
    df_last_week = fun.rename_columns(df_last_week,'last_week')
    counts_df_prints = fun.process_data(df_prints, df_last_week,'inner',left_on_counts_df_prints, right_on_counts_df_prints,'day_prints', three_weeks_ago, now, 'counts_prints')
    counts_df_taps = fun.process_data(df_taps, df_last_week,'inner',left_on_counts_df_taps, right_on_counts_df_taps,'day_taps',three_weeks_ago, now,'counts_taps')
    df_q1 = fun.merge_dataframes(df_last_week, df_taps, 'inner' ,left_on_df_q1, right_on_df_q1)
    counts_q1_prints = fun.group_and_count(df_q1, group_columns, 'counts_q1')
    merged_q1 = fun.merge_dataframes(df_last_week, counts_q1_prints,'left', left_on_merged_q1, right_on_merged_q1)
    merged_q1 = fun.fill_na_with_zero(merged_q1,'counts_q1','counts_q1')
    merged_q1 = fun.add_clicked_or_not_column(merged_q1, 'clicked_or_not', 'counts_q1')
    merged_q2 = fun.merge_dataframes(merged_q1, counts_df_prints, 'left', ['user_id_prints_last_week', 'value_prop_prints_last_week'], ['user_id_prints', 'value_prop_prints'])
    merged_q2 = fun.fill_na_with_zero(merged_q2,'count_number_prop_views_3_weeks','counts_prints')
    merged_q3 = fun.merge_dataframes(merged_q2, counts_df_taps,'left',['user_id_prints_last_week', 'value_prop_prints_last_week'], ['user_id_taps', 'value_prop_taps'])
    merged_q3 = fun.fill_na_with_zero(merged_q3,'count_number_prop_click_3_weeks','counts_taps')
    counts_df_pays,df_grouped_total_pays = fun.process_data_plus(df_pays, df_last_week, 'inner',['user_id_pays', 'value_prop_pays'], ['user_id_prints_last_week', 'value_prop_prints_last_week'],'pay_date_pays',three_weeks_ago, now,'total_pays','counts_pays')
    merged_q4 = fun.merge_dataframes(merged_q3, counts_df_pays, 'left', ['user_id_prints_last_week', 'value_prop_prints_last_week'],['user_id_pays', 'value_prop_pays'])
    merged_q4 = fun.fill_na_with_zero(merged_q4,'count_number_payments_3_weeks','counts_pays')
    merged_q5 = fun.merge_dataframes(merged_q4, df_grouped_total_pays, 'left', ['user_id_prints_last_week', 'value_prop_prints_last_week'],['user_id_pays', 'value_prop_pays'])
    merged_q5 = fun.fill_na_with_zero(merged_q5,'total_pays','total_pays')
    result = merged_q5[['day_prints_last_week','user_id_prints_last_week','position_prints_last_week','value_prop_prints_last_week','clicked_or_not','count_number_prop_views_3_weeks', 'count_number_prop_click_3_weeks', 'count_number_payments_3_weeks', 'total_pays']]
    result = fun.remove_string_from_column_names(result, '_last_week')

    print(result.head())
    
    end_time = time.time() 
    total_time = end_time - start_time 
    print(f"Prcess time: {total_time} seconds")