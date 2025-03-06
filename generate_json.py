import json
import glob
import os

def parse_example(file_path):
    """
    Reads the input file and splits it into HTML and Java parts.
    Expects markers '===HTML===' and '===JAVA===' in the file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    try:
        html_part = content.split("===HTML===")[1].split("===JAVA===")[0].strip()
        java_part = content.split("===JAVA===")[1].strip()
    except IndexError:
        raise ValueError(f"The input file {file_path} is not formatted correctly. It must contain both '===HTML===' and '===JAVA===' markers.")
    
    return html_part, java_part

def create_json_line(html, java, user_action):
    """
    Creates a JSON object in the chat format.
    """
    system_message = (
        "You are an expert in generating Selenium Java page object classes using provided DOM information. "
        "Follow the framework’s guidelines: use SeleniumBase wrapper methods, proper locators, and insert TODO comments if a mapping is missing."
    )
    
    user_message = (
        f"Given the following DOM structure:\n```html\n{html}\n```\n"
        f"Action to perform: {user_action}\n"
    )
    
    return {
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": java}
        ]
    }

def main():
    # Get all .txt files in the 'training' folder.
    input_files = glob.glob(os.path.join("training", "*.txt"))
    
    user_action = "Generate a Selenium Java page object class for this DOM."
    output_file = "training_data_chat.jsonl"
    
    # Open the output file once in append mode.
    with open(output_file, "a", encoding='utf-8') as out_f:
        for input_file in input_files:
            try:
                html, java = parse_example(input_file)
                json_obj = create_json_line(html, java, user_action,)
                jsonl_line = json.dumps(json_obj, ensure_ascii=False)
                out_f.write(jsonl_line + "\n")
                print(f"Processed {input_file}")
            except ValueError as e:
                print(f"Skipping {input_file}: {e}")

if __name__ == "__main__":
    main()
