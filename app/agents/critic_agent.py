from app.execution.java_executor import validate_java_code
from app.tools.learning_tool import learn_new_example


def critic_agent(state):

    code = state["generated_code"]

    valid, output = validate_java_code(code)

    attempts = state.get("attempts", 0) + 1

    if valid:

        learn_new_example(
            state["query"],
            code
        )

    return {

        "valid": valid,
        "compiler_output": output,
        "attempts": attempts

    }