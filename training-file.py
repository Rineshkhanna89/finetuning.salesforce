from openai import OpenAI
client = OpenAI()

file_response = client.files.create(
    file=open("training_data_chat.jsonl", "rb"),
    purpose="fine-tune"
)
training_file_id = file_response.id

print("Training file uploaded. File ID:", training_file_id)

