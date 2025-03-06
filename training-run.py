from openai import OpenAI
client = OpenAI()

file_response = client.files.create(
    file=open("training_data_chat.jsonl", "rb"),
    purpose="fine-tune"
)
training_file_id = file_response.id

print("Training file uploaded. File ID:", training_file_id)

job_response = client.fine_tuning.jobs.create(
    training_file=training_file_id,
    model="gpt-4o-mini-2024-07-18")
print("Fine-tune job started:", job_response)
