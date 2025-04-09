from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Wild Rydes – DevOps Test #2: Deployment in Action!</h1>
    <p>Hello! My name is <strong>Ketul Shah</strong>, and my student ID is <strong>100984227</strong>.</p>
    <p>This application is a demonstration of continuous integration and deployment using AWS CloudFormation, CodePipeline, CodeBuild, and ECS Fargate. The pipeline automatically picks up changes from GitHub, builds the Docker image, pushes it to Amazon ECR, and deploys the updated container to an ECS service behind an Application Load Balancer. It's been a great experience learning how to automate infrastructure deployment and manage application lifecycle using modern DevOps practices.</p>
    <p><em>Deployment successful — the system is working as intended!</em></p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
