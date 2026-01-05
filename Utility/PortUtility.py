class PortUtility:
    def __init__(self):
        self.video_dir = "/static/videos/"
        self.image_dir = "/static/images/"
    
    def project_desc(self, project_id : 1):
        if(project_id == 1):
            video_url = self.video_dir + "Project1.mp4"
            tech_stack = "Python, FastAPI, sklearn, SQL Server, ASP.Net Core 9.0, Docker"
            project_url = "https://omscs-spi7.onrender.com/"
            desc = ["Bundled the ML classifier in FastAPI microservices for real-time risk prediction.", "Built a data preprocessing pipeline for automated data transformation, batch loading and feature engineering for model training using unbalanced dataset.", "Engineered ensemble ML models achieving 83% recall and 85% precision using Random Forest + SMOTE hybrid sampling strategies.", "Implemented SHAP explanations for transparent decision-making and containerizing with Docker for Azure deployment.", "Logged the effect of hyper-parameters on the ML classifier using MLFlow"]
        elif(project_id == 2):
            video_url = self.video_dir + "Project2.mp4"
            tech_stack = "Python, Flask, NLP, Pytorch, sklearn, D3.js"
            project_url = "#"
            desc = ["Voting-Based Ensemble forecasting model combining Gradient Boosting, Random Forest, and RNN/LSTM to predict S&P 500 index movements(numeric data) based on macroeconomic indicators(numeric data), and news sentiment features(NLP)", "Optimized model weights using linear programming, reducing forecast error rates by 20% compared to standalone methods", "Visualized global index correlations and built dashboards (bivariate charts, sentiment vs % change, historical vs predicted) using D3.js to support explainability and decision-making."]
        elif(project_id == 3):
            video_url = self.image_dir + "Project3.png"
            tech_stack = "Python, PyTorch, sklearn, MLFlow"
            project_url = "https://drive.google.com/file/d/1okwRKc7Oc4hO483ELI4HO071e7YZ5Oin/view?usp=drive_link"
            desc = ["Developed Proof of Concept ANN models with dimensionality reduction (PCA, ICA) and clustering (K-Means, EM) for bankruptcy risk assessment.", "Optimized model performance by 20–27% through ICA, and achieved complete elimination of Type-II errors using EM clustering over K-Means.", "Delivered a more accurate and reliable bankruptcy risk assessment framework, enhancing interpretability for financial decision-makers."]
        
        return video_url, tech_stack, project_url, desc
                     