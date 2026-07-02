def compare(query, documents):

    if len(documents) < 2:
        return "I couldn't find enough assessments to compare."

    a = documents[0]
    b = documents[1]

    return f"""
Comparison

{a.get('title', a.get('name'))}

vs

{b.get('title', b.get('name'))}

Categories:
{a.get('category')} vs {b.get('category')}
"""