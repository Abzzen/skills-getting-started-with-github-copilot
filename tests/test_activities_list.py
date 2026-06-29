def test_get_activities_returns_dictionary_with_expected_keys(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "Programming Class" in payload
