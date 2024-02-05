if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


import polars as pl

@transformer
def transform(data_df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    print("Rows with zero passengers:", (data_df[['passenger_count', 'trip_distance']].isin([0]).sum()))

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    data_df.columns = (data_df.columns
                    .str.replace(' ', '_')
                    .str.lower()
    )

    return data_df[(data_df['passenger_count'] > 0) & (data_df['trip_distance'] > 0)]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output ['passenger_count'].isin([0]).sum() == 0
    assert output ['trip_distance'].isin([0]).sum() == 0
