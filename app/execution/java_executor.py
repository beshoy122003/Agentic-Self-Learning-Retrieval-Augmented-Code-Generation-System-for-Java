# code validation for java code, we can use subprocess to call javac and check if the code compiles successfully. 
# This is a simple way to validate the generated code without executing it, which can be dangerous. 

import subprocess
import os
import re
import time


def extract_class_name(code):

    match = re.search(r'public\s+class\s+(\w+)', code)

    if match:
        return match.group(1)

    return "Main"


def validate_java_code(code):

    class_name = extract_class_name(code)

    filename = f"{class_name}.java"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    try:

        result = subprocess.run(
            [r"C:\Program Files\Eclipse Adoptium\jdk-25.0.2.10-hotspot\bin\javac.exe", filename],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return True, "Compilation Success"

        return False, result.stderr

    finally:

        # انتظار بسيط حتى يفرغ javac الملف
        time.sleep(0.2)

        # حذف ملف java
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass

        # حذف ملف class
        class_file = f"{class_name}.class"

        if os.path.exists(class_file):
            try:
                os.remove(class_file)
            except:
                pass