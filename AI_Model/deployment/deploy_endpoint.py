from sagemaker.pytorch import PyTorchModel
import sagemaker


def deploy_endpoint():
    sagemaker.Session()
    role = "arn:aws:iam::659539930139:role/sentiment-analysis-deploy-endpoint-role"

    model_uri = "s3://sentiment-analysis-saas-vutl/inference/model.tar.gz"

    model = PyTorchModel(
        model_data=model_uri,
        role=role,
        framework_version="1.11.0",
        py_version="py38",
        entry_point="inference.py",
        source_dir=".",
        name="sentiment-analysis-model",
    )

    predictor = model.deploy(
        initial_instance_count=1,
        instance_type="ml.g5.xlarge",
        endpoint_name="sentiment-analysis-endpoint",
    )


if __name__ == "__main__":
    deploy_endpoint()