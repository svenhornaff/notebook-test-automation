from pytest import fixture
from testbook import testbook

notebook_path = "/Users/deepsnow/Workspace/Python/notebook-test-automation/notebooks/simple.ipynb"

@fixture(scope="module")
def simple_nb():
    with testbook(notebook_path, execute=True) as simple_nb:
        yield simple_nb

def test_summ(simple_nb):
    summ = simple_nb.ref('summ') # get reference to function
    
    assert summ(2,3) == 5
    
def test_get_details(simple_nb):
    with simple_nb.patch('requests.get') as mock_get:
        get_details = simple_nb.ref('get_details') # get reference to function
        get_details('https://github.com')

        mock_get.assert_called_with('https://github.com')

def test_get_status_code(simple_nb):
    get_status_code = simple_nb.ref('get_status_code') # get reference to function
    assert get_status_code('https://github.com') == 200
    
def test_dataframe_manipulation(simple_nb):
    # import pandas -- notebook cell needs a tag
    simple_nb.execute_cell('imports')

    # Inject a dataframe with code
    simple_nb.inject(
        """
        df = pandas.DataFrame([[1, None, 3], [4, 5, 6]], columns=['a', 'b', 'c'], dtype='float')
        """
    )

    # Perform manipulation - remove drop NaN rows
    simple_nb.execute_cell('manipulation')

    # Inject assertion into notebook
    simple_nb.inject("assert len(df) == 1")

def test_stdout(simple_nb):
    print(simple_nb.cell_output_text(1))

