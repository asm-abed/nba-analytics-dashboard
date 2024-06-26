if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import numpy as np
import pandas as pd
from datetime import date, timedelta, datetime


@transformer
def transform(data, *args, **kwargs):
    df = pd.DataFrame(data['df'])
    games_df = pd.DataFrame(data['games'])

    games_df['GAME_DATE'] = pd.to_datetime(games_df['GAME_DATE'])

    merged_df = pd.merge(df, games_df[['GAME_ID', 'WL', 'TEAM_ABBREVIATION', 'GAME_DATE']], on=['GAME_ID', 'TEAM_ABBREVIATION'], how='left')

    merged_df['win'] = np.where(merged_df['WL'] == 'W', 1, 0)
    
    merged_df = merged_df.drop(columns = ['NICKNAME', 'START_POSITION', 'COMMENT', 'TEAM_CITY', 'TEAM_ID', 'WL'])

    merged_df.rename(columns={
        'MIN': 'mins_played',
        'FGM': 'field_goal_made',
        'FGA': 'field_goal_attempt',
        'FG_PCT': 'field_goal_pct',
        'FG3M': 'three_pt_made',
        'FG3A': 'three_pt_attempt',
        'FG3_PCT': 'three_pt_pct',
        'FTM': 'free_throw_made',
        'FTA': 'free_throw_attempt',
        'FT_PCT': 'free_throw_pct',
        'PLUS_MINUS': 'plusminus',
        'TO':'TOV',
        'GAME_ID': 'game_id',
        'PLAYER_ID':'player_id',
        'TEAM_ABBREVIATION':'team',
        'PLAYER_NAME':'player',
        'GAME_DATE':'game_date'
        }, inplace=True)


    merged_df['mins_played']=merged_df['mins_played'].str.split(':').str[0].astype(float).astype(int)
    
    today = (date.today() - timedelta(days=2))

    if today >= datetime(2024, 4, 16).date():
        merged_df['season_id'] = 42023
        merged_df['season_type'] = 'Playoffs'
    else:
        merged_df['season_id'] = 22023
        merged_df['season_type'] = 'Regular Season'


    return merged_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'