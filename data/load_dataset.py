from datasets import load_dataset


def load_java_codegen_dataset(limit=5000):

    print("Loading Java code generation dataset...")

    dataset = load_dataset(
        "google/code_x_glue_tc_text_to_code",
        split="train"
    )

    samples = []

    for i, item in enumerate(dataset):

        prompt = item["nl"]
        code = item["code"]

        samples.append({
            "id": str(i),
            "prompt": prompt,
            "code": code
        })

        if len(samples) >= limit:
            break

    print("Loaded:", len(samples))

    return samples