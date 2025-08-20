# Multimodal Video Sentiment & Emotion Recognition SaaS

This project is a full-stack SaaS platform for multimodal video sentiment and emotion recognition. It features a PyTorch-based AI model that processes video, audio, and text to predict sentiment and emotion, and a modern web SaaS for user interaction, quota management, and real-time inference. The backend model is deployed on AWS SageMaker, and the SaaS is built with Next.js, React, Tailwind CSS, and Auth.js (T3 Stack).

---

## Features

- 🎥 Video sentiment & emotion analysis
- 📺 Video frame extraction
- 🎙️ Audio feature extraction
- 📝 Text embedding with BERT
- 🔗 Multimodal fusion (video, audio, text)
- 📊 Emotion & sentiment classification
- 🚀 Model training & evaluation (PyTorch, SageMaker)
- 📈 TensorBoard logging
- ☁️ AWS S3 for video storage
- 🤖 AWS SageMaker endpoint integration
- 🔐 User authentication (Auth.js)
- 🔑 API key management
- 📊 Usage quota tracking
- 📈 Real-time analysis results
- 🎨 Modern UI (Tailwind CSS)

---

## Project Structure

```
Emotion Recognition CV/
│
├── AI_Model/                  # PyTorch model, training, deployment
│   ├── dataset/               # MELD dataset (ignored by git)
│   ├── training/              # Training scripts & requirements.txt
│   ├── deployment/            # Deployment scripts (SageMaker)
│   ├── ...                    # Model code, utils, etc.
│
├── API_SaaS/
│   └── video-sentiment-saas/  # Next.js/React SaaS frontend & backend
│       ├── prisma/            # Database schema & migrations
│       ├── src/               # App source code (pages, components, etc.)
│       ├── .env.example       # Example env vars
│       ├── ...                # Config, scripts, etc.
│
├── .gitignore                 # Global ignore (includes dataset, build, etc.)
└── README.md                  # This file
```

---

## Setup & Installation

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd "Emotion Recognition CV"
```

### 2. Python Model Setup (AI_Model)

- Install Python 3.12+ if not already installed.
- Create a virtual environment:
  ```sh
  python3.12 -m venv venv
  venv\Scripts\activate  # On Windows
  # or
  source venv/bin/activate  # On Linux/Mac
  ```
- Install dependencies:
  ```sh
  pip install -r AI_Model/training/requirements.txt
  ```
- Download the MELD dataset and extract it to `AI_Model/dataset/`.

#### Training the Model (Locally or SageMaker)
- Edit configs as needed in `AI_Model/training/`.
- To train locally:
  ```sh
  python AI_Model/training/train.py
  ```
- To train on AWS SageMaker:
  1. Upload dataset to S3.
  2. Set up SageMaker role with S3 access.
  3. Run:
     ```sh
     python AI_Model/train_sagemaker.py
     ```

#### Deploying the Model (SageMaker Endpoint)
- Upload trained model to S3.
- Set up deployment role with SageMaker and CloudWatch permissions.
- Deploy endpoint:
  ```sh
  python AI_Model/deployment/deploy_endpoint.py
  ```

### 3. SaaS Setup (API_SaaS/video-sentiment-saas)

- Go to the SaaS directory:
  ```sh
  cd "API_SaaS/video-sentiment-saas"
  ```
- Install dependencies:
  ```sh
  npm install
  ```
- Copy `.env.example` to `.env` and fill in:
  - `DATABASE_URL` (e.g. PostgreSQL connection string)
  - `AUTH_SECRET`
  - `AWS_REGION`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`
- Initialize the database:
  ```sh
  npm run db:generate
  npm run db:push
  ```
- Start the development server:
  ```sh
  npm run dev
  ```
- For production:
  ```sh
  npm run build
  npm start
  ```

---

## Usage

- Users can upload videos via the SaaS UI.
- The backend sends video to the SageMaker endpoint for inference.
- Results (emotion, sentiment) are displayed in real time.
- Usage quotas and API keys are managed per user.

---

## TensorBoard Logs

- Download logs from S3:
  ```sh
  aws s3 sync s3://<your-bucket>/tensorboard ./tensorboard_logs
  ```
- Start TensorBoard:
  ```sh
  tensorboard --logdir tensorboard_logs
  ```
- Open http://localhost:6006 in your browser.

---

## AWS IAM Policy Examples

- SageMaker training/deployment roles need S3 and SageMaker permissions.
- Example S3 access policy:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:PutObject",
          "s3:GetObject",
          "s3:ListBucket",
          "s3:DeleteObject"
        ],
        "Resource": [
          "arn:aws:s3:::your-bucket-name",
          "arn:aws:s3:::your-bucket-name/*"
        ]
      }
    ]
  }
  ```
- Example endpoint invocation policy:
  ```json
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": ["sagemaker:InvokeEndpoint"],
        "Resource": ["arn:aws:sagemaker:us-east-1:YOUR_AWS_ACCOUNT:endpoint/YOUR_ENDPOINT_NAME"]
      }
    ]
  }
  ```

---

## Notes
- The MELD dataset is not included in this repo. Download it manually and place in `AI_Model/dataset/`.
- The `AI_Model/dataset/` folder is git-ignored for privacy and size.
- For production, secure your API keys and secrets.
- For more details, see comments in code and scripts in each folder.

---

## License
MIT (or your license here)
