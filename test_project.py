"""Pytest pro project.py."""

import project
import pytest
from unittest import mock


@mock.patch('project.input', return_value=254)
def test_numberSelection(mock_n):
    """Test pro funkci numberSelection()."""
    assert project.numberSelection() is None


@mock.patch('project.input', return_value='14')
def test_numberSelection2(mock_n):
    """Test pro funkci numberSelection()."""
    assert project.numberSelection() is None


@mock.patch('project.input', return_value='exit')
def test_numberSelection4(mock_n):
    """Test pro funkci numberSelection()."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        project.numberSelection()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'Program byl ukončen'


@mock.patch('project.input', return_value=3)
def test_systemSelection(mock_s):
    """Test pro funkci systemSelection()."""
    assert project.systemSelection() is None


@mock.patch('project.input', return_value='1')
def test_systemSelection2(mock_s):
    """Test pro funkci systemSelection()."""
    assert project.systemSelection() is None


@mock.patch('project.input', return_value='exit')
def test_systemSelection4(mock_n):
    """Test pro funkci systemSelection()."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        project.systemSelection()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 'Program byl ukončen'
