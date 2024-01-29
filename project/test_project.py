""" Tests for project.py my CS50p Final Project """

from unittest.mock import MagicMock, mock_open, patch
import pytest
from project import search, on_select, is_valid_entry


def test_search(mock_csv_data, mock_text_box, mock_decrypt_function):
    with patch('os.path.isfile', return_value=True):
        with patch('builtins.open', mock_open(read_data=mock_csv_data)):
            with patch('project.PROTEKTOR3000_ACTIVATED.decrypt', mock_decrypt_function):
                pattern = 'Luiz Fillipe Pinto da Silva'
                history = search(pattern, mock_text_box)

                # Verify that history contains the expected result
                expected_result = ['Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 139605','Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 811786',
                'Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 266845','Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 814934',
                'Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 745775']
                assert history == expected_result

                pattern = 'JOHN WICK'
                history = search(pattern, mock_text_box)
                expected_result = ['Name: John Wick, Appointment date: 10-10-2020, ID: 123456']
                assert history == expected_result

                pattern = ''
                history = search(pattern, mock_text_box)
                expected_result = ['Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 139605','Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 811786',
                'Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 266845','Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 814934',
                'Name: Luiz Fillipe Pinto da Silva, Appointment date: 11-06-2024, ID: 745775', 'Name: John Wick, Appointment date: 10-10-2020, ID: 123456']
                assert history == expected_result

                pattern = 'Joaquim da Silva'
                history = search(pattern, mock_text_box)
                expected_result = []
                assert history == expected_result

def test_is_valid():
    # mocking the inputs
    mock_entries = {
        'name': MagicMock(get=MagicMock(return_value="Luiz Fillipe Pinto da Silva")),
        'date_of_birth_': MagicMock(get=MagicMock(return_value="11-06-1996")),
        'appointment_date': MagicMock(get=MagicMock(return_value="26-01-2024")),
        'height_': MagicMock(get=MagicMock(return_value="180")),
        'weight_': MagicMock(get=MagicMock(return_value="91.5")),
        'temperature_': MagicMock(get=MagicMock(return_value="36.9")),
        'heart_rate_': MagicMock(get=MagicMock(return_value="60")),
        'respiratory_rate_': MagicMock(get=MagicMock(return_value="12")),
        'blood_pressure': MagicMock(get=MagicMock(return_value="120/80")),
        'current_complain': MagicMock(get=MagicMock(return_value="Headache")),
        'comorbidities': MagicMock(get=MagicMock(return_value="None")),
        'medications': MagicMock(get=MagicMock(return_value="Venvanse 50mg")),
        'allergies': MagicMock(get=MagicMock(return_value="None")),
        'family_history': MagicMock(get=MagicMock(return_value="Hypertension")),
        'miscellaneous_notes': MagicMock(get=MagicMock(return_value="None")),
        'surgical_procedures': MagicMock(get=MagicMock(return_value="None")),
        'subjective': MagicMock(get=MagicMock(return_value="whats beauty")),
        'objective': MagicMock(get=MagicMock(return_value="BEG LOC MUC BNF RR 2T SS MVUD SRA TEC < 3 SEG")),
        'assessment': MagicMock(get=MagicMock(return_value="good job?")),
        'plan': MagicMock(get=MagicMock(return_value="improve")),
    }

    # mocking summary
    mock_summary = MagicMock()

    with patch('project.entries', mock_entries), patch('project.summary', mock_summary), patch('project.save_consult') as mock_save_consult:

        # Call the function
        worked  = is_valid_entry()

        # Check that save_consult was called due to valid entry
        mock_save_consult.assert_called()

        # Assert that the function returned True, indicating valid input
        assert worked is True

def test_on_select():
    with patch('project.entry_listbox_6', new=MagicMock()) as mock_listbox:
        mock_listbox.get.return_value = "Some consult data, ID: 12345"
        mock_listbox.curselection.return_value = 0

        with patch('project.display_consult') as mock_display_consult:
            consult_id = on_select(0)
            mock_display_consult.assert_called_with("12345")
            assert consult_id == "12345"







































































@pytest.fixture
def mock_csv_data():
    return '''Name,Appointment Date,ID
              Luiz Fillipe Pinto da Silva,11-06-2024,139605
              Luiz Fillipe Pinto da Silva,11-06-2024,811786
              Luiz Fillipe Pinto da Silva,11-06-2024,266845
              Luiz Fillipe Pinto da Silva,11-06-2024,814934
              Luiz Fillipe Pinto da Silva,11-06-2024,745775
              John Wick,10-10-2020,123456'''
@pytest.fixture
def mock_text_box():
    text_box = MagicMock()
    text_box.insert = MagicMock()
    return text_box

@pytest.fixture
def mock_decrypt_function():
    return lambda data: data  #RETUNS THE SAME DATA