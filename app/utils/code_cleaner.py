import re


def extract_java_code(text: str) -> str:
    pattern = r"```java\s*(.*?)```"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if match:
        code = match.group(1).strip()
    else:
        fallback = re.search(r"(public\s+(class|interface|enum)\s+\w+.*)", text, re.DOTALL)
        if fallback:
            code = fallback.group(1).strip()
        else:
            code = text.strip()

    if "class " not in code:
        code = f"""public class Main {{

{code}

}}"""

    return code.strip()