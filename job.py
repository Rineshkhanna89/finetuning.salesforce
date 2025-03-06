from openai import OpenAI

client = OpenAI()

job_response = client.fine_tuning.jobs.create(
    training_file='file-KGEDq95DYFXg4XhLsRGbu2',
    model="gpt-4o-mini-2024-07-18")
print("Fine-tune job started:", job_response)