import json
from openai import OpenAI

# Initialize OpenAI Client
client = OpenAI(api_key="YOUR_API_KEY_HERE")

risks = []

# -------------------------
# EC2 CHECK
# -------------------------
def check_ec2():
    with open("configs/ec2.json") as f:
        data = json.load(f)

    if data["public_ip"] == True:
        risks.append("EC2 instance has a public IP address.")

    if data["ssh_open_to_world"] == True:
        risks.append("Security Group allows SSH access from anywhere (0.0.0.0/0).")

    if data["ebs_encrypted"] == False:
        risks.append("EBS volume is not encrypted.")


# -------------------------
# S3 CHECK
# -------------------------
def check_s3():
    with open("configs/s3.json") as f:
        data = json.load(f)

    if data["public_access"] == True:
        risks.append("S3 bucket is publicly accessible.")

    if data["encryption"] == False:
        risks.append("S3 bucket encryption is disabled.")


# -------------------------
# IAM CHECK
# -------------------------
def check_iam():
    with open("configs/iam.json") as f:
        data = json.load(f)

    if data["admin_access"] == True:
        risks.append("IAM user has AdministratorAccess policy.")

    if data["mfa_enabled"] == False:
        risks.append("MFA is not enabled for IAM user.")


# -------------------------
# GENAI ANALYSIS
# -------------------------
def analyze_with_ai(risk):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a cloud security expert."},
            {"role": "user", "content": f"Explain the risk and provide remediation: {risk}"}
        ]
    )

    return response.choices[0].message.content


# -------------------------
# REPORT GENERATION
# -------------------------
def generate_report():

    print("\n====== CLOUD SECURITY REVIEW REPORT ======\n")

    if not risks:
        print("No risks detected ✅")
        return

    print(f"Total Risks Found: {len(risks)}\n")

    for i, risk in enumerate(risks, 1):
        print(f"Risk {i}: {risk}")

        try:
            ai_result = analyze_with_ai(risk)
            print("AI Recommendation:")
            print(ai_result)
        except Exception as e:
            print("AI analysis skipped (API issue).")
            print("Basic Recommendation: Follow AWS security best practices.\n")

        print("-" * 60)


# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    check_ec2()
    check_s3()
    check_iam()

    generate_report()
