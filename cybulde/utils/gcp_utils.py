from google.cloud import secretmanager


def access_secret_version(project_id: str, secret_id: str, version_id: str = "1") -> str:
    """
    Access the payload for the given secret version if one exists
    """
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")
    return payload
