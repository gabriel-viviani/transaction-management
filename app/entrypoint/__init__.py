from fastapi import Header, HTTPException, status


def check_content_type(content_type: str = Header(...)):
    if content_type != "application/json":
        raise HTTPException(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Unsupported media type: {content_type}.",
        )
