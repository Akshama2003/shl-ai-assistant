def format_list(value):
    if isinstance(value, list):
        return ", ".join(value) if value else "Not specified"
    return value or "Not specified"


def compare(query, documents):
    if len(documents) < 2:
        return "I couldn't find enough SHL assessments in the catalog to compare."

    selected = documents[:2]

    response = "Here is a catalog-grounded comparison of the SHL assessments:\n\n"

    for doc in selected:
        name = doc.get("name", doc.get("title", "Unknown Assessment"))
        description = doc.get("description", "No description available.")
        duration = doc.get("duration", "Not specified")
        remote = doc.get("remote", "Not specified")
        adaptive = doc.get("adaptive", "Not specified")
        keys = format_list(doc.get("keys", []))
        job_levels = format_list(doc.get("job_levels", []))
        languages = format_list(doc.get("languages", []))
        url = doc.get("link", doc.get("url", "https://www.shl.com/"))

        response += (
            f"Assessment: {name}\n"
            f"Purpose: {description}\n"
            f"Assessment Areas: {keys}\n"
            f"Duration: {duration or 'Not specified'}\n"
            f"Remote Testing: {remote}\n"
            f"Adaptive: {adaptive}\n"
            f"Job Levels: {job_levels}\n"
            f"Languages: {languages}\n"
            f"URL: {url}\n\n"
            "----------------------------------------\n\n"
        )

    return response