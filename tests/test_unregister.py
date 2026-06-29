def test_unregister_success_removes_participant(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "remove.student@mergington.edu"
    signup_endpoint = f"/activities/{activity_name}/signup"
    unregister_endpoint = f"/activities/{activity_name}/participants"
    client.post(signup_endpoint, params={"email": student_email})

    # Act
    response = client.delete(unregister_endpoint, params={"email": student_email})
    activities_response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {student_email} from {activity_name}"
    assert student_email not in activities_response.json()[activity_name]["participants"]


def test_unregister_not_signed_up_participant_returns_404(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "not.signed@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": student_email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_nonexistent_activity_returns_404(client):
    # Arrange
    activity_name = "Nonexistent Club"
    student_email = "student@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": student_email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
