from openai import OpenAI
client = OpenAI()

job_status = client.fine_tuning.jobs.retrieve("ftjob-OSDjON9RySojAICvCxFxMjuY")
print("Current job status:", job_status)